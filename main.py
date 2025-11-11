from graph import app

def main():
    while True:
        text = input("\nEnter patient symptoms: ")

        if text.lower() in ["exit", "quit"]:
            print("Exiting medical assistant...")
            break

        state = {"input": text}  # ✅ Important: initial key must be "input"

        print("\n--- Processing ---\n")
        final_output = {}

        for step in app.stream(state):
            for key, value in step.items():
                final_output[key] = value

        print("\n✅ Final Medical Report:\n")
        print(final_output.get("report", "No report generated"))

if __name__ == "__main__":
    main()
