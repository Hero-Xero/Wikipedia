import re
import random
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))

def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title..
    If no such entry exists, the function returns None.
    added case-insensitive search for entries
    """
    all_entries = list_entries()  
    matched_entry = next((entry for entry in all_entries if entry.lower() == title.lower()), None) # the next is for stopping at the first match
    
    if matched_entry:
        try:
            with default_storage.open(f"entries/{matched_entry}.md") as f:
                return f.read().decode("utf-8")
        except FileNotFoundError:
            return None

    return None
    
def random_entry():
    """
    Returns a random entry from the list of entries
    """
    entries = list_entries()
    return random.choice(entries) if entries else None


def edit_entry(title, content, entry):
    """
    Edits an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """

    entry = f"entries/{entry}.md"
    if default_storage.exists(entry):
        default_storage.delete(entry)
        title = f"entries/{title}.md"
        default_storage.save(title, ContentFile(content))

