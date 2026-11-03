#!/usr/bin/env python3
"""Normalize image filenames to lowercase English snake_case.

Run with --root PATH --dry-run to preview. Use --apply to rename files and
update image filename references in text files under the repository root.
"""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from functools import lru_cache
from pathlib import Path


IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"}
TEXT_EXTENSIONS = {".md", ".json", ".js", ".html", ".css", ".yml", ".yaml", ".txt", ".lua"}
COMMON_WORDS = set("""
advanced animal apple ammo armor assault axe bacon bag ball banana bandage bank barrel base battle ceramic gadget military vintage pump sawn off
basic battery bean bear beef belt berry bike bird biscuit black blade blanket blood blue boat
body bone book bottle box bread brick broken bronze brown bullet burger bus cable cake camera
can candy car card cargo casing cat chain cheese chicken chip chocolate cigar cleaner cleaning
clip cloth clothing club coal coffee coin cold combat computer copper crate cream croissant crop
crystal cup curry cutter damage dark data dead deer detector diamond dirty dough drink driver
drill drone drug duck dust egg electric energy engine evidence explosive eye face fake farm fast
feather fence file fire first fish fishing fit flashlight flour food fork fries fuel full game
garbage gas gear glass gold golf grape green grilled gun gunpowder hair hammer hand hard hat
head heavy helmet herb hide high hiking honey hook hot house hunting ice iron item jacket jar
juice key kitchen knife labor large laser leather left lemon license light lock lockpick log
long loose low lunch machine magazine mail marked mask meat medical medium metal milk mini mint
mixed money monitor motorcycle mount mountain mouth mouse mushroom nail navy neck night nitrogen nitro
oil orange ore package paint pair paper parts pasta pastry patch pedal pepper pet phone photo
pick picture pie pill pink pipe pistol pizza plant plastic plate pliers pocket police pool pork
potato powder press printer proof purple quality radio rail raw red repair rifle ring river rock
roll rope round rubber ruined safe salad salt sandwich sauce saw scrap screw screwdriver sea
security seed server shotgun side silver skin small smoke snack soda soft soup special spice
spider spray spring square steel stick stone storage strawberry street strip sugar suit sulfur
switch table tablet taco tail tape tea tech telephone tequila thermal ticket tin tire tool tooth
torch toy tracker trade trash tray treasure tree truck tuna tv two usb utility vanilla vegetable
vehicle video vine water weapon wheel white whiskey wine wire wolf wood wool work yellow yogurt
9mm 44magnum 762mm mk hp ap ballas advancedlockpick blackcat doghouse dogfood doghousekit
repairkit metaldetector metalscrap metaltrash bulletcasings birdhouse bookshelf lockpick safecracker
firework chips cassette headphones dogtag firstaid firstaidkit firstaidbandage nightstick radio
airsoft assaultcarbine assaultsmg autoshotgun bullpup bullpuprifle bullpupshotgun carbine carbine rifle
combat combatmg combatpdw combatpistol combatshotgun combatrifle compact compactlauncher compactrifle knuckles
doublebarrel marksman marksmanrifle machinepistol machinegun machinepistol minigun minismg microsmg
navyrevolver specialcarbine snowball stungun sweeper shotgunpump pumpshotgun sawnoffshotgun smg sniper
heavyshotgun heavyrifle heavypistol heavysniper launcher grenadelauncher marksmanpistol assault rifle
advanced kit lock pick lockpick lockpicks lockpicktool marked bills money bag ammo pouch scrap metal
ice cream hot dog hotdog hotdogbun strawberryroll strawberrymochi blue berry blueberry lemon lime
black bear blackcat black cat rabbitfood rabbit food petfood pet food tennisball tennis ball
bacon eggs egg baconandeggs caesar salad chickenstrip chickenstrips chickenwrap cheese fries
high quality highquality advancedkit advancedlockpick jumper cables jumpercables car battery carbattery
power washer powerwasher air freshener airfreshener cleaning wipes cleaningwipes lock pick lockpick
first aid firstaid repair kit repairkit tool box toolbox handcuffs police badge body camera bodycam
fish bait fishbait fishing rod fishingrod largemouth bass largemouthbass striped bass stripedbass
blue chip bluechip gold chip goldchip black chip blackchip casino chip casinoblackchip
weapon parts weaponparts mechanic kit mechanic kit electronics kit electronickit hacking device
hackingdevice security card securitycard access card accesscard bank card bankcard credit card
debit card debitcard phone card phonecard sim card simcard laptop computer laptop computer gameboy
game boy gameboy game console gameconsole controller game controller gamecontroller movie camera
moviecamera video camera videocamera digital camera digitalcamera camera lens cameralens
car jack carjack jumper cable jumpercables toolkit screw driver screwdriver set screwdriverset
wheelchair medical kit medkit firstaid kit firstaidkit blood sample bloodsample animal skin animalskin
bird nest birdnest gun powder gunpowder bullet casing bulletcasings shotgun shell shotgunshell
ammo crate ammocrate paint ball paintball paint ammo paintammo bean bag beanbag beanbagammo
french toast french toast bacon french toastbacon frenchtoastbacon grilled cheese grilledcheese
blueberry pie blueberrypie apple pie applepie chocolate chip chocolatechip strawberry cake strawberrycake
corn dog corndog hot sauce hotsauce soda can sodacan coffee bean coffeebean coffee cup coffeecup
ice tea iced tea icedtea black tea blacktea green tea greentea bubble tea bubbletea
chicken nugget chickennugget onion ring onionring onion rings onionrings fish and chips fishandchips
backwoods grape backwoodsgrape backwoods honey backwoodshoney russian cream russiancream
high quality scales highqualityscales dirty needle dirtyneedle hydrochloric acid hydrochloricacid
electronic kit electronickit advanced kit advancedkit lock pick lockpick screw driver screwdriverset
strawberry lemonade strawberrylemonade lemon lime lemonnlime mount lion mtlion mountain lion
bulletproof vest bulletproofvest advanced rifle advancedrifle assault rifle assaultrifle
heavy armor heavyarmor body armor bodyarmor riot shield riotshield fire extinguisher fireextinguisher
street sign streetsign stop sign stopsign yield sign yieldsign left turn leftturn right turn rightturn
walking man walkingman parking sign parkingsign no parking noparking u turn uturn
ocean bass blue fish bluefish catfish goldfish redfish sting ray stingray
clothing bag clothingbag money roll moneyroll cash roll cashroll pocket watch pocketwatch ancient coin
antique coin antique coin ancientcoin ww2 relic ww2relic broken detector brokendetector broken phone
brokenphone broken gameboy brokengameboy buried treasure buriedtreasure treasure key treasurekey
master key masterkey lottery ticket lottery ticket lottery ticket lottery ticket
armored truck armoredtruck flat tire flattire car door cardoor car hood carhood car battery carbattery
vehicle door vehicle door vehicle key vehiclekey race ticket raceticket casino chip casinochip
cardboard sign cardboardsign sticky note stickynote measuring tape measuringtape cleaning kit cleaningkit
stancer kit stancerkit tuner chip tunerchip nitrous oxide nitrousoxide nitrous kit nitrous kit
healing potion healingpotion mana potion manapotion health potion healthpotion
blue hulk bluehulk green hulk greenhulk orange hulk orangehulk purple hulk purplehulk red hulk redhulk
yellow hulk yellowhulk action figure actionfigure teddy bear teddybear plushie doll jet pack jetpack
gold chain goldchain silver chain silverchain billion dollar baby billiondollarbaby
grand theft auto grandtheftauto vinewood sign vinewoodsign rockford hill rockfordhill
""".split())
PROTECTED_WORDS = {"blueprint", "combat", "shotgun"}
CANONICAL_PAIRS = {("blue", "print"): "blueprint", ("com", "bat"): "combat"}


