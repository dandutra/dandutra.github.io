// Spec rule 5, on file sizes. Lighthouse budgets can't cap a sum of types or one file.
import { readdirSync, statSync } from "node:fs";

const KB = 1024;
const sizeOf = (path) => statSync(path).size;
const failures = [];

const pageFiles = [
  "index.html",
  ...readdirSync(".").filter((f) => /\.(css|js)$/.test(f)),
];
const pageBytes = pageFiles.reduce((sum, f) => sum + sizeOf(f), 0);
console.log(
  `${pageFiles.join(" + ")}: ${(pageBytes / KB).toFixed(1)} KB (limit 30 KB)`,
);
if (pageBytes > 30 * KB) failures.push("index.html + CSS + JS");

const screenshots = readdirSync("assets").filter((f) => f.endsWith(".webp"));
for (const f of screenshots) {
  const bytes = sizeOf(`assets/${f}`);
  console.log(`assets/${f}: ${(bytes / KB).toFixed(1)} KB (limit 40 KB)`);
  if (bytes > 40 * KB) failures.push(`assets/${f}`);
}

console.log(
  `Checked ${pageFiles.length + screenshots.length} files, ${failures.length} over budget.`,
);
if (screenshots.length === 0) failures.push("no screenshots found in assets/");
if (failures.length) {
  console.error(`Failed: ${failures.join(", ")}`);
  process.exit(1);
}
