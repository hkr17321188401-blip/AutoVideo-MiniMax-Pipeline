AutoVideo-MiniMax-Pipeline
Automated end-to-end video generation pipeline integrating prompt orchestration with MiniMax Video-01 API and Hailuo AI. Designed for high-throughput AI short-form content production
Overview
Generating AI video at scale often requires tedious manual prompting, queue management, status polling, and asset downloading across web interfaces. AutoVideo-MiniMax-Pipeline automates the entire lifecycle from structured prompt inputs to final rendered MP4 exports, ready for downstream editing or automated publishing pipelines
Key Features
- Batch Task Queue: Feed text prompts or image references via JSON/CSV and let the worker manage submission queues automatically
- Polling and Auto-Download: Asynchronous task tracking with automatic retry, timeout handling, and asset retrieval
- High-Quality Presets: Configured for MiniMax Video-01 generation parameters with camera motion control
- Decoupled Config: Clean separation between credentials, task payloads, and output artifacts
- Pipeline Ready: Seamlessly pipes output into downstream engines like AutoAudioSync-Engine for complete hands-free production
Architecture
1. Prompt Ingestion: Ingest structured prompts, aspect ratios, and camera movement tags
2. MiniMax / Hailuo API: Submit asynchronous generation requests
3. Task Worker: Poll generation status with exponential backoff
4. Asset Sync: Download completed MP4 clips into raw_footage/ directory
Quick Start
Prerequisites
- Python 3.10+
- MiniMax API Key
Installation & Run
1. Clone this repository
2. Install dependencies: pip install requests
3. Set your API credentials in config.json or environment variables
4. Run the pipeline: python video_pipeline.py
Support the Project
If this tool saved your production hours, feel free to buy me a coffee:
USDT (TRC20): TVGr7ffrZEfBVxxGAeo2oB6aV8qcCUjLHP