def words_from_text(root: Path) -> set[str]:
    words = set(COMMON_WORDS)
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() != ".md":
            continue
        if ".git" in path.parts:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            continue
        prose = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
        prose = re.sub(r"(?m)^.*(?:\.png|\[['\"]|\]\s*=|\bimage\s*=).*$", " ", prose, flags=re.IGNORECASE)
        words.update(word.lower() for word in re.findall(r"[A-Za-z]{2,}", prose))
        for value in re.findall(r"(?i)(?:label|description)\s*[:=]\s*['\"]([^'\"]+)", text):
            words.update(word.lower() for word in re.findall(r"[A-Za-z]{2,}", value))

    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in IMAGE_EXTENSIONS or ".git" in path.parts:
            continue
        stem = path.stem
        explicit_boundaries = any(char in stem for char in "_-") or bool(re.search(r"[a-z][A-Z]", stem))
        stem = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", stem)
        stem = re.sub(r"([A-Z])([A-Z][a-z])", r"\1_\2", stem)
        if explicit_boundaries:
            words.update(part.lower() for part in re.split(r"[^A-Za-z]+", stem) if len(part) >= 2)
    return words


def segment_compound(token: str, vocabulary: set[str]) -> list[str]:
    if token in PROTECTED_WORDS:
        return [token]
    if len(token) < 6:
        return [token]

    @lru_cache(maxsize=None)
    def best(start: int) -> tuple[str, ...] | None:
        if start == len(token):
            return ()
        protected = sorted((word for word in PROTECTED_WORDS if token.startswith(word, start)), key=len, reverse=True)
        if protected:
            word = protected[0]
            tail = best(start + len(word))
            if tail is not None:
                return (word, *tail)
        options = []
        for end in range(len(token), start + 1, -1):
            word = token[start:end]
            if start == 0 and end == len(token):
                continue
            if word in vocabulary and (len(word) >= 3 or word in {"ap", "bp", "hp", "mg", "mk", "mm", "mp", "tv", "usb", "vr"}):
                tail = best(end)
                if tail is not None:
                    options.append((word, *tail))
        if not options:
            return None
        return max(options, key=lambda parts: (len(parts), tuple(len(word) for word in parts)))

    parts = best(0)
    if not parts:
        return [token]
    canonical = []
    index = 0
    while index < len(parts):
        pair = tuple(parts[index:index + 2])
        if pair in CANONICAL_PAIRS:
            canonical.append(CANONICAL_PAIRS[pair])
            index += 2
        else:
            canonical.append(parts[index])
            index += 1
    return canonical if len(canonical) > 1 or canonical[0] != token else [token]


