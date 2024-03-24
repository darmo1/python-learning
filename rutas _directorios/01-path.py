from pathlib import Path #nos ayuda a referenciar una ruta en la maquina (pc)

Path(r'C:\Archivos_de_programa\any')
Path('/user/bin') #este es para linux porque los servers estan corriendo en linux #esta es ruta absoluta y empieza con /
Path() #nos crea una ruta donde estamos parados o ubicados actualmente
Path('one/__init__.py') #aprovecha la carperta actual y le agrega /one/__init__.py esto se llama ruta relativa

path = Path('hola-mundo/mi-archivo-py')
path.is_file()
path.is_dir()

path.name()
path.stem() # da name mas extension
path.suffix() # da la extension 
path.parent()
path.absolute()

p = path.with_name('CHANCHITO.EXE') #Lo que hace es ayudarnos  cambiar el file name
p = path.with_suffix('something') 
p = path.with_stem('anyelse')


#working with dir
pathDir = Path('rutas')
pathDir.exists()
pathDir.mkdir()
pathDir.rmdir()

