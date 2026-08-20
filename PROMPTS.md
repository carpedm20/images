# Generation prompts

All fixtures were generated with OpenAI's built-in image generation tool on
2026-08-20. No reference image was used.

Every prompt shared this contract:

> Create an original, photorealistic, square ecommerce catalog image on a
> neutral studio background. Keep the complete primary product clear. Do not
> include logos, trademarks, watermarks, packaging, or readable brand text.
> The output is a public regression-test fixture for garment classification.

The per-file primary requests were:

| File | Primary request |
| --- | --- |
| `valid-flat-cat-sushi-tee.png` | One adult heather-gray short-sleeve T-shirt laid flat, with six whimsical generic cats arranged like sushi printed on the fabric. |
| `valid-modeled-menu-print-long-sleeve.png` | Back view of an adult model wearing a black long-sleeve shirt whose back has a dense white grid of abstract menu-like pseudo-text and small food icons. |
| `valid-two-model-graphic-tees.png` | Two adult models, one front-facing and one back-facing, wearing off-white T-shirts covered with original fish, cat, and food illustrations. |
| `valid-fishing-utility-vest.png` | One adult olive fishing utility vest laid flat, with mesh panels, pockets, zippers, straps, and realistic technical construction. |
| `valid-cropped-dense-print-tee.png` | A deliberately close ecommerce crop of an adult navy T-shirt with dense white text-like print; collar, sleeves, torso, and fabric remain identifiable. |
| `non-target-script-lampshade.png` | One tapered cream fabric lampshade printed with dense decorative handwritten pseudo-script, unmistakably a home-lighting product. |
| `non-target-washer-drain-pump.png` | One washing-machine drain-pump replacement part with plastic housing, motor, terminals, and impeller details. |
| `non-target-car-seat-cover.png` | One fitted automotive seat cover installed on an isolated car seat, with headrest, bolsters, seams, and harness openings. |
| `non-target-cat-sushi-blanket.png` | One rectangular fleece throw blanket laid flat with a folded corner and repeating original cat-and-sushi illustrations. |
| `challenge-dog-sweater.png` | A small dog wearing a red knitted pet sweater, clearly showing both the animal and pet garment. |
| `challenge-doll-outfit.png` | A miniature floral doll dress on a tiny hanger beside doll-scale shoes, with scale made explicit. |

The valid cases additionally required that the sold product be unmistakably an
adult human garment. The non-target cases required that the primary object be
unmistakably outside human fashion. The challenge cases intentionally combine
garment visual cues with a non-human intended wearer.

## Branch-complete expansion

The following exact prompts produced the additional v1 assets. No separate
negative-prompt field was used; exclusions are written directly in each prompt.

### Matched front subject

> Create one original photorealistic full-body ecommerce studio photograph for
> a public virtual-try-on regression test. A single adult woman with medium-brown
> skin and an average build stands straight, front-facing, centered, arms
> relaxed slightly away from the torso, feet fully visible, neutral expression.
> She wears a plain close-fitting light gray sleeveless top and plain charcoal
> fitted shorts, with no jacket, dress, accessories, logos, text, patterns, or
> shoes. Soft even lighting, seamless pale gray background, portrait composition
> with generous margin around the complete body, anatomically realistic hands
> and feet. Exactly one person, no mirrors, no props, no watermark, no readable
> text.

### Matched side subject

This was an edit of the generated front subject, using that image as the only
reference.

> Create the matching side-view companion for this virtual-try-on test subject.
> Preserve the same adult woman's identity, skin tone, hair, body proportions,
> plain light gray sleeveless top, plain charcoal fitted shorts, bare feet,
> lighting, scale, pale gray studio background, and full portrait framing.
> Rotate her body exactly 90 degrees into a clean left-facing side profile, head
> aligned with torso, neutral expression, arms relaxed straight at her sides
> without hiding the torso silhouette, both feet fully visible. Exactly one
> person, complete body with generous margins, no mirrors, props, logos,
> patterns, text, accessories, watermark, or extra limbs.

### Low-contrast bottom

> Create one original photorealistic square ecommerce catalog image for a public
> virtual-try-on regression test. Show exactly one adult pair of ivory wide-leg
> pleated trousers laid flat, front view, fully visible from waistband to both
> hems. The nearly white fabric sits on a very pale warm-gray seamless
> background, deliberately low contrast but with seams, waistband, belt loops,
> pockets, pleats, and trouser silhouette still physically clear. No person,
> mannequin, hanger, belt, shoes, other garments, logos, brand text, watermark,
> packaging, or readable text. Soft diffuse studio lighting, realistic fabric
> texture and natural folds, centered product with modest margin.

### Transparent footwear cutout

