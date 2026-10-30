"""
Pest Recognition & Agricultural Entomology Extension Module.
Describes the architectural requirements, pest profiles, diagnostic rule-engine,
and technical roadmap for extending the system from leaf disease classification
to real-time insect-pest recognition.
"""

# Common Agricultural Pests impacting Apple, Corn, Grape, Potato, and Tomato
PEST_PROFILES = [
    {
        "name": "Fall Armyworm",
        "scientific_name": "Spodoptera frugiperda",
        "target_crops": ["Corn (Maize)", "Tomato"],
        "stage": "Larval (Caterpillar)",
        "damage_type": "Defoliation & Ear/Whorl Destruction",
        "visual_signature": [
            "Inverted 'Y' suture on dark head capsule.",
            "Four dark spots forming a square on the 8th abdominal segment.",
            "Extensive ragged 'windowpane' leaf damage and coarse sawdust-like frass."
        ],
        "economic_threshold": "Apply control when 10-20% of whorl-stage corn plants show fresh windowpane feeding and live larvae.",
        "ipm_management": [
            "Biological: Release egg parasitoids (Trichogramma pretiosum) and Telenomus remus.",
            "Microbial: Spray Bacillus thuringiensis (Bt subsp. kurstaki) or Spodoptera frugiperda multiple nucleopolyhedrovirus (SfMNPV).",
            "Botanical: Cold-pressed neem oil applied into the whorl in early evening.",
            "Chemical: Chlorantraniliprole, Spinetoram, or Emamectin benzoate."
        ]
    },
    {
        "name": "Two-Spotted Spider Mite",
        "scientific_name": "Tetranychus urticae",
        "target_crops": ["Tomato", "Grape", "Apple"],
        "stage": "Adult & Nymph (Acarid)",
        "damage_type": "Cell-content feeding, leaf stippling & webbing",
        "visual_signature": [
            "Yellow/white speckling (stippling) on upper leaf surface.",
            "Extensive fine silk webbing on leaf undersides and shoot tips.",
            "Tiny oval bodies (0.4 mm) with two dark lateral spots."
        ],
        "economic_threshold": "1-2 mites per leaflet in early season; presence of active colonies with eggs.",
        "ipm_management": [
            "Biological: Introduce predatory mites (Phytoseiulus persimilis, Neoseiulus californicus).",
            "Cultural: Overhead misting to maintain canopy humidity; suppress road dust.",
            "Organic: Horticultural mineral oils and insecticidal potassium soaps.",
            "Chemical: Bifenazate, Spiromesifen, Abamectin."
        ]
    },
    {
        "name": "Tomato Hornworm",
        "scientific_name": "Manduca quinquemaculata",
        "target_crops": ["Tomato", "Potato"],
        "stage": "Larval (Giant Caterpillar)",
        "damage_type": "Severe canopy defoliation & chewed fruit",
        "visual_signature": [
            "Large green caterpillar (up to 10 cm) with white 'V'-shaped markings.",
            "Prominent black/blue horn protruding from posterior abdomen.",
            "Stripped bare stems with large, dark hexagonal droppings below."
        ],
        "economic_threshold": "1 larva per 10-15 tomato plants justifies hand-picking or biological spray.",
        "ipm_management": [
            "Biological: Protect larvae parasitized by Cotesia congregata wasps (white cocoons on body).",
            "Microbial: Foliar spray of Bacillus thuringiensis (Bt).",
            "Cultural: Deep fall tillage to destroy overwintering pupae in soil.",
            "Manual: Hand-picking under blacklight/UV illumination at night."
        ]
    },
    {
        "name": "Colorado Potato Beetle",
        "scientific_name": "Leptinotarsa decemlineata",
        "target_crops": ["Potato", "Tomato"],
        "stage": "Larva & Adult Beetle",
        "damage_type": "Voracious foliage defoliation",
        "visual_signature": [
            "Adults have rounded yellow-orange bodies with 10 distinctive black stripes.",
            "Larvae are plump, humpbacked, reddish-orange with two rows of black dots along sides.",
            "Clusters of bright yellow/orange football-shaped eggs glued beneath leaves."
        ],
        "economic_threshold": "Defoliation exceeding 10% during tuber initiation or 1 adult/larva per potato plant.",
        "ipm_management": [
            "Cultural: Crop rotation at least 0.5 km away from previous potato fields; plastic-lined trenches.",
            "Biological: Spined soldier bug (Podisus maculiventris) and Beauveria bassiana.",
            "Chemical: Spinosad, Chlorantraniliprole, or Novaluron (rotate strictly to delay resistance)."
        ]
    },
    {
        "name": "Sweetpotato Whitefly",
        "scientific_name": "Bemisia tabaci",
        "target_crops": ["Tomato", "Potato"],
        "stage": "Adult & Nymph (Hemiptera)",
        "damage_type": "Sap-feeding, vector for TYLCV, sticky honeydew & sooty mold",
        "visual_signature": [
            "Tiny white-winged moth-like insects (1 mm) fluttering off leaves when disturbed.",
            "Scale-like translucent flat nymphs adhering to lower leaf surfaces.",
            "Sticky honeydew secretions coating leaves followed by black sooty mold fungus."
        ],
        "economic_threshold": "Zero-tolerance in seedbeds; >5 adults per yellow sticky trap per week in greenhouse.",
        "ipm_management": [
            "Physical: 50-mesh insect netting in greenhouses; reflective silver plastic ground mulch.",
            "Biological: Parasitoid wasps (Encarsia formosa), green lacewing larvae.",
            "Botanical: Azadirachtin (neem extract) and Beauveria bassiana sprays.",
            "Chemical: Spirotetramat, Dinotefuran, Flupyradifurone."
        ]
    },
    {
        "name": "Grape Berry Moth",
        "scientific_name": "Paralobesia viteana",
        "target_crops": ["Grape"],
        "stage": "Larva",
        "damage_type": "Fruit cluster webbing & berry tunnel entry",
        "visual_signature": [
            "Silken webbing binding together flower buds or green berries.",
            "Small purple/red puncture spots on green berries with entry holes.",
            "Small greenish caterpillars (8-10 mm) feeding within berry pulp."
        ],
        "economic_threshold": "5% berry cluster infestation at veraison stage.",
        "ipm_management": [
            "Pheromone Disruption: Install female sex pheromone dispensers (Isomate-GBM) to prevent mating.",
            "Biological: Trichogramma minutum egg parasitoids.",
            "Microbial: Bt sprays applied within 2-3 days of egg hatch.",
            "Chemical: Methoxyfenozide (Intrepid) or Chlorantraniliprole."
        ]
    },
    {
        "name": "Apple Codling Moth",
        "scientific_name": "Cydia pomonella",
        "target_crops": ["Apple"],
        "stage": "Larva (Caterpillar)",
        "damage_type": "Fruit tunneling & core entry ('wormy apple')",
        "visual_signature": [
            "Brown frass extruded from entry hole at calyx end or side of fruit.",
            "Whitish/pink caterpillar with brown head feeding inside fruit seed core.",
            "Premature apple ripening and fruit drop."
        ],
        "economic_threshold": "1 moth per pheromone trap per week during biofix period.",
        "ipm_management": [
            "Pheromone: Mating disruption dispensers across minimum 5-acre contiguous blocks.",
            "Biological: Codling moth granulovirus (CpGV) sprays targeted at neonate larvae.",
            "Physical: Bagging individual fruit clusters in small orchards.",
            "Chemical: Spinetoram, Acetamiprid, or Rynaxypyr."
        ]
    }
]

