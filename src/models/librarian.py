import uuid

class Librarian:
    def __init__(self, name, email):
        self.employee_id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.sections = []  # list of section_ids this librarian manages
        # Add more attributes as needed
    
    def assign_section(self, section_id):
        """Assign a section to this librarian"""
        if section_id not in self.sections:
            self.sections.append(section_id)
            return True
        return False
    
    def remove_section(self, section_id):
        """Remove a section from this librarian"""
        if section_id in self.sections:
            self.sections.remove(section_id)
            return True
        return False