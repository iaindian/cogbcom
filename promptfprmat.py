import json

raw_prompts = """
 ((cjw woman)) standing beside the pool at the (pool party), wearing a tiny red string bikini with triangle-cut top and tied bottoms, sheer white floral cover-up draped over her shoulders, white platform sandals on her feet, and silver mirrored sunglasses on her head
 ((cjw woman)) sitting on the pool steps at the (pool party), wearing a tiny red string bikini with water clinging to the tight triangle top and tied bottoms, sandals off and set beside her, sunlight reflecting on her soaked chest
 ((cjw woman)) lying on a towel-draped lounge chair at the (pool party), wearing a tiny red string bikini, back arched, one hand grazing her inner thigh as she glances seductively over her sunglasses
 ((cjw woman)) kneeling at the edge of the pool at the (pool party), wearing a tiny red string bikini, tugging down one side of the tied bottoms while her nipples show through the tight wet fabric
 ((cjw woman)) topless, lying on a bright yellow pool float at the (pool party), her bare breasts glistening in the sun, the tiny red bikini bottoms still tied tight at her hips, sunglasses resting on her nose
 ((cjw woman)) topless, kneeling on a lounge chair at the (pool party), wearing only red bikini bottoms, breasts pushed forward as she runs a hand across her chest with a teasing grin
 ((cjw woman)) topless, standing by the outdoor shower at the (pool party), wearing red string bikini bottoms, arching her back with both hands in her wet hair, breasts fully exposed under the sunlight
 ((cjw woman)) topless, sitting on a towel beside the pool at the (pool party), red bikini bottoms pulled halfway down her thighs, her legs spread slightly as she looks at the camera with a playful smirk
 ((cjw woman)) completely nude, kneeling on a lounge chair at the (pool party), her red bikini tossed beside her, legs parted and one hand resting on her inner thigh as she looks shyly at the camera
 ((cjw woman)) completely nude, standing near the glass fence at the (pool party), body dripping with water, arms down and pussy fully visible, her gaze flirtatious and inviting
 ((cjw woman)) completely nude, lying on her side on a towel-covered chair at the (pool party), legs stretched out and breasts resting on the chair as she tilts her head playfully toward the viewer
 ((cjw woman)) completely nude, crouched beside the pool at the (pool party), ass raised, back arched, one hand gently spreading her pussy lips open to show her folds
 ((cjw woman)) completely nude, standing in front of the hot tub at the (pool party), legs parted slightly, holding up one finger pointed at her pussy as if teasing, “want me to put this inside?”
 ((cjw woman)) completely nude, sitting on a towel by the pool at the (pool party), one knee up and her other leg extended, pointing one finger toward her pussy with a naughty grin
 ((cjw woman)) completely nude, standing on the pool steps at the (pool party), holding up two fingers toward her wet pussy in a taunting pose as if preparing to insert them
 ((cjw woman)) completely nude, lying back on a deck chair at the (pool party), legs spread wide as she is (fingering herself) with two fingers, her head tilted back in pleasure
 ((cjw woman)) completely nude, squatting on a towel at the (pool party), one hand gripping her thigh while the other hand is (fingering herself) deeply, her mouth open as she pants
 ((cjw woman)) completely nude, standing under the outdoor shower at the (pool party), water cascading down her back as she uses two fingers to (finger herself), her hips grinding against her hand
 ((cjw woman)) completely nude, lying with her legs up against the pool fence at the (pool party), body trembling as she is (fingering herself) furiously, her breasts bouncing slightly with each motion
 ((cjw woman)) completely nude, kneeling on a pool lounger at the (pool party), leaning back with her fingers dripping from (fingering herself), mouth open and gaze fixed on a hard cock in front of her
 ((cjw woman)) completely nude, sitting on a lounge chair at the (pool party), looking up at a man in front of her, his cock fully visible as she licks her lips and says “want me to (blow you)?”
 ((cjw woman)) completely nude, kneeling between a man's legs on a towel at the (pool party), her hand wrapped around his cock, staring up at him seductively as she prepares to (blow him)
 ((cjw woman)) completely nude, on her knees at the (pool party), lips parted and tongue out as she slowly leans toward his cock for a (blowjob), her breasts brushing his thighs
 ((cjw woman)) completely nude, giving a (blowjob) by the pool at the (pool party), her cheeks hollowing as she sucks his cock, fingers gripping his thighs tightly
 ((cjw woman)) completely nude, kneeling on the pool deck at the (pool party), hungrily (blowing him), spit trailing from her lips to his cock as she goes deeper
 ((cjw woman)) completely nude, poolside at the (pool party), her head bobbing rapidly as she gives a messy (blowjob), his cock disappearing between her lips as her eyes water from the intensity
 ((cjw woman)) completely nude, lying on her back across a lounge chair at the (pool party), head hanging over the edge as she is (deepthroating his cock), throat bulging with the stretch
 ((cjw woman)) completely nude, one hand wrapped around his cock while the other cups his balls at the (pool party), her lips and chin soaked in spit during an intense (blowjob)
 ((cjw woman)) completely nude, sitting up from a (blowjob) by the pool at the (pool party), his cock twitching against her lips as she gasps for breath, spit and precum dripping from her mouth
 ((cjw woman)) completely nude, holding his cock in both hands as she looks up from between his legs at the (pool party), smiling before going back down for another (blowjob)
 ((cjw woman)) completely nude, lying back on a poolside towel at the (pool party), legs spread as a man kneels between them, his cock pressed against her entrance as if about to (fuck her)
 ((cjw woman)) completely nude, holding onto the pool railing at the (pool party), bent forward with a man’s cock rubbing up and down her pussy lips, teasing before he (fucks her)
 ((cjw woman)) completely nude, POV view of her straddling a man in the pool at the (pool party), his cock beginning to enter her as she prepares to (ride him)
 ((cjw woman)) completely nude, POV angle from above as a man’s cock slides slowly into her tight pussy at the (pool party), her legs wrapped around his waist as he begins to (fuck her)
 ((cjw woman)) completely nude, bent over a lounge chair at the (pool party), being (fucked) from behind, her ass bouncing with each thrust and hands gripping the cushions
 ((cjw woman)) completely nude, straddling a man in the hot tub at the (pool party), her hands on his chest as she moans while being (fucked) in cowgirl position
 ((cjw woman)) completely nude, lying back on a pool lounger at the (pool party), legs up in the air as she is (fucked) in deep missionary, her breasts bouncing with every thrust
 ((cjw woman)) completely nude, kneeling on all fours beside the pool at the (pool party), her body rocking as she is (fucked) hard from behind, her face twisted in ecstasy
 ((cjw woman)) completely nude, squatting on top of a man seated on the pool steps at the (pool party), riding him hard as his cock slams up into her, water splashing around them
 ((cjw woman)) completely nude, lying on her stomach on a pool towel at the (pool party), ass raised as a man pounds her pussy from behind, gripping her hips tightly as he (fucks her)
 ((cjw woman)) completely nude, kneeling poolside at the (pool party), looking up at a man standing over her, his cock erupting mid-((cumshot)) across her chest, thick white streams landing between her bare breasts
 ((cjw woman)) completely nude, lying on her back on a pool lounger at the (pool party), legs spread as a man strokes his cock and delivers a dripping ((cumshot)) all over her stomach and tits
 ((cjw woman)) completely nude, straddling a man lying on a towel at the (pool party), her hands on his chest as he grips her waist and cums with a powerful ((cumshot)) deep inside her pussy
 ((cjw woman)) completely nude, bent over the edge of a lounge chair at the (pool party), a man pulling out and delivering a thick ((cumshot)) across her ass and lower back, his cock still pulsing
 ((cjw woman)) completely nude, lying back with her knees to her chest on the pool deck at the (pool party), a man kneeling between her thighs and cumming directly into her soaked pussy with a hard ((cumshot))
 ((cjw woman)) completely nude, kneeling on a towel by the pool at the (pool party), tongue out as a man strokes his cock and erupts mid-((cumshot)) across her face and open mouth
 ((cjw woman)) completely nude, riding a man in the shallow end of the pool at the (pool party), her hips grinding as his cock jerks and releases a deep ((cumshot)) inside her
 ((cjw woman)) completely nude, bent over the pool steps at the (pool party), gripping the handrail as a man pulls out and shoots a messy ((cumshot)) across her wet pussy and ass
 ((cjw woman)) completely nude, lying belly-down on a lounger at the (pool party), her ass raised high as a man jerks his cock and paints her back with a thick ((cumshot))
 ((cjw woman)) completely nude, sitting on the pool edge at the (pool party), mouth wide open as a man stands over her, his cock pulsing as he unloads a warm ((cumshot)) onto her tongue and lips
 ((cjw woman)) completely nude, kneeling between a man’s legs on the pool deck at the (pool party), head tilted back as she catches a powerful ((cumshot)) mid-air in her open mouth
 ((cjw woman)) completely nude, lying on her back at the (pool party), a man straddling her chest, gripping his cock as he pumps out a massive ((cumshot)) directly into her mouth and over her face
 ((cjw woman)) completely nude, kneeling at the base of a lounge chair at the (pool party), eyes closed and lips parted as a man holds her head and finishes a sticky ((cumshot in her mouth)), cum dripping down her chin
 ((cjw woman)) completely nude, sitting on her heels at the (pool party), her cheeks puffed and mouth sealed around a man's cock as he finishes a deep ((cumshot in her mouth)), his hand resting on the back of her head
 ((cjw woman)) completely nude, kneeling on a towel beside the hot tub at the (pool party), cum dripping from her lips as she looks up at the man towering above her, his cock still twitching from the final pulse of a heavy ((cumshot in her mouth))

""".strip().splitlines()

negative = "more fingers, blur, bad anatomy, lowres, watermark"

output = []
for i, line in enumerate(raw_prompts, start=1):
    output.append({
        "id": f"prompt{i:02d}",
        "positive": line,
        "negative": negative
    })

# print(json.dumps(output, indent=2))

with open("prompt1.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Saved {len(output)} prompts to prompt1.json")