# Pest Diagnostic Rule Engine
def diagnose_pest(crop: str, damage_symptom: str, insect_appearance: str) -> list[dict]:
    """
    Expert rule-engine matching farmer observations to potential insect pests.
    Acts as an interactive decision aid before machine vision integration.
    """
    matches = []
    
    for pest in PEST_PROFILES:
        score = 0
        reasons = []
        
        # Check Crop match
        if crop == "All" or any(crop.lower() in tc.lower() for tc in pest["target_crops"]):
            score += 40
            reasons.append(f"Known pest of {crop}")
            
        # Check Damage match
        dmg_lower = damage_symptom.lower()
        pest_dmg_lower = pest["damage_type"].lower()
        if any(term in pest_dmg_lower for term in dmg_lower.split()):
            score += 35
            reasons.append(f"Matches observed injury pattern: {pest['damage_type']}")
            
        # Check Visual appearance match
        vis_lower = insect_appearance.lower()
        pest_vis = " ".join(pest["visual_signature"]).lower()
        if any(term in pest_vis for term in vis_lower.split() if len(term) > 3):
            score += 25
            reasons.append("Matches physical insect morphology")
            
        if score >= 40:
            matches.append({
                "pest": pest,
                "confidence_score": min(score, 95),
                "match_reasons": reasons
            })
            
    # Sort descending by match score
    matches.sort(key=lambda x: x["confidence_score"], reverse=True)
    return matches
