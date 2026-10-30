"""
Agricultural Knowledge Base: Crop Disease Details, Symptoms, and Management Guidance.
Comprehensive agronomic suggestions aligned with Integrated Pest and Disease Management (IPM).
"""

DISEASE_INFO = {
    # ------------------ APPLE ------------------
    "Apple___Apple_scab": {
        "crop": "Apple",
        "common_name": "Apple Scab",
        "pathogen": "Venturia inaequalis (Ascomycete fungus)",
        "category": "Fungal",
        "severity": "Moderate to High",
        "symptoms": [
            "Olive-green to velvety dark brown spots on leaf upper surfaces.",
            "Lesions become raised, corky, and puckered as leaf tissue ages.",
            "Infected leaves turn chlorotic, curl upward, and drop prematurely.",
            "Can spread to fruit causing dark scab lesions and deformities."
        ],
        "favorable_conditions": "Cool (15-24°C), wet, and humid spring weather with prolonged leaf wetness (6+ hours).",
        "cultural_practices": [
            "Rake, destroy, or compost fallen overwintering leaves in autumn.",
            "Prune canopy during dormancy to promote sunlight penetration and rapid air drying.",
            "Avoid overhead irrigation; use drip or soaker hose systems."
        ],
        "biological_controls": [
            "Apply Bacillus subtilis (e.g., Serenade) early in the growing season.",
            "Sulfur or potassium bicarbonate sprays during early bud break before rain events."
        ],
        "chemical_treatments": [
            "Protectant fungicides: Captan, Mancozeb (FRAC M04, M03).",
            "Systemic fungicides (curative within 24-48 hrs of rain): Difenoconazole, Myclobutanil (FRAC 3).",
            "Rotate chemical groups annually to prevent pathogen resistance."
        ],
        "urgent_action": "Apply protectant fungicide immediately before next predicted rain event and inspect orchard floor."
    },

    "Apple___Black_rot": {
        "crop": "Apple",
        "common_name": "Black Rot (Frog-Eye Leaf Spot)",
        "pathogen": "Botryosphaeria obtusa (Fungus)",
        "category": "Fungal",
        "severity": "High",
        "symptoms": [
            "Small purple spots on leaves expanding to 4-5 mm with tan centers and dark purple margins (frog-eye appearance).",
            "Black rot cankers on dead bark and branches.",
            "Firm brown rotted fruit with concentric dark rings."
        ],
        "favorable_conditions": "Warm (20-27°C) and rainy weather during post-bloom periods; wounded tree bark.",
        "cultural_practices": [
            "Prune out dead wood, fire blight cankers, and mummified fruit from trees and orchard floor.",
            "Sterilize pruning tools in 70% isopropyl alcohol between cuts.",
            "Maintain overall tree vigor with balanced nitrogen fertilization."
        ],
        "biological_controls": [
            "Biofungicide sprays (Trichoderma harzianum) to colonize pruning wounds.",
            "Liquid copper octanoate during dormant season."
        ],
        "chemical_treatments": [
            "Captan, Thiophanate-methyl, or Strobilurins (e.g., Pyraclostrobin, FRAC 11).",
            "Apply from petal fall through mid-summer cover sprays."
        ],
        "urgent_action": "Prune out diseased twigs at least 15 cm below visible cankers and remove all mummified apples."
    },

    "Apple___Cedar_apple_rust": {
        "crop": "Apple",
        "common_name": "Cedar Apple Rust",
        "pathogen": "Gymnosporangium juniperi-virginianae (Heteroecious rust fungus)",
        "category": "Fungal",
        "severity": "Moderate",
        "symptoms": [
            "Bright yellow-orange or reddish spots on upper leaf surfaces in late spring.",
            "Clusters of tiny brown dots (pycnia) inside the orange spots.",
            "Spiky fungal tubular structures (aecia) on the underside of infected leaves.",
            "Severe infections cause early leaf drop and small fruit."
        ],
        "favorable_conditions": "Presence of alternate host (Eastern Red Cedar / Juniper) within 1-2 miles; wet spring spells (10-24°C).",
        "cultural_practices": [
            "Remove eastern red cedars or ornamental junipers within 500-1000 feet of orchard.",
            "Plant rust-resistant apple varieties (e.g., Liberty, Freedom, Enterprise, Redfree).",
            "Inspect nearby junipers for brown woody galls and prune them before spring rains."
        ],
        "biological_controls": [
            "Sulfur sprays applied from tight cluster through petal fall.",
            "Bio-rational neem oil and potassium bicarbonate."
        ],
        "chemical_treatments": [
            "Myclobutanil (Immunox), Propiconazole, or Mancozeb.",
            "Apply beginning at pink bud stage until 1-2 weeks past petal fall."
        ],
        "urgent_action": "Check nearby cedar/juniper trees for gelatinous spore horns; apply myclobutanil if apples are in active shoot growth."
    },

    "Apple___healthy": {
        "crop": "Apple",
        "common_name": "Healthy Apple Foliage",
        "pathogen": "None (Healthy tissue)",
        "category": "Healthy",
        "severity": "Optimal",
        "symptoms": [
            "Deep green, glossy leaf surface without spots, curling, or lesions.",
            "Uniform vein architecture and healthy cellular turgidity.",
            "No signs of chlorosis, necrosis, or pest grazing."
        ],
        "favorable_conditions": "Adequate sunlight, well-draining loamy soil (pH 6.0-6.8), balanced N-P-K nutrition.",
        "cultural_practices": [
            "Maintain regular orchard monitoring schedule.",
            "Ensure proper soil moisture with drip irrigation.",
            "Apply balanced compost or slow-release fertilizer according to soil test results."
        ],
        "biological_controls": [
            "Encourage beneficial predators (lacewings, ladybugs, predatory mites).",
            "Maintain pollinator-friendly cover crops in alleyways."
        ],
        "chemical_treatments": [
            "No chemical intervention needed.",
            "Maintain standard preventative dormant oil spray during late winter."
        ],
        "urgent_action": "Keep up routine scouting and standard seasonal orchard maintenance."
    },

    # ------------------ CORN (MAIZE) ------------------
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "crop": "Corn (Maize)",
        "common_name": "Gray Leaf Spot (Cercospora)",
        "pathogen": "Cercospora zeae-maydis (Fungus)",
        "category": "Fungal",
        "severity": "High",
        "symptoms": [
            "Small, tan spots with yellow halos expanding into long, rectangular lesions.",
            "Lesions strictly bordered by parallel leaf veins (distinct blocky shape).",
            "Under humid weather, lesions take on a grayish cast from fungal sporulation.",
            "Extensive leaf blighting leads to stalk lodging and reduced grain fill."
        ],
        "favorable_conditions": "High relative humidity (>90%) and warm temperatures (24-30°C); conservation tillage retaining corn residue.",
        "cultural_practices": [
            "Rotate crops with non-grasses (soybean, alfalfa, pulses) for 1-2 years.",
            "Incorporate corn residue into soil through deep tillage to accelerate decomposition.",
            "Select corn hybrids with high GLS resistance ratings."
        ],
        "biological_controls": [
            "Seed treatments with beneficial microbes (Bacillus amyloliquefaciens).",
            "Soil health amendments promoting rapid residue breakdown."
        ],
        "chemical_treatments": [
            "Foliar fungicides: Strobilurins (Azoxystrobin, Pyraclostrobin) + Triazoles (Propiconazole).",
            "Optimal application timing is between VT (tasseling) and R2 (blister stage)."
        ],
        "urgent_action": "Scout the ear leaf and three leaves below; if lesions are visible on >50% of plants at tasseling, spray immediately."
    },

    "Corn_(maize)___Common_rust_": {
        "crop": "Corn (Maize)",
        "common_name": "Common Rust",
        "pathogen": "Puccinia sorghi (Basidiomycete fungus)",
        "category": "Fungal",
        "severity": "Moderate",
        "symptoms": [
            "Golden-brown to cinnamon-red powdery pustules (uredinia) on upper and lower leaf surfaces.",
            "Pustules rupture the leaf epidermis, releasing powdery rust spores.",
            "In late season, pustules turn black as overwintering teliospores develop.",
            "Severe rust can lead to leaf chlorosis and premature senescence."
        ],
        "favorable_conditions": "Cooler to moderate temperatures (16-25°C) with high humidity (>95%) and night dew.",
        "cultural_practices": [
            "Plant rust-resistant hybrids containing Rp resistance genes.",
            "Early planting can allow crop to mature before airborne spores arrive from warmer southern regions."
        ],
        "biological_controls": [
            "Trichoderma-based biocontrol foliar applications.",
            "Plant extracts (garlic/neem) as preventative rust inhibitors."
        ],
        "chemical_treatments": [
            "Triazole fungicides (Propiconazole, Tebuconazole) or QoI strobilurins.",
            "Economic threshold: Apply if pustules appear on upper leaves prior to brown silk stage in susceptible hybrids."
        ],
        "urgent_action": "Evaluate crop growth stage: if corn is past blister stage, chemical treatment is usually not economically justified."
    },

    "Corn_(maize)___Northern_Leaf_Blight": {
        "crop": "Corn (Maize)",
        "common_name": "Northern Corn Leaf Blight (NCLB)",
        "pathogen": "Exserohilum turcicum (Fungus)",
        "category": "Fungal",
        "severity": "Critical",
        "symptoms": [
            "Large, elliptical or 'cigar-shaped' grayish-green to tan lesions (2.5 to 15 cm long).",
            "Lesions cross leaf veins freely, unlike Gray Leaf Spot.",
            "Dark sporulation appears on lesions during damp mornings.",
            "Lower canopy infected first, rapidly advancing to upper canopy."
        ],
        "favorable_conditions": "Moderate temperatures (18-27°C) with persistent wetness and heavy dew periods (6-18 hours).",
        "cultural_practices": [
            "Rotate out of corn for at least one full season.",
            "Plow down infected residue to bury spores.",
            "Select resistant hybrids with Ht genes."
        ],
        "biological_controls": [
            "Streptomyces-based biofungicides.",
            "Compost tea sprays to boost phyllosphere microbial competition."
        ],
        "chemical_treatments": [
            "Combination premixes: Triazole + Strobilurin (e.g., Pyraclostrobin + Fluxapyroxad).",
            "Apply between V12 and R1 if lesions are present on leaves below the ear leaf."
        ],
        "urgent_action": "Inspect ear leaves immediately; apply targeted dual-action fungicide if 50% of plants show lesions before silking."
    },

    "Corn_(maize)___healthy": {
        "crop": "Corn (Maize)",
        "common_name": "Healthy Corn Foliage",
        "pathogen": "None (Healthy tissue)",
        "category": "Healthy",
        "severity": "Optimal",
        "symptoms": [
            "Vibrant green, sturdy leaf blades with crisp distinct venation.",
            "No pustules, elongated lesions, or yellow borders.",
            "Strong stalk development and normal canopy photosynthesis."
        ],
        "favorable_conditions": "Adequate soil nitrogen, full sunlight, balanced watering during vegetative and reproductive stages.",
        "cultural_practices": [
            "Side-dress nitrogen according to crop stage (V4-V8).",
            "Maintain weed-free zone around young corn to prevent resource competition.",
            "Regular scouting for cutworms and stalk borers."
        ],
        "biological_controls": [
            "Conserve beneficial predators (ground beetles, minute pirate bugs).",
            "Use mycorrhizal inoculants at planting to enhance root nutrient uptake."
        ],
        "chemical_treatments": [
            "None required.",
            "Scout regularly during tasseling stage for incoming rust or leaf spot."
        ],
        "urgent_action": "Maintain soil moisture during silking and grain fill stages."
    },

    # ------------------ GRAPE ------------------
    "Grape___Black_rot": {
        "crop": "Grape",
        "common_name": "Grape Black Rot",
        "pathogen": "Guignardia bidwellii (Fungus)",
        "category": "Fungal",
        "severity": "High to Critical",
        "symptoms": [
            "Small circular reddish-brown leaf lesions surrounded by narrow dark brown margins.",
            "Tiny black pimple-like fruiting bodies (pycnidia) arranged in rings inside spots.",
            "Berries develop light brown spots, shrivel rapidly into hard, wrinkled black 'mummies'.",
            "Can destroy up to 80% of crop in untreated humid vineyards."
        ],
        "favorable_conditions": "Warm (21-32°C) and rainy weather; continuous leaf wetness for 7-10 hours.",
        "cultural_practices": [
            "Collect and destroy all shriveled grape mummies from trellis and vineyard floor.",
            "Canopy management: shoot thinning and leaf pulling around fruit zones to maximize air flow.",
            "Ensure proper drainage and eliminate wild grapevines nearby."
        ],
        "biological_controls": [
            "Copper hydroxide or liquid lime sulfur applications in early spring.",
            "Biofungicide: Bacillus amyloliquefaciens strain D747."
        ],
        "chemical_treatments": [
            "Mancozeb, Captan, or Ziram as early protectants from 1-inch shoot growth.",
            "Myclobutanil or Tebuconazole from immediate pre-bloom to 4 weeks post-bloom."
        ],
        "urgent_action": "Prune out infected shoots, remove all mummies, and spray DMI fungicide before next rainfall."
    },

    "Grape___Esca_(Black_Measles)": {
        "crop": "Grape",
        "common_name": "Esca (Black Measles / Trunk Disease)",
        "pathogen": "Complex of Phaeomoniella chlamydospora, Phaeoacremonium minimum, and Fomitiporia mediterranea",
        "category": "Fungal",
        "severity": "Critical",
        "symptoms": [
            "Striking 'tiger-stripe' leaf pattern: yellow or red chlorotic patches between green veins followed by necrosis.",
            "Small dark spots or measles on berries; fruit cracking or drying on vine.",
            "Cross-section of vine trunk shows black spotting and vascular necrosis.",
            "Sudden vine collapse (apoplexy) during hot dry summer periods."
        ],
        "favorable_conditions": "Mature vines (usually >7-10 years old); entry via pruning wounds during wet winter periods.",
        "cultural_practices": [
            "Prune late in the dormant season (February/March) when wounds heal faster.",
            "Treat all pruning wounds larger than 1.5 cm with wound protectant sealants.",
            "Mark symptomatic vines in summer for separate pruning or trunk renewal."
        ],
        "biological_controls": [
            "Apply Trichoderma-based formulations to pruning cuts within 24-48 hours.",
            "Avoid excessive water stress in summer to delay sudden apoplexy."
        ],
        "chemical_treatments": [
            "No chemical cure exists for infected vine vascular tissue.",
            "Foliar nutrient sprays (calcium, magnesium) can reduce visual leaf stress."
        ],
        "urgent_action": "Sanitize pruning tools; cut infected trunk down to healthy white wood or plan vine replacement."
    },

    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "crop": "Grape",
        "common_name": "Grape Leaf Blight (Isariopsis)",
        "pathogen": "Pseudocercospora cladosporioides (Isariopsis clavispora)",
        "category": "Fungal",
        "severity": "Moderate",
        "symptoms": [
            "Irregular, circular to angular dark reddish-brown lesions on leaves.",
            "Lesions develop grayish-brown velvety coating of fungal conidiophores on leaf undersides.",
            "Infected leaves turn yellow, become necrotic, and drop prematurely in late summer.",
            "Weakens vine reserves, reducing cold hardiness and following year's crop."
        ],
        "favorable_conditions": "Late summer warm and humid conditions; dense canopies with poor ventilation.",
        "cultural_practices": [
            "Leaf removal in the fruit zone to improve airflow and dry leaf surfaces.",
            "Proper vine spacing and shoot positioning on vertical trellis systems.",
            "Rake and compost fallen leaves after harvest."
        ],
        "biological_controls": [
            "Copper oxychloride and copper hydroxide sprays.",
            "Neem-based botanical fungicides."
        ],
        "chemical_treatments": [
            "Strobilurin fungicides (Kresoxim-methyl, Pyraclostrobin).",
            "Mancozeb or chlorothalonil applied during late summer post-bloom sprays."
        ],
        "urgent_action": "Open up canopy by removing senescing lower leaves; apply copper fungicide if defoliation begins."
    },

    "Grape___healthy": {
        "crop": "Grape",
        "common_name": "Healthy Grape Foliage",
        "pathogen": "None (Healthy tissue)",
        "category": "Healthy",
        "severity": "Optimal",
        "symptoms": [
            "Broad palmate leaves with vivid green color and supple texture.",
            "Intact leaf margins without scorch, spots, or interveinal tiger striping.",
            "Active vine shoot elongation and healthy tendril production."
        ],
        "favorable_conditions": "Well-drained gravelly or sandy loam soil, full sunlight (7+ hours/day), balanced drip irrigation.",
        "cultural_practices": [
            "Perform balanced dormant pruning to maintain vine architecture.",
            "Manage vineyard cover crops to regulate vine vigor and soil moisture.",
            "Apply balanced micronutrients (zinc, boron, magnesium) based on petiole tests."
        ],
        "biological_controls": [
            "Encourage predatory mites (Typhlodromus pyri) for spider mite control.",
            "Maintain wildflower strips to support parasitoid wasps."
        ],
        "chemical_treatments": [
            "No active fungicides needed.",
            "Follow standard preventative sulfur dusting program for powdery mildew prevention."
        ],
        "urgent_action": "Continue routine canopy management and petiole nutrient monitoring."
    },

    # ------------------ POTATO ------------------
    "Potato___Early_blight": {
        "crop": "Potato",
        "common_name": "Potato Early Blight",
        "pathogen": "Alternaria solani (Fungus)",
        "category": "Fungal",
        "severity": "Moderate to High",
        "symptoms": [
            "Dark brown to black spots with distinct concentric rings creating a 'target board' pattern.",
            "Lesions start on older lower leaves, often surrounded by yellow chlorotic halos.",
            "Leaves turn brittle, brown, and dry up while remaining attached to stem.",
            "Can cause sunken, dark, leathery dry rot lesions on tubers."
        ],
        "favorable_conditions": "Warm temperatures (24-29°C) with alternating wet periods (rain or dew) and dry sunny periods.",
        "cultural_practices": [
            "Implement a 3-4 year crop rotation with non-solanaceous crops.",
            "Ensure balanced fertilization; nitrogen deficiency severely accelerates early blight susceptibility.",
            "Use certified disease-free seed tubers.",
            "Irrigate early in the morning so foliage dries quickly before nightfall."
        ],
        "biological_controls": [
            "Foliar sprays of Bacillus subtilis or Trichoderma viride.",
            "Copper soaps or fixed copper fungicides."
        ],
        "chemical_treatments": [
            "Protectants: Chlorothalonil, Mancozeb (FRAC M05, M03).",
            "Targeted translaminar fungicides: Boscalid (FRAC 7), Difenoconazole (FRAC 3), or Fluopyram."
        ],
        "urgent_action": "Top-dress with nitrogen if crop is deficient; apply chlorothalonil to protect middle and upper canopy."
    },

    "Potato___Late_blight": {
        "crop": "Potato",
        "common_name": "Potato Late Blight",
        "pathogen": "Phytophthora infestans (Oomycete / Water mold)",
        "category": "Oomycete",
        "severity": "Critical (Emergency)",
        "symptoms": [
            "Irregular water-soaked pale-to-dark green lesions that rapidly turn brown or black.",
            "Lesions expand rapidly across leaves and stems in wet weather.",
            "Delicate white fuzzy fungal-like growth (sporangia) on the underside of infected leaves in high humidity.",
            "Foul decaying odor in heavily infested potato fields; tubers suffer granular reddish-brown rot."
        ],
        "favorable_conditions": "Cool to moderate temperatures (12-21°C) with continuous high humidity (>90%) and rain.",
        "cultural_practices": [
            "Plant only certified disease-free seed tubers.",
            "Destroy all volunteer potato plants and cull piles before planting season.",
            "Hill up soil around potato hills deeply to prevent sporangia from washing down into tubers.",
            "Kill potato vines 2-3 weeks before harvest to prevent tuber contamination at digging."
        ],
        "biological_controls": [
            "Bordeaux mixture or copper sulfate (preventative, organic approved).",
            "Streptomyces lydicus foliar biofungicide."
        ],
        "chemical_treatments": [
            "Systemic oomycides: Metalaxyl / Mefenoxam (FRAC 4), Mandipropamid (FRAC 40), or Fluopicolide (FRAC 43).",
            "Spray protectant fungicides (Mancozeb, Chlorothalonil) on a strict 5-7 day schedule during blight-favorable weather."
        ],
        "urgent_action": "🚨 CRITICAL: Immediately rogue and bag severely infected plants; spray systemic oomycide across the field within 24 hours."
    },

    "Potato___healthy": {
        "crop": "Potato",
        "common_name": "Healthy Potato Foliage",
        "pathogen": "None (Healthy tissue)",
        "category": "Healthy",
        "severity": "Optimal",
        "symptoms": [
            "Dark green compound leaves with crisp leaflets and robust petioles.",
            "No water-soaked lesions, target spots, or chlorotic mottling.",
            "Stout upright stems supporting vigorous vegetative and tuber initiation."
        ],
        "favorable_conditions": "Cool temperate climate (15-22°C), loose friable soil (pH 5.0-6.0), consistent hilling.",
        "cultural_practices": [
            "Maintain consistent soil moisture to prevent tuber growth cracks and scab.",
            "Scout weekly for Colorado potato beetle egg clusters on leaf undersides.",
            "Hill potatoes when plants reach 15-20 cm in height."
        ],
        "biological_controls": [
            "Beneficial nematodes (Steinernema carpocapsae) for soil grubs.",
            "Companion planting with bush beans to deter pests."
        ],
        "chemical_treatments": [
            "None required.",
            "Keep preventative fungicides ready if rainy, cool weather is forecasted."
        ],
        "urgent_action": "Maintain routine scouting and check local Late Blight warning alerts."
    },

    # ------------------ TOMATO ------------------
    "Tomato___Bacterial_spot": {
        "crop": "Tomato",
        "common_name": "Bacterial Spot",
        "pathogen": "Xanthomonas campestris pv. vesicatoria (Bacterium)",
        "category": "Bacterial",
        "severity": "High",
        "symptoms": [
            "Small (2-3 mm) dark brown to black water-soaked circular spots on leaves.",
            "Spots develop a translucent yellow halo; centers may drop out giving a shot-hole appearance.",
            "Severe infection causes general leaf yellowing and blighting.",
            "Fruit exhibits raised, scab-like, dark scabby specks."
        ],
        "favorable_conditions": "Warm temperatures (24-30°C) with driving rain, wind, and overhead sprinkler irrigation.",
        "cultural_practices": [
            "Use certified disease-free and hot-water treated tomato seeds.",
            "Never work in tomato fields when plants are wet with dew or rain.",
            "Clean and disinfect stakes, cages, and machinery with 10% bleach.",
            "Rotate out of solanaceous crops for a minimum of 2 years."
        ],
        "biological_controls": [
            "Bacteriophage sprays (e.g., AgriPhage) targeting specific Xanthomonas strains.",
            "Bacillus amyloliquefaciens foliar treatments."
        ],
        "chemical_treatments": [
            "Copper bactericides mixed with Mancozeb (improves copper solubility and bacterial kill).",
            "Actigard (Acibenzolar-S-methyl) to activate plant systemic acquired resistance (SAR)."
        ],
        "urgent_action": "Avoid overhead watering; spray copper-mancozeb tank mix; sanitize hands and pruning shears."
    },

    "Tomato___Early_blight": {
        "crop": "Tomato",
        "common_name": "Early Blight",
        "pathogen": "Alternaria linariae / Alternaria solani (Fungus)",
        "category": "Fungal",
        "severity": "Moderate to High",
        "symptoms": [
            "Small brown spots with distinct concentric rings (target pattern) on older lower leaves.",
            "Surrounding tissue turns bright yellow (chlorotic halo).",
            "Progresses upwards from the soil level; stems develop dark sunken collar-rot lesions.",
            "Severe defoliation exposes green tomatoes to solar sunscald."
        ],
        "favorable_conditions": "Warm temperatures (24-29°C) and alternating humid/rainy and dry conditions.",
        "cultural_practices": [
            "Prune off lower 30 cm of leaves (bottom pruning) to prevent soil splash.",
            "Apply 5-8 cm of organic straw or plastic mulch around plant bases.",
            "Stake or cage plants to keep foliage off the ground.",
            "Maintain 3-year solanaceous crop rotation."
        ],
        "biological_controls": [
            "Biofungicides: Trichoderma harzianum or Bacillus subtilis.",
            "Potassium silicate sprays to strengthen leaf cuticle resistance."
        ],
        "chemical_treatments": [
            "Chlorothalonil, Mancozeb, or Copper hydroxide as preventative protectants.",
            "Difenoconazole, Azoxystrobin, or Penthiopyrad for active control."
        ],
        "urgent_action": "Prune out and bag infected lower leaves immediately; apply straw mulch under plants."
    },

    "Tomato___Late_blight": {
        "crop": "Tomato",
        "common_name": "Late Blight",
        "pathogen": "Phytophthora infestans (Oomycete)",
        "category": "Oomycete",
        "severity": "Critical (Emergency)",
        "symptoms": [
            "Large, dark, water-soaked, greasy greenish-brown to black lesions.",
            "Lesions expand rapidly across leaves, petioles, and main stems.",
            "White frost-like fungal mold appears on leaf undersides in morning humidity.",
            "Green and ripe tomatoes turn brown with firm, greasy, bumpy rot.",
            "An entire tomato plot can be destroyed within 5 to 7 days."
        ],
        "favorable_conditions": "Cool to moderate temperatures (15-22°C) combined with prolonged high relative humidity (>90%) and rain.",
        "cultural_practices": [
            "Destroy all volunteer tomatoes and potatoes in early spring.",
            "Ensure wide plant spacing (at least 60-90 cm) for rapid leaf drying.",
            "Do not compost infected plants; double-bag and discard in household trash."
        ],
        "biological_controls": [
            "Fixed copper fungicides applied proactively before wet periods.",
            "Resistant varieties: Mountain Magic, Defiant, Plum Regal, Iron Lady."
        ],
        "chemical_treatments": [
            "Systemic fungicides: Mandipropamid (Revus), Cyazofamid (Ranman), or Fluopicolide (Presidio).",
            "Must be applied preventatively or at the earliest sign of disease."
        ],
        "urgent_action": "🚨 CRITICAL: Immediately remove and dispose of infected plants; notify neighboring growers; apply systemic oomycide."
    },

    "Tomato___Leaf_Mold": {
        "crop": "Tomato",
        "common_name": "Tomato Leaf Mold",
        "pathogen": "Passalora fulva (Cladosporium fulvum, Fungus)",
        "category": "Fungal",
        "severity": "Moderate",
        "symptoms": [
            "Pale green to yellowish diffuse spots on the upper leaf surface.",
            "Olive-green to purplish-brown velvety fungal mold on the lower leaf surface directly under the yellow spots.",
            "Leaves curl, wilt, turn brown, and drop prematurely.",
            "Primarily a high-tunnel and greenhouse problem due to limited airflow."
        ],
        "favorable_conditions": "High humidity (>85%) and warm temperatures (21-24°C); common in poorly ventilated greenhouses.",
        "cultural_practices": [
            "Ventilate greenhouses and high tunnels with exhaust fans to reduce relative humidity below 80%.",
            "Increase plant spacing and prune lower suckers to maximize cross-breeze.",
            "Heat greenhouse slightly at dusk while venting to prevent dew formation on leaves."
        ],
        "biological_controls": [
            "Bacillus amyloliquefaciens foliar spray.",
            "Copper octanoate or sulfur fumigation between crop cycles."
        ],
        "chemical_treatments": [
            "Chlorothalonil, Mancozeb, or Cyazofamid.",
            "Strobilurin fungicides (e.g., Pyraclostrobin, FRAC 11)."
        ],
        "urgent_action": "Immediately open greenhouse vents and turn on circulation fans to drive down humidity below 80%."
    },

    "Tomato___Septoria_leaf_spot": {
        "crop": "Tomato",
        "common_name": "Septoria Leaf Spot",
        "pathogen": "Septoria lycopersici (Fungus)",
        "category": "Fungal",
        "severity": "High",
        "symptoms": [
            "Numerous tiny circular spots (1.5-3 mm) with grayish-white centers and distinct dark brown borders.",
            "Tiny black specks (pycnidia) clearly visible inside the center of each spot with a hand lens.",
            "Causes leaves to turn yellow and drop from bottom to top, leaving bare stems.",
            "Does not directly infect fruit, but loss of canopy severely stunts yield and causes sunscald."
        ],
        "favorable_conditions": "Warm temperatures (20-25°C) and extended rainy or wet periods with splash dispersal.",
        "cultural_practices": [
            "Strip bottom leaves up to 30 cm from the ground.",
            "Mulch heavily with clean straw, paper, or plastic film to block soil splash.",
            "Do not touch or cultivate plants when foliage is wet.",
            "Rake and burn all infected crop residue at season's end."
        ],
        "biological_controls": [
            "Copper soap fungicides applied every 7-10 days.",
            "Biofungicides containing Streptomyces or Bacillus strains."
        ],
        "chemical_treatments": [
            "Chlorothalonil (Daconil), Mancozeb, or Copper sulfate.",
            "Quadris Top (Azoxystrobin + Difenoconazole) for severe outbreaks."
        ],
        "urgent_action": "Pick off diseased lower leaflets with pycnidia; install thick straw mulch under vines."
    },

    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "crop": "Tomato",
        "common_name": "Two-Spotted Spider Mite Damage",
        "pathogen": "Tetranychus urticae (Acarid pest)",
        "category": "Pest / Mite",
        "severity": "High",
        "symptoms": [
            "Fine yellow or white stippling (pinpoint speckling) on upper leaf surfaces.",
            "Leaves take on a bronzed, dusty, or bleached appearance and become brittle.",
            "Fine, silky webbing visible on leaf undersides and terminal growing tips.",
            "Microscopic 8-legged mites (with two dark spots) visible crawling with 10x hand lens."
        ],
        "favorable_conditions": "Hot (>30°C), dry, dusty weather; water-stressed plants; overuse of broad-spectrum insecticides killing natural predators.",
        "cultural_practices": [
            "Overhead hose or misting to knock mites off foliage and reduce dust on farm roads.",
            "Avoid excessive synthetic nitrogen, which produces succulent growth favored by mites.",
            "Remove and bag heavily webbed plant clusters immediately."
        ],
        "biological_controls": [
            "Release predatory mites: Phytoseiulus persimilis or Neoseiulus californicus.",
            "Insecticidal soap, potassium salts of fatty acids, or 1% cold-pressed neem oil.",
            "Horticultural mineral oils applied thoroughly to leaf undersides."
        ],
        "chemical_treatments": [
            "Selective miticides: Bifenazate (Acramite), Abamectin, or Spiromesifen.",
            "Avoid synthetic pyrethroids which cause mite flare-ups by eliminating predatory insects."
        ],
        "urgent_action": "Mist leaf undersides with high-pressure water; apply insecticidal soap or release Phytoseiulus mites."
    },

    "Tomato___Target_Spot": {
        "crop": "Tomato",
        "common_name": "Target Spot",
        "pathogen": "Corynespora cassiicola (Fungus)",
        "category": "Fungal",
        "severity": "Moderate to High",
        "symptoms": [
            "Pinpoint brown lesions on foliage that enlarge to 5-10 mm.",
            "Lesions develop light brown to tan centers with dark concentric rings (similar to early blight).",
            "Lesions often cause surrounding leaf tissue to collapse into ragged tears.",
            "Sunken, crater-like lesions on green and mature fruit."
        ],
        "favorable_conditions": "Warm (20-28°C) temperatures with high relative humidity and prolonged leaf wetness periods.",
        "cultural_practices": [
            "Ensure wide spacing and pruning to allow foliage to dry quickly.",
            "Remove and destroy weeds in the Solanaceae family (nightshades) that host Corynespora.",
            "Avoid overhead sprinkler irrigation."
        ],
        "biological_controls": [
            "Copper formulations combined with biofungicides.",
            "Regular compost tea soil drenches to promote root defense."
        ],
        "chemical_treatments": [
            "Chlorothalonil, Azoxystrobin, Pyraclostrobin, or Famoxadone + Cymoxanil.",
            "Ensure thorough coverage of both upper and lower leaf surfaces."
        ],
        "urgent_action": "Prune out infected leaves and treat canopy with broad-spectrum protectant fungicide."
    },

    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "crop": "Tomato",
        "common_name": "Tomato Yellow Leaf Curl Virus (TYLCV)",
        "pathogen": "Begomovirus (Transmitted by Sweetpotato Whitefly, Bemisia tabaci)",
        "category": "Viral (Vector: Insect)",
        "severity": "Critical",
        "symptoms": [
            "Pronounced upward curling and cupping of leaflet margins.",
            "Severe interveinal chlorosis (yellowing) with young leaves turning pale lime-green.",
            "Marked reduction in leaf size ('shoestring' appearance) and severe plant stunting.",
            "Drastic flower drop; infected young plants fail to set marketable fruit."
        ],
        "favorable_conditions": "High whitefly populations; warm, sunny tropical or subtropical weather.",
        "cultural_practices": [
            "Plant TYLCV-resistant tomato cultivars (e.g., Tygress, Skyway, Charger).",
            "Use 50-mesh insect-proof screening in greenhouses and nurseries.",
            "Apply reflective silver plastic mulches to repel incoming whiteflies.",
            "Remove and seal infected plants in plastic bags to prevent vector dispersal."
        ],
        "biological_controls": [
            "Yellow sticky traps placed above canopy for whitefly monitoring and mass trapping.",
            "Parasitic wasps (Encarsia formosa, Eretmocerus eremicus) targeting whitefly nymphs.",
            "Beauveria bassiana entomopathogenic fungus against whiteflies."
        ],
        "chemical_treatments": [
            "No chemical cure exists for viral plant infections.",
            "Manage whitefly vectors: Spirotetramat (Movento), Dinotefuran, or Flupyradifurone.",
            "Rotate insecticidal modes of action to prevent whitefly pesticide resistance."
        ],
        "urgent_action": "Immediately rogue out symptomatic plants; spray insecticidal soap or targeted insecticide to suppress whitefly vectors."
    },

    "Tomato___Tomato_mosaic_virus": {
        "crop": "Tomato",
        "common_name": "Tomato Mosaic Virus (ToMV)",
        "pathogen": "Tobamovirus (Extremely stable mechanical & seed-borne virus)",
        "category": "Viral (Mechanical Vector)",
        "severity": "Critical",
        "symptoms": [
            "Mottling of leaves with alternating light and dark green mosaic patches.",
            "Leaf distortion, blistering, leaf narrowing ('shoestring' or 'fern leaf' appearance).",
            "Plant stunting and uneven fruit ripening with internal brown necrotic rings (browning).",
            "Can survive for years on dried plant debris, seed coats, and smoking tobacco products."
        ],
        "favorable_conditions": "Transmitted easily through worker hands, tools, grafting knives, and mechanical contact; high temperature stresses.",
        "cultural_practices": [
            "Plant certified virus-free seed and resistant hybrids (labeled with 'T' or 'ToMV').",
            "Workers must wash hands with soap and water or 20% non-fat dry milk before handling plants.",
            "Strictly prohibit smoking or handling tobacco products in or near the tomato field/greenhouse.",
            "Sanitize trellising strings, clips, and pruning shears in 10% trisodium phosphate (TSP) or 20% bleach."
        ],
        "biological_controls": [
            "Cross-protection with mild attenuated viral strains in commercial greenhouse setups.",
            "No biological cure exists once a plant is infected."
        ],
        "chemical_treatments": [
            "No chemical bactericide or fungicide can eliminate viruses from plant tissue.",
            "Focus entirely on sanitation and vector exclusion."
        ],
        "urgent_action": "Carefully dig out and burn/discard infected plants; soak pruning tools in 20% dry milk solution or 10% TSP."
    },

    "Tomato___healthy": {
        "crop": "Tomato",
        "common_name": "Healthy Tomato Foliage",
        "pathogen": "None (Healthy tissue)",
        "category": "Healthy",
        "severity": "Optimal",
        "symptoms": [
            "Lush, deep-green, serrated compound leaves with turgid petioles.",
            "No curling, necrotic target spots, powdery mildew, or viral mosaic mottling.",
            "Vigorous stem and flower truss formation indicating healthy nutrient flow."
        ],
        "favorable_conditions": "Full sun (6-8 hours daily), fertile loamy soil (pH 6.2-6.8), consistent drip moisture.",
        "cultural_practices": [
            "Maintain consistent drip irrigation to prevent blossom end rot and fruit splitting.",
            "Mulch base of plants to regulate soil temperature and suppress weeds.",
            "Prune non-productive lower suckers to channel energy into fruiting branches."
        ],
        "biological_controls": [
            "Conserve beneficial generalist predators (geocoris bugs, spiders, parasitic wasps).",
            "Plant marigolds and basil alongside tomatoes for pest deterrence."
        ],
        "chemical_treatments": [
            "No chemical pesticides needed.",
            "Continue weekly monitoring of lower leaves and pest sticky traps."
        ],
        "urgent_action": "Maintain balanced calcium-magnesium-potassium feeding schedule during fruit swell."
    }
}


def get_disease_details(class_key: str) -> dict:
    """Retrieve full agronomic info for a given PlantVillage class key."""
    if class_key in DISEASE_INFO:
        return DISEASE_INFO[class_key]
    
    # Fallback default
    return {
        "crop": "Unknown",
        "common_name": class_key.replace("___", " - ").replace("_", " "),
        "pathogen": "Under classification",
        "category": "Unspecified",
        "severity": "Moderate",
        "symptoms": ["Leaf tissue variation observed."],
        "favorable_conditions": "Standard agricultural field environment.",
        "cultural_practices": ["Inspect field and monitor symptoms."],
        "biological_controls": ["Apply standard organic preventative sprays."],
        "chemical_treatments": ["Consult local agricultural extension advisor."],
        "urgent_action": "Monitor crop and review laboratory diagnostic options."
    }