> Create one original photorealistic ecommerce product cutout for a public
> virtual-try-on regression test. Show exactly one matching pair of low-top
> sneakers, three-quarter view, complete and centered, with white mesh uppers,
> pale blue panels, cream rubber soles, laces, eyelets, and realistic
> construction. Isolate only the shoes on a genuinely transparent alpha
> background with clean edges and no floor, shadow, person, feet, socks, box,
> props, logos, brand marks, watermark, or readable text. Square PNG composition
> with generous transparent whitespace; preserve fine lace openings and the gap
> between the shoes.

### Tiny bag

> Create one original photorealistic square ecommerce catalog image for a public
> virtual-try-on regression test. Show exactly one very small emerald-green
> crossbody bag with a long thin strap arranged in a loose loop, front
> three-quarter view. The bag itself should occupy only about 18 percent of the
> canvas height, centered within unusually large clean white studio whitespace,
> testing tiny-product detection. Keep the complete strap and bag visible,
> including flap, stitching, clasp, and realistic leather texture. No person,
> mannequin, hand, other fashion item, logos, brand text, watermark, packaging,
> or readable text; soft subtle grounding shadow only.

### Dark-on-dark headwear

> Create one original photorealistic square ecommerce catalog image for a public
> virtual-try-on regression test. Show exactly one soft black bucket hat,
> three-quarter view, fully visible, with a floppy asymmetric brim, tonal
> stitched concentric rings, two thin chin cords crossing once and ending in
> small toggles. Place it on a very dark charcoal seamless studio background so
> the silhouette is deliberately low contrast while rim light still reveals the
> hat and cords. No person, mannequin head, hair, other fashion items, logos,
> text, pattern, watermark, or packaging. Centered product, realistic fabric and
> construction, complete cords inside the frame.

### Complex one-piece

> Create one original photorealistic square ecommerce catalog image for a public
> virtual-try-on regression test. Show exactly one adult ankle-length wrap dress
> laid flat, complete from shoulders to hem, with one long sleeve and one short
> flutter sleeve, a tied waist sash, layered asymmetric hem, and a dense original
> botanical-and-geometric print in coral, teal, navy, and cream. It must be
> unmistakably a single one-piece human garment despite the complex pattern and
> overlapping fabric. Neutral light-gray studio background, realistic folds and
> seams, centered. No person, mannequin, hanger, shoes, bag, other garments,
> logos, brand text, watermark, packaging, or readable text.

### Sparse eyewear

> Create one original photorealistic square ecommerce catalog image for a public
> virtual-try-on regression test. Show exactly one pair of nearly transparent
> rimless eyeglasses, open in a three-quarter view, with very thin silver
> temples, clear nose pads, clear lenses, tiny hinges, and realistic soft
> reflections. Place them on a clean white seamless studio background so the
> product is deliberately sparse and low contrast, but keep the entire frame and
> both temple arms visible. No face, person, mannequin, case, cloth, other
> accessories, logo, brand text, watermark, packaging, or readable text.
> Centered with generous whitespace and a very subtle grounding shadow.

### Wearable textile accessory

> Create one original photorealistic square ecommerce catalog image for a public
> virtual-try-on regression test. Show exactly one adult silk neck scarf tied in
> a loose asymmetric bow with two narrow tails, fully visible, isolated on a
> neutral pale-gray studio background. Use a dense original abstract print of
> cobalt waves, orange dots, cream lines, and tiny geometric marks that resemble
> design details but contain no readable words. The compact tied form and
> finished rolled edges must make it clearly a wearable fashion accessory rather
> than a blanket. No person, mannequin, hanger, bag, clothing, jewelry, logos,
> brand text, watermark, packaging, or readable text. Centered, realistic sheen
> and folds.

### Clear single-person outfit

> Create one original photorealistic full-body ecommerce editorial photograph
> for a public virtual-try-on regression test. Exactly one adult man with East
> Asian features and a slim build stands front-facing in a neutral studio, face
> clearly visible, entire body and shoes in frame. He wears a complete layered
> outfit: cream graphic-free T-shirt, open rust overshirt, dark teal straight
> trousers, white sneakers, and a small black crossbody bag. Arms slightly away
> from the torso so every garment remains visible; neutral pose and expression.
> Pale beige seamless background, soft even lighting, portrait composition. No
> other people, mirrors, props, collage panels, logos, readable text, watermark,
> or brand marks.

### Threshold-small single person

> Create one original photorealistic square ecommerce catalog image for a public
> virtual-try-on detector-boundary regression test. Exactly one adult woman
> stands full-body near the lower-right of a very large pale-gray studio canvas,
> occupying only about 32 percent of the image height, with abundant empty space
> everywhere else. She wears a clearly visible bright cobalt blazer over a white
> top, black trousers, and red shoes. Her front-facing face should remain clean
> and recognizable despite the distant scale; neutral pose, arms slightly apart.
> No enlarged product inset, collage border, second person, mannequin, mirrors,
> props, logos, readable text, watermark, or brand marks. The intentionally tiny
> single person is the only subject.
