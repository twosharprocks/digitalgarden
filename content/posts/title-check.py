import os

def check_markdown_titles(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".md"):
            file_path = os.path.join(folder_path, filename)

            with open(file_path, "r", encoding="utf-8") as file:
                lines = []
                for _ in range(5):  # read first few lines (safe buffer)
                    try:
                        lines.append(next(file).rstrip("\n"))
                    except StopIteration:
                        break  # file shorter than expected, stop reading

            # Track blank lines at the top
            blank_lines = 0
            for line in lines:
                if line.strip() == "":
                    blank_lines += 1
                else:
                    break

            # Remove the blank lines before checking front matter
            content = [l for l in lines if l.strip() != ""]

            # Check for expected structure
            if len(content) < 2:
                print(f"⚠️ Too short to check: {filename}")
                continue

            first_line = content[0].strip()
            second_line = content[1].strip()

            if first_line != "---" or not second_line.startswith("title:"):
                print(f"❌ Invalid front matter: {filename}")
            else:
                print(f"✅ OK: {filename}")

            # Report blank lines if any
            if blank_lines > 0:
                print(f"   ⚠️ {blank_lines} blank line(s) at start of {filename}")

# Example usage
folder = r"C:\Users\Josh\Documents\garden\content\posts"
check_markdown_titles(folder)
