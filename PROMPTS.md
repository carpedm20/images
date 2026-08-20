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