def normalized_stem(stem: str, vocabulary: set[str]) -> str:
    stem = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", stem)
    stem = re.sub(r"([A-Z])([A-Z][a-z])", r"\1_\2", stem)
    stem = re.sub(r"([A-Za-z])([0-9])", r"\1_\2", stem)
    stem = re.sub(r"([0-9])([A-Za-z])", r"\1_\2", stem)
    raw_parts = [part for part in re.split(r"[^A-Za-z0-9]+", stem) if part]
    output = []
    for part in raw_parts:
        if part.isdigit():
            output.append(part)
        else:
            output.extend(segment_compound(part.lower(), vocabulary))
    canonical = []
    index = 0
    while index < len(output):
        pair = tuple(output[index:index + 2])
        if pair in CANONICAL_PAIRS:
            canonical.append(CANONICAL_PAIRS[pair])
            index += 2
        else:
            canonical.append(output[index])
            index += 1
    return "_".join(canonical).lower()


def build_plan(root: Path) -> tuple[list[tuple[Path, Path]], list[str]]:
    vocabulary = words_from_text(root)
    images = sorted(
        (path for path in root.rglob("*") if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS and ".git" not in path.parts),
        key=lambda path: path.as_posix().casefold(),
    )
    proposals = []
    for source in images:
        stem = source.stem
        if "blueprints" in {part.casefold() for part in source.relative_to(root).parts}:
            stem = re.sub(r"(?i)^bp(?=[a-z])", "blueprint_", stem)
            stem = re.sub(r"(?i)blurprint", "blueprint", stem)
        target_name = normalized_stem(stem, vocabulary) + source.suffix.lower()
        proposals.append((source, source.with_name(target_name)))

    plan = []
    collision_notes = []
    by_parent: dict[str, list[tuple[Path, Path]]] = defaultdict(list)
    for pair in proposals:
        by_parent[pair[0].parent.as_posix().casefold()].append(pair)

    for pairs in by_parent.values():
        clusters: dict[str, list[tuple[Path, Path]]] = defaultdict(list)
        for pair in pairs:
            clusters[pair[1].name.casefold()].append(pair)
        reserved = set(clusters)
        final_names = {}
        for base_name, cluster in clusters.items():
            priority = sorted(
                cluster,
                key=lambda pair: (
                    pair[0].name.casefold() != pair[1].name.casefold(),
                    not bool(re.search(r"_\d+(?:\.|$)", pair[0].stem)),
                    not any(char in pair[0].stem for char in "_-") and not bool(re.search(r"[a-z][A-Z]", pair[0].stem)),
                    pair[0].as_posix().casefold(),
                ),
            )
            winner = priority[0]
            final_names[winner[0]] = winner[1]
            for duplicate_index, (source, target) in enumerate(priority[1:], start=2):
                candidate = f"{target.stem}_duplicate_{duplicate_index}{target.suffix}"
                suffix = duplicate_index
                while candidate.casefold() in reserved:
                    suffix += 1
                    candidate = f"{target.stem}_duplicate_{suffix}{target.suffix}"
                reserved.add(candidate.casefold())
                final_target = target.with_name(candidate)
                final_names[source] = final_target
                collision_notes.append(f"{source.relative_to(root)} -> {final_target.relative_to(root)} (name collision)")
        for source, target in pairs:
            final_target = final_names[source]
            if final_target != source:
                plan.append((source, final_target))
    return plan, collision_notes


