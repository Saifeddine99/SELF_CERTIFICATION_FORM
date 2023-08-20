import os
import shutil
import subprocess
import uuid
from typing import List

from streamlit.components.v1 import html

from common1.exceptions import JavaProgramException
from common1.java_class import JavaClass


def try_remove(path: str) -> None:
    try:
        shutil.rmtree(path)
    except FileNotFoundError:
        pass


def create_tmp_sub_folder() -> str:
    """
    Creates a temporary sub folder under tmp

    :return:
    """
    if not os.path.exists("tmp"):
        os.mkdir("tmp")
    tmp_sub_folder_name = str(uuid.uuid4())[:8]
    tmp_sub_folder_path = os.path.join("tmp", tmp_sub_folder_name)
    os.mkdir(tmp_sub_folder_path)
    return tmp_sub_folder_path


def run_java_program(
        main_java_class: JavaClass,
        other_java_classes: List[JavaClass] = None
) -> str:
    """
    This method takes the given java classes, compiles them and runs :)

    :param main_java_class:
    :param other_java_classes:
    :return:
    """

    # Default java_classes is empty list
    if other_java_classes is None:
        other_java_classes = []

    # Create sub-folder under tmp folder for all the code
    tmp_sub_folder_path = create_tmp_sub_folder()

    # Save all the java classes under this folder
    for java_class in [main_java_class] + other_java_classes:
        java_class.save_class(tmp_sub_folder_path)
    tmp_sub_folder_java_files = os.path.join(tmp_sub_folder_path, "*.java")

    # Compile and run
    try:
        # Compile the program
        output = subprocess.run(f"javac {tmp_sub_folder_java_files}", capture_output=True, shell=True)
        if output.returncode != 0:
            raise JavaProgramException(
                f"לא הצלחנו לקמפל את הקוד שלך ... התקבלה השגיאה הבאה:",
                output.stderr.decode()
            )

        # Run the java program
        output = subprocess.run(
            f'cd "{tmp_sub_folder_path}" && java {main_java_class.class_name}',
            capture_output=True,
            shell=True
        )
        if output.returncode != 0:
            raise JavaProgramException(
                f"הייתה לך שגיאת זמן ריצה ... התקבלה השגיאה הבאה:",
                output.stderr.decode()
            )
    finally:
        try_remove(tmp_sub_folder_path)
    return output.stdout.decode()


def indent_menu():
    html(
        f"""
            <script id={uuid.uuid4()}>
                console.log("Including indentation script");

                function setIndentation() {{
                    console.log("Setting Indentation");
                    
                    // Get all side bar radio buttons
                    allRadios = window.parent.document.getElementsByTagName("label");
                    console.log("Found", allRadios.length, "radio buttons in total (some are irrelevant)");
                    for (let i = 0; i < allRadios.length; i++) {{
                        if(allRadios[i].getAttribute("data-baseweb") != "radio"){{
                            console.log("Skipping radio:", allRadios[i]);
                            continue;
                        }}
                        let radioDot =  allRadios[i].childNodes[0];
                        radioDot.style.display = "none";
                        
                        let radioContent = allRadios[i].childNodes[2];
                        radioContent.id = "menuRadioOption";
                        console.log("Handling radio:", radioContent);
                    
                        if(radioContent.innerHTML.startsWith("📄")) {{
                            console.log("Indenting page", radioContent.innerHTML);
                            radioContent.innerHTML = "&emsp;&emsp;&emsp;&emsp;" + radioContent.innerHTML;
                        }}
                        if(radioContent.innerHTML.startsWith("📂")) {{
                            console.log("Indenting directory", radioContent.innerHTML);
                            radioContent.innerHTML = "&emsp;&emsp;<b>" + radioContent.innerHTML + "</b>";
                        }}
                    }}
                }}

                // Set trigger for indentation script
                setIndentation();
            </script>
        """
    )


if __name__ == '__main__':
    run_java_program(
        "A",
        """
        class A {
            public static void main(String args[]){
                System.out.println("I am in Java Program");
            }
        }   
        """
    )