// the420code.org in every language: the translation fan-out, one agent per slice.
// Launched with the Workflow tool; args = { lang: "de", batches: ["de__g1b000", ...], mode: "translate" | "review" }.
// Each agent reads its prompt file from disk (written by prompts.py write <lang>) and writes its patch file.
export const meta = {
  name: 'the420code-translate',
  description: 'Translate (or review) the slices of one language of the420code.org, one agent per slice',
  phases: [{ title: 'Translate', detail: 'one agent per slice writes a patch file' }],
}
let A = args
if (typeof A === 'string') A = JSON.parse(A)
if (A && A.lang && !A.batches && A.count) {
  // batchize.py names a cut's slices <lang>__g<gen>b000 ... ; pass gen and count (both printed by batchize.py)
  const g = A.gen ? `g${A.gen}` : ''
  A.batches = Array.from({ length: A.count }, (_, i) => `${A.lang}__${g}b${String(i).padStart(3, '0')}`)
}
if (!A || !A.lang || !Array.isArray(A.batches) || !A.batches.length) throw new Error('args.lang and args.batches (or count) needed')
const mode = A.mode || 'translate'
const SCHEMA = { type: 'object', properties: { batch: { type: 'string' }, n: { type: 'integer' }, valid: { type: 'boolean' } }, required: ['batch', 'n', 'valid'] }
log(`${A.lang}: ${A.batches.length} slices, ${mode}`)
phase('Translate')
const results = await parallel(A.batches.map(b => () => agent(
  `Read the file C:/Users/info/the420code-i18n-work/${A.lang}/prompts/${b}${mode === 'review' ? '.review' : ''}.md with the Read tool and do exactly what it says: it is your whole brief (the language, the voice, the rules, the locked words, the slice to read, the file to write and the validation to run). Never skip the validation. Return batch="${b}", n = the number the validation printed, valid = whether it printed the number the brief expects.`,
  { label: `${mode}:${b}`, phase: 'Translate', schema: SCHEMA })))
const bad = []
results.forEach((r, i) => { if (!r || !r.valid) bad.push(A.batches[i]) })
log(`${A.lang}: ${A.batches.length - bad.length}/${A.batches.length} slices valid`)
return { lang: A.lang, mode, total: A.batches.length, bad }
