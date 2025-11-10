---

# Auto Transcriber + YouTube Metadata Generator (WIP)

This project is a work-in-progress tool that automates parts of the video publishing workflow. It currently handles":"

✅ **video → audio → transcript**

I’m gradually expanding it so the pipeline becomes smarter, more structured, and eventually (hopefully) fully automated.

This is something I’m building for fun and learning":" but it’s already useful, and who knows where it goes next.

---

## Current Features

* Convert video to audio
* Transcribe audio to text
* Optional transcript with timestamps
* Simple folder-based processing

---

## Planned Pipeline

1. **video → audio → transcript (with timestamps)**
2. **LLM processing** for descriptions, keywords, SEO text
3. **Structured output** (JSON + clean text)
4. **YouTube Data API integration**
5. **One-button draft creation** with all metadata autofilled

---

## Roadmap / Things to Implement

### ✅ Faster-Whisper

Switch from Whisper to **faster-whisper** for:

* better speed
* lower VRAM usage
* improved throughput
* smoother performance on GPU

### ✅ Structured JSON Output

Use JSON to store:

* title suggestions
* short + long descriptions
* chapters
* tags + keywords
* transcript metadata
* timestamps
* future extensions

### ✅ Microservice Setup

Run the pipeline on a PC with better specs, accessible from any device.

Plan:

* containerize the service (Docker)
* run FastAPI backend
* enable GPU acceleration
* accept uploads or shared folder input
* return generated artifacts

### ✅ File Handling

Possible ingestion methods:

* direct API upload
* shared folder
* Tailscale file transfer
* mounted network drive
* remote HTTP download

### ✅ Hashing / Skip Duplicates

Use SHA-256 to:

* check for duplicates
* skip reprocessing
* speed up workflow
* save compute resources

### ✅ YouTube Data API Integration

Eventually automate:

* draft creation
* title + description population
* tags
* captions
* thumbnails (future idea)
* video scheduling

---

## To-Do List (Short Version)

* [ ] Replace Whisper with faster-whisper
* [ ] Add timestamped transcripts
* [ ] Integrate LLM for metadata generation
* [ ] Output structured JSON + clean txt summaries
* [ ] Build a microservice wrapper (API)
* [ ] Add SHA-256 dedupe logic
* [ ] Implement YouTube API upload
* [ ] Optional: word-level timestamps via whisperX
* [ ] Optional: UX improvements for readability

---

## Notes

This is an in-progress learning project, and the design may evolve as I go. The goal is not to over-engineer, but to steadily improve the speed, automation, and quality of the content pipeline.

If it eventually becomes a one-button “publish to YouTube with everything generated automatically,” that would be a fun milestone.

---