def apply_plan(root: Path, plan: list[tuple[Path, Path]]) -> None:
    basename_map: dict[str, set[str]] = defaultdict(set)
    for source, target in plan:
        basename_map[source.name.casefold()].add(target.name)

    # Move through unique temporary names so cycles and case-only renames are safe.
    staged = []
    for index, (source, target) in enumerate(plan):
        temp = source.with_name(f".__image_rename_{index:05d}__.tmp")
        source.rename(temp)
        staged.append((temp, source, target))
    for temp, source, target in staged:
        temp.rename(target)

    replacements = {old: next(iter(new_names)) for old, new_names in basename_map.items() if len(new_names) == 1}
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_EXTENSIONS or ".git" in path.parts:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            continue
        updated = text
        for old, new in sorted(replacements.items(), key=lambda pair: -len(pair[0])):
            if old != new.casefold():
                updated = re.sub(re.escape(old), lambda _match, value=new: value, updated, flags=re.IGNORECASE)
        if updated != text:
            path.write_text(updated, encoding="utf-8", newline="")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--apply", action="store_true", help="rename image files and update text references")
    args = parser.parse_args()
    root = args.root.resolve()
    plan, collisions = build_plan(root)
    print(f"Images to rename: {len(plan)}")
    for source, target in plan[:120]:
        print(f"{source.relative_to(root).as_posix()} -> {target.relative_to(root).as_posix()}")
    if len(plan) > 120:
        print(f"... and {len(plan) - 120} more")
    print(f"Resolved name collisions: {len(collisions)}")
    for note in collisions[:30]:
        print(note)
    if args.apply:
        apply_plan(root, plan)
        print("Image filenames and unambiguous text references updated.")
    else:
        print("Dry run only. Re-run with --apply to perform the renames.")


if __name__ == "__main__":
    main()
