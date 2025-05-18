# import os for accessing system resources
import os
# Object-oriented path manipulation that works across different operating systems
from pathlib import Path
# library call pyMupdf for read pdf content
import fitz #type: ignore

# the folder contening the pdf files to be rename
target = Path("/home/suman/Documents")

# going through the folder 
for item in target.iterdir():

    # filtering only pdfs from the folder
    if item.is_file() and item.suffix.lower() == ".pdf":
        try:
            # using fitz from/as pyMupdf to read the content of the pdf
            with fitz.open(item) as pdf_pages:

                # getting the first page of the pdf
                page = pdf_pages[0].get_text().strip().split("\n")

                if len(page) > 10:
                        
                    #storing the fullname of the student 
                    fullname = page[4].replace(" ","_")
                    # storing the registration number 
                    ug = page[10].replace("/","_")

                    # ensuring that filename is safe
                    safe_fullname = "".join(c for c in fullname if c.isalnum() or c in "_-")
                    safe_ug = "".join(c for c in ug if c.isalnum() or c in "-_")

                    # creating a new filename base on the fullname and registration number
                    new_filename = f"{safe_fullname}_{safe_ug}.pdf"
                    
                    # now let rename the file using pathlib in a modern way not using os

                    # get the exact path of the old filename
                    old_path = Path(target/item.name)
                    # create a new path for new name of the file
                    new_path = old_path.with_name(new_filename)

                    # check if there is file with the given name
                    if not(new_path.exists()):

                        # changin the filename base on the new path created
                        old_path.rename(new_path)

                        # tell user that the operation is done
                        print("filename change successfully")
                    else:
                        print("file with same name exist")
                else:
                    print("file have less number of lines")
            
        except Exception as e:
            print("Erro Processing {item.name}: {e}")
