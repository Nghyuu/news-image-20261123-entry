// news-image-20261123 entrypoint.
// Copies the pre-rendered entry.png (built at build time by draw.py)
// into the output directory. Node stdlib only; no network, no shelling out.
import { copyFileSync, existsSync, mkdirSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const src = join(here, "entry.png");
if (!existsSync(src)) {
  console.error("entry.png missing next to main.ts");
  process.exit(1);
}
const outDir = process.env.MAKEFUN_OUTPUT_DIR;
if (!outDir) {
  console.error("MAKEFUN_OUTPUT_DIR is not set");
  process.exit(1);
}
mkdirSync(outDir, { recursive: true });
copyFileSync(src, join(outDir, "entry.png"));
console.log(`wrote entry.png (${statSync(src).size} bytes)`);
