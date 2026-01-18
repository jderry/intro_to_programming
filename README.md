# intro_to_programming
Datasets and other files for the Introduction to Programming for Researchers book and class, UT-Austin

For a reader using the book in independent study to gain a working knowledge of Linux and SciPy, I believe the hardest part is setting up or gaining access to a Linux machine. Depending on readers' circumstances, they may have different options:

1) Get access to a remote Linux server. If it provides web access via JupyterHub and has the standard SciPy libraries installed, then readers have access to everything they need to follow in the book;
2) Buy a machine with Linux installed, or with Linux available through emulation. The machine should have 4 cores and 8-16GB ram. Possible options include laptops, Raspberry Pi 5s, even Android tablets; and
3) Install a virtual hypervisor on a Mac or Windows machine with at least 4 cores and 8-16GB ram; then install an Ubuntu virtual machine. There are free hypervisors available: UTM for M* Macs and VirtualBox for Macs, Windows, and Linux machines. (This is the option most used in the class).

After accessing a Linux machine, readers should either install git client or verify that it's installed, then clone this intro_to_programming repo into their home directories, preferably in a subdirectory named "repo".

The folder "how_to_get_started" contains how-to guides on how to install an ubuntu virtual machine, and how to configure an ubuntu machine for class use, as well as for use in working through the book.
The folder "system_administration" contains text files that serve as both how-to guides and scripts for setting up Linux machines. This includes installing apps invoked in Linux statements in the book.
The folder "book_scripts_organized_by_chapter" contains the code found in the book, organized by chapter.
The folder "datafile" contains the datafiles used in the class and the book.
The folder "notebook" contains the Jupyter notebooks used in the class and the book.
