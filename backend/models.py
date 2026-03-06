from pydantic import BaseModel

class Equipment(BaseModel):
    id: int
    type: str
    name: str
    description: str

allequipment: list[Equipment] = [
    # Cable
    Equipment(id = 1,
              type = "Cable",
              name = "Cable Crossover",
              description = "Versatile multi-plane pulling; targets chest, shoulders, arms, and core."
              ),
    Equipment(id = 2,
              type = "Cable",
              name = "Ab Crunch Machine",
              description = "Seated crunch motion; isolates and strengthens abdominal muscles."
              ),
    Equipment(id = 3,
              type = "Cable",
              name = "Lateral Raise Machine",
              description = "Raises arms sideways; isolates deltoids (especially lateral head)."
              ),
    Equipment(id = 4,
              type = "Cable",
              name = "Functional Trainer",
              description = "Dual independently adjustable cable columns; enables pulling, pushing, and rotational movements at any angle."
              ),
    Equipment(id = 5,
              type = "Cable",
              name = "Low Row Cable Station",
              description = "Seated cable row at low pulley; targets mid-back, lats, and biceps."
              ),
    Equipment(id = 6,
              type = "Cable",
              name = "Triceps Pushdown Station",
              description = "High-pulley cable with rope or bar attachment; isolates triceps through elbow extension."
              ),
    Equipment(id = 7,
              type = "Cable",
              name = "Face Pull Station",
              description = "High-pulley cable pulled toward the face; strengthens rear delts, external rotators, and upper traps."
              ),
    # Cardio
    Equipment(id = 8,
              type = "Cardio",
              name = "Treadmill",
              description = "Simulates walking, jogging, or running; targets legs, glutes, and cardiovascular system."
              ),
    Equipment(id = 9,
              type = "Cardio",
              name = "Bicycle",
              description = "Cycling motion; strengthens quads, hamstrings, glutes, calves, and core."
              ),
    Equipment(id = 10,
              type = "Cardio",
              name = "Rowing Machine",
              description = "Pulls and pushes with full-body movement; targets legs, back, shoulders, arms, and core."
              ),
    Equipment(id = 11,
              type = "Cardio",
              name = "Stair Climber",
              description = "Simulates climbing stairs; emphasizes quads, glutes, hamstrings, and calves."
              ),
    Equipment(id = 12,
              type = "Cardio",
              name = "Elliptical Trainer",
              description = "Low-impact gliding motion; works legs, glutes, and arms simultaneously while elevating heart rate."
              ),
    Equipment(id = 13,
              type = "Cardio",
              name = "Ski Erg",
              description = "Simulates cross-country skiing pull-down; targets lats, core, shoulders, and legs for full-body cardio."
              ),
    Equipment(id = 14,
              type = "Cardio",
              name = "Air Bike",
              description = "Fan-resistance bike with moving handlebars; delivers intense full-body cardio hitting legs, arms, and core."
              ),
    Equipment(id = 15,
              type = "Cardio",
              name = "Jacob's Ladder",
              description = "Self-paced inclined ladder climb; targets glutes, quads, arms, and core with minimal joint impact."
              ),
    # Free Weights
    Equipment(id = 16,
              type = "Free Weights",
              name = "Barbell",
              description = "Standard Olympic bar; used for compound lifts such as squats, deadlifts, bench press, and overhead press."
              ),
    Equipment(id = 17,
              type = "Free Weights",
              name = "Dumbbells",
              description = "Unilateral or bilateral free-weight movements; used for presses, curls, rows, lunges, and dozens of accessory exercises."
              ),
    Equipment(id = 18,
              type = "Free Weights",
              name = "EZ Curl Bar",
              description = "Angled bar that reduces wrist strain; primarily used for bicep curls and skull crushers."
              ),
    Equipment(id = 19,
              type = "Free Weights",
              name = "Kettlebell",
              description = "Offset-center-of-mass weight; ideal for swings, Turkish get-ups, goblet squats, and dynamic full-body movements."
              ),
    Equipment(id = 20,
              type = "Free Weights",
              name = "Trap Bar (Hex Bar)",
              description = "Hexagonal frame users step inside; reduces spinal load during deadlifts and shrugs, emphasizing quads and traps."
              ),
    Equipment(id = 21,
              type = "Free Weights",
              name = "Weight Plates",
              description = "Disc-shaped loads loaded onto barbells or used directly for exercises like plate pinch holds and weighted carry."
              ),
    # Functional
    Equipment(id = 22,
              type = "Functional",
              name = "Pull-Up Bar",
              description = "Fixed overhead bar; builds lats, biceps, and core through bodyweight pulling."
              ),
    Equipment(id = 23,
              type = "Functional",
              name = "Dip Bars",
              description = "Parallel bars for bodyweight dips; targets chest, triceps, and anterior deltoids."
              ),
    Equipment(id = 24,
              type = "Functional",
              name = "Battle Ropes",
              description = "Heavy anchored ropes used for wave, slam, and spiral patterns; builds conditioning, shoulders, and grip."
              ),
    Equipment(id = 25,
              type = "Functional",
              name = "TRX / Suspension Trainer",
              description = "Adjustable straps anchored overhead; uses bodyweight at varying angles for rows, push-ups, pikes, and lunges."
              ),
    Equipment(id = 26,
              type = "Functional",
              name = "Plyo Box",
              description = "Sturdy box for box jumps, step-ups, and depth drops; develops explosive leg power and agility."
              ),
    Equipment(id = 27,
              type = "Functional",
              name = "Medicine Ball",
              description = "Weighted ball for slams, throws, and rotational drills; builds power and core stability."
              ),
    Equipment(id = 28,
              type = "Functional",
              name = "Foam Roller",
              description = "Cylindrical foam tool for self-myofascial release; reduces muscle soreness and improves mobility."
              ),
    Equipment(id = 29,
              type = "Functional",
              name = "Resistance Bands",
              description = "Elastic bands providing variable resistance; used for activation drills, assisted stretching, and accessory exercises."
              ),
    Equipment(id = 30,
              type = "Functional",
              name = "Gymnastic Rings",
              description = "Suspended rings for push-ups, dips, rows, and muscle-ups; demands high stabilizer engagement."
              ),
    Equipment(id = 31,
              type = "Functional",
              name = "Sled / Prowler",
              description = "Heavy push/pull sled; develops lower-body power, conditioning, and posterior chain strength."
              ),
    # Strength
    Equipment(id = 32,
              type = "Strength",
              name = "Leg Press",
              description = "Pushes weight away using legs; targets quads, glutes, and hamstrings."
              ),
    Equipment(id = 33,
              type = "Strength",
              name = "Hack Squat",
              description = "Mimics squat pattern with additional support; works quads, glutes, hamstrings."
              ),
    Equipment(id = 34,
              type = "Strength",
              name = "Chest Press",
              description = "Horizontal pressing motion; trains chest, shoulders, and triceps."
              ),
    Equipment(id = 35,
              type = "Strength",
              name = "Lat Pulldown",
              description = "Pulls bar from overhead; focuses on latissimus dorsi, biceps, and upper back."
              ),
    Equipment(id = 36,
              type = "Strength",
              name = "Shoulder Press",
              description = "Vertical push; isolates shoulders and triceps."
              ),
    Equipment(id = 37,
              type = "Strength",
              name = "Bicep Curl Machine",
              description = "Elbow flexion in isolation; isolates biceps."
              ),
    Equipment(id = 38,
              type = "Strength",
              name = "Triceps Extension Machine",
              description = "Elbow extension; targets triceps muscles."
              ),
    Equipment(id = 39,
              type = "Strength",
              name = "Leg Extension",
              description = "Straightens knee against resistance; isolates quadriceps."
              ),
    Equipment(id = 40,
              type = "Strength",
              name = "Leg Curl",
              description = "Flexes knee from prone or seated position; isolates hamstrings."
              ),
    Equipment(id = 41,
              type = "Strength",
              name = "Inner/Outer Thigh Machines",
              description = "Hip adduction/abduction; strengthens adductor and abductor muscles."
              ),
    Equipment(id = 42,
              type = "Strength",
              name = "Glute Bridge Machine",
              description = "Guided bridge thrust; targets glutes and hamstrings."
              ),
    Equipment(id = 43,
              type = "Strength",
              name = "Smith Machine",
              description = "Multi-purpose, guided barbell; used for squats, bench presses, and more, engaging different muscle groups dependent on exercise."
              ),
    Equipment(id = 44,
              type = "Strength",
              name = "Seated Row Machine",
              description = "Horizontal pulling motion; emphasizes mid-back, rhomboids, rear delts, and biceps."
              ),
    Equipment(id = 45,
              type = "Strength",
              name = "Pec Deck (Chest Fly Machine)",
              description = "Brings arms together in an arc; isolates the chest (pectoralis major) with reduced shoulder strain."
              ),
    Equipment(id = 46,
              type = "Strength",
              name = "Rear Delt Fly Machine",
              description = "Reverses the pec deck motion; targets rear deltoids and upper back."
              ),
    Equipment(id = 47,
              type = "Strength",
              name = "Seated Calf Raise Machine",
              description = "Plantarflexion under load in a seated position; isolates the soleus muscle of the calf."
              ),
    Equipment(id = 48,
              type = "Strength",
              name = "Standing Calf Raise Machine",
              description = "Plantarflexion under a shoulder yoke; emphasizes the gastrocnemius (upper calf)."
              ),
    Equipment(id = 49,
              type = "Strength",
              name = "Assisted Pull-Up / Dip Machine",
              description = "Counterweighted platform assists pull-ups and dips; builds back, biceps, chest, and triceps."
              ),
    Equipment(id = 50,
              type = "Strength",
              name = "Hyperextension Bench",
              description = "Hip-hinge extension; targets lower back (erector spinae), glutes, and hamstrings."
              ),
    Equipment(id = 51,
              type = "Strength",
              name = "Preacher Curl Machine",
              description = "Supports upper arms on a pad during elbow flexion; strictly isolates the biceps and brachialis."
              ),
    Equipment(id = 52,
              type = "Strength",
              name = "Rotary Torso Machine",
              description = "Seated trunk rotation against resistance; targets obliques and rotational core muscles."
              ),
    Equipment(id = 53,
              type = "Strength",
              name = "Chest-Supported Row Machine",
              description = "Prone row with chest support; removes lower-back involvement to isolate mid-back and rear delts."
              ),
]

user_equipment: list[Equipment] = []
