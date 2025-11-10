# Auto Transcriber + YouTube Metadata Generator (WIP)

This project is a work-in-progress tool that automates parts of the video publishing workflow for video transcription, captions, chapters, and YouTube SEO metadata. It currently handles:

✅ **video → audio → transcript**

I’m gradually expanding it so the pipeline becomes smarter, more structured, and eventually (hopefully) fully automated.

---

## Overview ʕ•ᴥ•ʔ

This project is a personal tool I built to speed up video production for the **Meloy Engineering Entrepreneurship Program** at Texas A&M University. With a campus of more than **70,000 students**, the Meloy Program creates content that reaches and supports a huge community, and producing that content quickly and consistently matters.

The workflow often involves many repeatable tasks:

- Convert video → audio
- Generate accurate captions
- Pull SEO keywords and hashtags
- Draft descriptions
- Create chapter markers
- Prepare content for YouTube upload

I wanted to automate these steps so I could focus more on creativity, storytelling, and production quality rather than repeating manual work.

This project started as something fun: a personal experiment to learn Whisper, GPU inference, microservices, and system design. But it quickly became a genuinely useful tool for the production pipeline. And maybe one day I’ll scale it further or adapt it for other teams, creators, or tools. Who knows?

---

## Why I built this (ง'̀-'́)ง

I’m running content creation workflows for the **Meloy Engineering Entrepreneurship** channel, and part of the job is optimizing videos for clarity, accessibility, and reach.

Manually doing this for each video:

- wastes time
- introduces inconsistencies
- slows down creativity

This project was a chance to learn:

- distributed design
- GPU inference optimization
- API + microservice patterns
- how to architect efficient workflows
- how to build production-adjacent tools
- how to automate repetitive tasks in content pipelines

It’s both practical and exploratory, and something I can iterate on and improve.

---

## Current Features (͡ ͡° ͜ つ ͡͡°)

- Convert video to audio
- Transcribe audio to text
- Optional transcript with timestamps
- Simple folder-based processing

---

## Planned Pipeline (づ｡◕‿‿◕｡)づ

1. **video → audio → transcript (with timestamps)**
2. **LLM processing** for descriptions, keywords, SEO text
3. **Structured output** (JSON + clean text)
4. **YouTube Data API integration**
5. **One-button draft creation** with all metadata autofilled

---

## Roadmap / Things to Implement

### Faster-Whisper

Switch from Whisper to **faster-whisper** for:

- better speed
- lower VRAM usage
- improved throughput
- smoother performance on GPU

**RESULT**: 538.0857 seconds -> 71.1989 seconds (755.75% increased throughput)

### Structured JSON Output

Use JSON to store:

- title suggestions
- short + long descriptions
- chapters
- tags + keywords
- transcript metadata
- timestamps
- future extensions

### Microservice Setup

Run the pipeline on a PC with better specs, accessible from any device.

Plan:

- containerize the service (Docker)
- run FastAPI backend
- enable GPU acceleration
- accept uploads or shared folder input
- return generated artifacts

### File Handling

Possible ingestion methods:

- direct API upload
- shared folder
- Tailscale file transfer
- mounted network drive
- remote HTTP download

### Hashing / Skip Duplicates

Use SHA-256 to:

- check for duplicates
- skip reprocessing
- speed up workflow
- save compute resources

### YouTube Data API Integration

Eventually automate:

- draft creation
- title + description population
- tags
- captions
- thumbnails (future idea)
- video scheduling

---

## ┬┴┬┴┤ ͜ʖ ͡°) ├┬┴┬┴

## To-Do List (Short Version)

- [x] Replace Whisper with faster-whisper
- [ ] Add timestamped transcripts
- [ ] Integrate LLM for metadata generation
- [ ] Output structured JSON + clean txt summaries
- [ ] Build a microservice wrapper (API)
- [ ] Add SHA-256 dedupe logic
- [ ] Implement YouTube API upload
- [ ] Optional: word-level timestamps via whisperX
- [ ] Optional: UX improvements for readability

---

## (ノ ಠ 益 ಠ)ノ彡 ┻━┻

## Notes

This is an in-progress learning project, and the design may evolve as I go. The goal is not to over-engineer, but to steadily improve the speed, automation, and quality of the content pipeline.

If it eventually becomes a one-button “publish to YouTube with everything generated automatically,” that would be a fun milestone.

---

## Thanks For Read(ing)Me!

```text
⠸⣷⣦⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⠀⠀
⠀⠙⣿⡄⠈⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠔⠊⠉⣿⡿⠁⠀⠀
⠀⠀⠈⠣⡀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠁⠀⠀⣰⠟
⠀⠀⠀⠀⠈⠢⣄⠀⡈⠒⠊⠉⠁⠀⠈⠉⠑⠚⠀⠀⣀⠔⢊⣠⠤⠒⠊⠉⠀⡜
⠀⠀⠀⠀⠀⠀⠀⡽⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠩⡔⠊⠁⠀⠀⠀⠀⠀⠀⠇
⠀⠀⠀⠀⠀⠀⠀⡇⢠⡤⢄⠀⠀⠀⠀⠀⡠⢤⣄⠀⡇⠀⠀⠀⠀⠀⠀⠀⢰⠀
⠀⠀⠀⠀⠀⠀⢀⠇⠹⠿⠟⠀⠀⠤⠀⠀⠻⠿⠟⠀⣇⠀⠀⡀⠠⠄⠒⠊⠁⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⡆⠀⠰⠤⠖⠦⠴⠀⢀⣶⣿⣿⠀⠙⢄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢻⣿⠃⠀⠀⠀⠀⠀⠀⠀⠈⠿⡿⠛⢄⠀⠀⠱⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠈⠓⠦⠀⣀⣀⣀⠀⡠⠴⠊⠹⡞⣁⠤⠒⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⠃⠀⠀⠀⠀⡌⠉⠉⡤⠀⠀⠀⠀⢻⠿⠆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠰⠁⡀⠀⠀⠀⠀⢸⠀⢰⠃⠀⠀⠀⢠⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢶⣗⠧⡀⢳⠀⠀⠀⠀⢸⣀⣸⠀⠀⠀⢀⡜⠀⣸⢤⣶⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠻⣿⣦⣈⣧⡀⠀⠀⢸⣿⣿⠀⠀⢀⣼⡀⣨⣿⡿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠻⠿⠿⠓⠄⠤⠘⠉⠙⠤⢀⠾⠿⣿⠟⠋
```

_Thanks for reading — contributions and feedback welcome._
