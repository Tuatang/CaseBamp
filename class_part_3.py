from datetime import datetime


class Element:
	def __init__(self, title, id):
		self.__title = title
		self.__id = id
		self.__in_trash = False

class Content:
	def __init__(self, details):
		self.__details = details

class ToDo(Element):
	numberic_id = 0
	id = "100" + str(numberic_id)
	def __init__(self, title, content, start_date, end_date, added_by, assigned_to, notify_who_when_done):
		super.__init__(title, id)
		self.__content = content
		self.__start_date = start_date
		self.__end_date = end_date
		self.__completed = completed
		self.__over_due = over_due
		self.__added_by = added_by
		self.__assigned_to = assigned_to
		self.__notify_who_when_done = notify_who_when_done

		numberic_id += 1
		id += str(numberic_id)

	def set_attribute(self, attribute, value):
		pass

class ToDosTopic(Element):
	numberic_id = 0
	id = "200" + str(numberic_id)
	def __init__(self, title, description):
		super.__init__(title,id)
		self.__description = description
		self.__list_of_to_dos = []
	def create_to_do(selected_to_dos_topic, title, content, start_date, end_date, added_by, assigned_to, notify_who_when_done):
		pass
	def edit_to_do(to_do, attribute, value):
		pass
	def get_to_do():
		pass
	def save_to_do(to_do):
		pass
	def check_to_do_for_assigned(user, to_do):
		pass

class DocumentOrFile(Element):
	numberic_id = 0
	id = "300" + str(numberic_id)
	def __init__(self, title, content, added_user, last_uploaded_date):
		super.__init__(title,id)
		self.__content = content
		self.__added_user = added_user
		self.__last_uploaded_date = last_uploaded_date

		numberic_id += 1
		id += str(numberic_id)

	def set_attribute(attribute, value):
		pass

class DocumentAndFilesFolder(Element):
	numberic_id = 0
	id = "400" + str(numberic_id)
	def __init__(self, title):
		super.__init__(title,id)
		self.__title = title
		self.__list_of_folders = []
		self.__list_of_docs_and_files = []

		numberic_id += 1
		id += str(numberic_id)

	def create_document_or_file(documents_and_files_folder, title, content, added_user, last_uploaded_date):
		pass
	def edit_document_or_file(document_or_file, attribute, value)
		pass
	def get_document_or_file():
		pass
	def save_document_or_file(document_or_file):
		pass

if __name__ == "main":
	sample_to_dos_topic = ToDosTopic("Sameple Todo Topic", "Sample Description")
	sample_to_do = ToDo("Sample Todo", "Sameple Content", datetime.now(), datetime.now(), "Thanaphat", "Nicharat", "Thanaphat")
	sample_document_or_file = DocumentOrFile("Sample Document or File", "Sample Content", "Thanaphat", datetime.now())
	sample_documents_and_files_folder = DocumentAndFilesFolder("Sample Folder Name")