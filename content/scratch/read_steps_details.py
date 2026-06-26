import json

transcript_path = r"C:\Users\Hero\.gemini\antigravity\brain\c90890fa-d75e-4b8f-99de-acc3a60af337\.system_generated\logs\transcript.jsonl"

with open(transcript_path, "r", encoding="utf-8") as f:
    for line in f:
        try:
            data = json.loads(line)
            step = data.get("step_index")
            if 275 <= step <= 285:
                print(f"Step {step} ({data.get('type')}):")
                print("Thinking:", data.get("thinking", "")[:500])
                print("Content:", data.get("content", "")[:200])
                print("-" * 40)
        except Exception as e:
            pass
