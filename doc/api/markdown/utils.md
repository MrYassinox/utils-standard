<!-- markdownlint-disable -->

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `utils`
Utils a standard toolkits for devlops.  

**Global Variables**
---------------
- **python**
- **platform_sys**
- **platform_arch**
- **platform_form**
- **platform_procs**
- **platform_pyth**
- **system**
- **current_working_dir**
- **root_path**
- **logger**

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L434"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_current_py_version`

```python
get_current_py_version(
    major: bool = True,
    minor: bool = True,
    micro: bool = True
) → str
```

Get the current Python version number info. 



**Args:**
 
 - <b>``major` (bool, optional)`</b>:  The current version major. Defaults to True. 
 - <b>``minor` (bool, optional)`</b>:  The current version minor. Defaults to True. 
 - <b>``micro` (bool, optional)`</b>:  The current version micro. Defaults to True. 



**Returns:**
 
 - <b>`str`</b>:  Returns version number. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L462"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_py_versions_available`

```python
get_py_versions_available() → None
```

Gets all Python versions available on the system. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L467"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `setup_temp`

```python
setup_temp(
    path: str = 'C:\\Users\\Mr Yassin NM\\Documents\\Develops\\GitHub\\utils-standard\\utils_standard'
) → str
```

Initialize a temporary folder path. 



**Args:**
 
 - <b>``path` (str, optional)`</b>:  The root path for the temporary folder.  Defaults to root_path. 



**Returns:**
 
 - <b>`str`</b>:  The path to the temporary folder. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L483"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `create_directory`

```python
create_directory(folder: str, exist_ok: bool = True) → str
```

Create a directory. 



**Args:**
 
 - <b>``folder` (str, optional)`</b>:  The name or path of the directory to create.  Defaults to None. 
 - <b>``exist_ok` (bool, optional)`</b>:  set to True, which avoids raising an error if the directory already exists. 



**Returns:**
 
 - <b>`str`</b>:  The path to the folder created. 



**Raises:**
 
 - <b>`Exception`</b>:  If no folder name is provided. 



**Notes:**

> - This function creates the directory using `os.makedirs`. - The `exist_ok` parameter is set to True, which avoids raising an error if the directory already exists. - If no folder name is provided, an exception is raised. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L509"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `clear`

```python
clear() → None
```

Clear the screen. 



**Notes:**

> - This function clears the screen for Windows using 'cls' command and for Mac and Linux using 'clear' command. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L525"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `remove_files_older`

```python
remove_files_older(
    path_dir: str,
    days_old: int = 0,
    logs: Optional[LoggerHandle] = None
) → None
```

Remove files that are older than specified days. 



**Args:**
 
 - <b>``path_dir` (str, optional)`</b>:  Path to the directory containing the files. 
 - <b>``days_old` (int, optional)`</b>:  Number of days old the files should be. Defaults to 0. 
 - <b>``logs` (Optional[LoggerHandle], optional)`</b>:  An instance of the `LoggerHandle` class for logging purposes. 



**Returns:**
 None 



**Example:**
 ```python
    # Remove files older than 7 days in the specified directory
    remove_files(days_old=7, path_dir='/path/to/directory')

    # Remove files older than 30 days in the current directory
    remove_files(days_old=30)
``` 



**Notes:**

> - This function checks the modified timestamp of each file in the specified directory. - If a file's timestamp is older than the specified number of days, it is removed. - The function logs the count of files found to be days old and the count of successfully removed files. - If the logs flag is set to True, the function logs additional debug messages for file removal. - The `logs` parameter is optional. If provided, it should be an instance of the `LoggerHandle` class for logging purposes. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L579"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_pkg_distribution`

```python
get_pkg_distribution(pkg: str = 'utils_dev') → Distribution
```

Get the distribution information for a package. 



**Args:**
 
 - <b>``pkg` (str, optional)`</b>:  The name of the package. Defaults to 'utils_dev'. 



**Returns:**
 
 - <b>`pkg_resources.Distribution`</b>:  The distribution information for the package. 



**Example:**
 ```python
    # Get the distribution information for a package
    distribution = get_pkg_distribution('utils_dev')

    # Print the package details
    print(distribution.project_name)
    print(distribution.version)
    print(distribution.location)
``` 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L603"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `os_environ_list`

```python
os_environ_list() → list
```

Return a list of environment variables. 



**Returns:**
 
 - <b>`list`</b>:  A list of tuples containing the environment variable name-value pairs. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L616"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `os_environ_set`

```python
os_environ_set(environ_name: str, environ_value=None) → None
```

Set an environment variable locally. 



**Args:**
 
 - <b>``environ_name` (str, optional)`</b>:  The name of the environment variable. 
 - <b>``environ_value` (Any, optional)`</b>:  The value to set for the environment variable.  Defaults to None. 



**Returns:**
 None 



**Example:**
 ```python
    # Set the 'PATH' environment variable to '/usr/bin'
    >>> os_environ_set('PATH', '/usr/bin')
``` 



**Notes:**

> - This function sets the environment variable locally. - It modifies the `os.environ` dictionary. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L640"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `os_environ_get`

```python
os_environ_get(environ_name: str) → str
```

Get the value of an environment variable. 



**Args:**
 
 - <b>``environ_name` (str, optional)`</b>:  The name of the environment variable. 



**Returns:**
 
 - <b>`str`</b>:  The value of the environment variable. 



**Example:**
 ```python
    # Get the value of the 'GIT_HOME' environment variable
    >>> os_environ_get('GIT_HOME')
    # Output: '/path/to/git'
``` 



**Notes:**

> - This function retrieves the value of the environment variable from the `os.environ` dictionary. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L663"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `module_exists`

```python
module_exists(
    module_name: str = None,
    logs: Optional[LoggerHandle] = None
) → bool
```

Check if a module exists. 



**Args:**
 
 - <b>``module_name` (str, optional)`</b>:  The name of the module. Defaults to None. 
 - <b>``logs` (Optional[LoggerHandle], optional)`</b>:  An instance of the `LoggerHandle` class for logging purposes. 



**Returns:**
 
 - <b>`bool`</b>:  True if the module exists, False otherwise. 



**Example:**
 ```python
    # Check if the module "math" exists
    exists1 = module_exists("math")
    print(exists1)  # Output: True

    # Check if the module "nonexistent_module" exists
    exists2 = module_exists("nonexistent_module")
    print(exists2)  # Output: False

    # Check if the module with no name exists
    exists3 = module_exists()
    print(exists3)  # Output: False
``` 



**Notes:**

> - This function uses `util.find_spec` to check if the module exists. - If the module is not found, a warning message is logged if the logs flag is set to True. - The `logs` parameter is optional. If provided, it should be an instance of the `LoggerHandle` class for logging purposes. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L701"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `run_shell_command`

```python
run_shell_command(
    command: str,
    shell: Optional[Literal['system', 'popen', 'subprocess']] = None
)
```

Run a shell command python and capture the output. 



**Args:**
 
 - <b>``command` (str)`</b>:  The command to run on shell. Example "-h" or "--help". 
 - <b>``shell` (Optional["system", "popen", "subprocess"], optional)`</b>:  The shell of to run command. Defaults to "system". 



**Returns:**
 
 - <b>`(str | None)`</b>:  if use shell `subprocess` Returns output as string else return none. 



**Notes:**

> - `system`:  This will run the command and return any output. - `popen`: This will run the command and not return any output. - `subprocess`: Can then process or display the output and returned as a string. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L741"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `sub_run`

```python
sub_run(
    command: str = None,
    desc: str = None,
    errdesc: str = None,
    logs: Optional[LoggerHandle] = None
) → str
```

Run a subprocess command and capture the output. 



**Args:**
 
 - <b>``command` (str, optional)`</b>:  The command to run. Defaults to None. 
 - <b>``desc` (str, optional)`</b>:  The description of the command. Defaults to None. 
 - <b>``errdesc` (str, optional)`</b>:  The error description. Defaults to None. 
 - <b>``logs` (Optional[LoggerHandle], optional)`</b>:  An instance of the `LoggerHandle` class for logging purposes. 



**Returns:**
 
 - <b>`str`</b>:  The captured stdout output. 



**Raises:**
 
 - <b>`RuntimeError`</b>:  If the command execution returns a non-zero return code. 



**Example:**
 ```python
    # Run a command and capture the output
    output = sub_run("ls -l", desc="Listing files")

    # Run a command and handle errors
    try:
         output = sub_run("some_invalid_command", desc="Running invalid command", errdesc="Error occurred")
    except RuntimeError as e:
         print(e)
``` 



**Notes:**

> - This function uses `subprocess.run` to execute the command. - If an error occurs during command execution, a `RuntimeError` is raised. - The `logs` parameter is optional. If provided, it should be an instance of the `LoggerHandle` class for logging purposes. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L790"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `check_run`

```python
check_run(command) → bool
```

Check if a command runs successfully. 



**Args:**
 
 - <b>``command` (str)`</b>:  The command to run. 



**Returns:**
 
 - <b>`bool`</b>:  True if the command runs successfully, False otherwise. 



**Notes:**

> - You can use this function by providing the desired command as a string to the command parameter. The function will execute the command using subprocess.run and capture the return code. If the return code is 0, it means the command ran successfully, and the function will return True. Otherwise, it will return False. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L810"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `run_python`

```python
run_python(command: str = None, desc: str = None, errdesc: str = None) → str
```

Run a Python command and capture the output. 



**Args:**
 
 - <b>``command` (str, optional)`</b>:  The Python command to run. Defaults to None. 
 - <b>``desc` (str, optional)`</b>:  Description of the command. Defaults to None. 
 - <b>``errdesc` (str, optional)`</b>:  Description of the error message. Defaults to None. 



**Returns:**
 
 - <b>`str`</b>:  The output of the `sub_run` function. 



**Example:**
 ```python
    # Run a Python command
    run_python('print("Hello, world!")', desc='Print a greeting')
    # Output: 'Hello, world!'
``` 



**Notes:**

> - This function uses the `sub_run` function to execute the Python command. - This function utilizes the sub_run function, passing the Python command to be executed as a shell command It captures the stdout output and returns it as a string To use this function, provide the Python command as a string to the command paramete You can also optionally provide a description for the command using the desc parameter and an error description using the errdesc parameter The function will execute the command and return the captured stdout output. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L839"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `sub_gitclone`

```python
sub_gitclone(
    url: str,
    targetdir: str = None,
    branch: str = None,
    logs: Optional[LoggerHandle] = None
) → None
```

Clone a Git repository from a given URL. 



**Args:**
 
 - <b>``url` (str)`</b>:  The URL of the Git repository. 
 - <b>``targetdir` (str, optional)`</b>:  The target directory to clone the repository into. Defaults to None. 
 - <b>``branch` (str, optional)`</b>:  The branch to clone. Defaults to None. 
 - <b>``logs` (bool, optional)`</b>:  Flag to determine whether to log the results. 



**Returns:**
 None 



**Raises:**
 
 - <b>`Exception`</b>:  If an error occurs during cloning or path manipulation. 



**Example:**
 ```python
    sub_gitclone('https://github.com/example/repo.git', targetdir='/path/to/destination', branch='main')
    sub_gitclone('https://github.com/example/repo.git', targetdir='myrepo', branch='main')
``` 



**Notes:**

> - This example will clone the Git repository from the given URL `(https://github.com/example/repo.git)` into the specified target directory `(/path/to/destination)` and checkout the `main` branch. - Make sure you have the git command-line tool installed and accessible in your environment for this function to work properly 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L890"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `repositories`

```python
repositories(
    cachDir: str = 'cachname',
    nameEnv: str = 'name',
    repoUrl: str = 'https://github.com/',
    branch: str = None,
    customDir: str = None,
    logs: Optional[LoggerHandle] = None
) → None
```

Manage repositories. 



**Args:**
 
 - <b>``cachDir` (str, optional)`</b>:  The cache directory name. Defaults to 'cachname'. 
 - <b>``nameEnv` (str, optional)`</b>:  The name of the environment variable. Defaults to 'name'. 
 - <b>``repoUrl` (str, optional)`</b>:  The URL of the repository. Defaults to 'https://github.com/'. 
 - <b>``branch` (str, optional)`</b>:  The branch to clone. Defaults to None. 
 - <b>``customDir` (str, optional)`</b>:  The custom directory to clone into. Defaults to None. 
 - <b>``logs` (Optional[LoggerHandle], optional)`</b>:  An instance of the `LoggerHandle` class for logging purposes. 



**Raises:**
 
 - <b>`Exception`</b>:  If an error occurs during cloning or path manipulation. 



**Notes:**

> - The `logs` parameter is optional. If provided, it should be an instance of the `LoggerHandle` class for logging purposes. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L952"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `sub_gitinstall`

```python
sub_gitinstall(module: str, logs: Optional[LoggerHandle] = None) → None
```

Install a Git module. 



**Args:**
 
 - <b>``module` (str)`</b>:  The module string to install. 
 - <b>``logs` (Optional[LoggerHandle], optional)`</b>:  An instance of the `LoggerHandle` class for logging purposes. 



**Returns:**
 None 



**Example:**
 ```python
    sub_gitinstall(module='your_module')
    sub_gitinstall('https://github.com/example/module.git', logs=True)
``` 



**Notes:**

> - Make sure to have `Git` installed and configured on your system for the function to work correctly. - The `logs` parameter is optional. If provided, it should be an instance of the `LoggerHandle` class for logging purposes. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L977"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `sub_wget`

```python
sub_wget(url: str, outputdir: str, logs: Optional[LoggerHandle] = None) → None
```

Download a file using wget. 



**Args:**
 
 - <b>``url` (str)`</b>:  The URL of the file to download. 
 - <b>``outputdir` (str)`</b>:  The output directory to save the file. 
 - <b>``logs` (Optional[LoggerHandle], optional)`</b>:  An instance of the `LoggerHandle` class for logging purposes. 



**Returns:**
 None 



**Example:**
 ```python
    sub_wget(url='your_url', outputdir='your_output_directory')
    sub_wget('https://example.com/file.zip', '/path/to/output', logs=True)
``` 



**Notes:**

> - Make sure to have the `wget` command-line tool installed and accessible in your system's PATH for the function to work correctly. - The `logs` parameter is optional. If provided, it should be an instance of the `LoggerHandle` class for logging purposes. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L1003"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `wget`

```python
wget(url: str, outputdir: str, logs: Optional[LoggerHandle] = None) → None
```

Download a file using wget. 



**Args:**
 
 - <b>``url` (str)`</b>:  The URL of the file to download. 
 - <b>``outputdir` (str)`</b>:  The output directory to save the file. 
 - <b>``logs` (Optional[LoggerHandle], optional)`</b>:  An instance of the `LoggerHandle` class for logging purposes. 



**Raises:**
 
 - <b>`Exception`</b>:  If an error occurs during cloning or path manipulation. 



**Example:**
 ```python
    wget(url='your_url', outputdir='your_output_directory')
``` 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L1042"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `requests_get`

```python
requests_get(
    url: str,
    outputdir: str = None,
    outputBytesIO: bool = False,
    stream: bool = False,
    logs: Optional[LoggerHandle] = None
)
```

Download a file using requests. 



**Args:**
 
 - <b>``url` (str)`</b>:  The URL of the file to download. 
 - <b>``outputdir` (str, optional)`</b>:  The output directory to save the file. Defaults to None. 
 - <b>``outputBytesIO` (bool, optional)`</b>:  Whether to return the file content as BytesIO. Defaults to False. 
 - <b>``stream` (bool, optional)`</b>:  By default, when you make a request, the body of the response is downloaded immediately.  You can override this behavior and defer downloading the response body until you access the `Response.content` 
 - <b>`attribute with the stream parameter`</b>: . Defaults to False. 
 - <b>``logs` (Optional[LoggerHandle], optional)`</b>:  An instance of the `LoggerHandle` class for logging purposes. 



**Returns:**
 
 - <b>`BytesIO`</b>:  The file content as BytesIO, if outputBytesIO is True. 



**Raises:**
 
 - <b>`Exception`</b>:  If an error occurs during request or path manipulation. 



**Example:**
 ```python
    requests_get(url='your_url', outputdir='your_output_directory', outputBytesIO=False)
``` 



**Notes:**

> - Note that connections are only released back to the pool for reuse once all body data has been read; be sure to either set stream to False or read the content property of the Response object - The `logs` parameter is optional. If provided, it should be an instance of the `LoggerHandle` class for logging purposes. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L1099"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_file_size`

```python
get_file_size(file_pathe: str, include_unit: bool = True) → str
```

Get the file size in bytes and convert it to bytes, KB, MB, GB, or TB. 



**Args:**
 
 - <b>``file_pathe` (str)`</b>:  The path to the file. 
 - <b>``include_unit` (bool)`</b>:  The include unit if false then return size by integer without unit. 



**Returns:**
 
 - <b>`str`</b>:  The file size with the corresponding unit. in bytes, KB, MB, GB, or TB. 



**Example:**
 ```python
    file_path = 'path_to_your_file'
    size = get_file_size(file_path)
    print(f"The size of {file_path} is: {size}")
``` 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L1130"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `check_file_size`

```python
check_file_size(foldersize: str, allowed_size: float) → bool
```

Check if the file size is less than or equal to the allowed size. 



**Args:**
 
 - <b>``foldersize` (str)`</b>:  The size of the file in the format "<size> <unit>" (e.g., "10.5 KB"). 
 - <b>``allowed_size` (float)`</b>:  The maximum allowed file size in megabytes (MB). 



**Returns:**
 
 - <b>`bool`</b>:  True if the file size is less than or equal to the allowed size, False otherwise. 



**Example:**
 ```python
    file_size = "10.5 KB"
    allowed_limit = 20.0  # Maximum allowed size in megabytes

    is_within_limit = check_file_size(file_size, allowed_limit)
    print(f"The file size is within the allowed limit: {is_within_limit}")
``` 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L1193"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `search_str`

```python
search_str(
    file_path: str,
    word: str,
    logs: Optional[LoggerHandle] = None
) → None
```

Search for a word in a file and print if it exists or not. 



**Args:**
 
 - <b>``file_path` (str)`</b>:  The path to the file. 
 - <b>``word` (str)`</b>:  The word to search for. 
 - <b>``logs` (Optional[LoggerHandle], optional)`</b>:  An instance of the `LoggerHandle` class for logging purposes. 



**Returns:**
 None 



**Raises:**
 
 - <b>`FileNotFoundError`</b>:  If the specified file does not exist. 



**Example:**
 ```python
    >>> search_str('file.txt', 'apple')
    # Output:
    # [apple] exists in the file.

    >>> search_str('file.txt', 'banana')
    # Output:
    # [banana] does not exist in the file.
``` 

This function searches for a specific word in a file. It opens the file specified by `file_path`, reads its content, and checks if the `word` is present in the file. If the word is found, it prints "[word] exists in the file.". Otherwise, it prints "[word] does not exist in the file.". 



**Notes:**

> - The function assumes the file is a text file and reads it in read-only mode. - The `logs` parameter is optional. If provided, it should be an instance of the `LoggerHandle` class for logging purposes. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L1241"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `search_str_by_line`

```python
search_str_by_line(
    file_path: str,
    word: str,
    logs: Optional[LoggerHandle] = None
) → None
```

Search for a word in each line of a file and print the line and line number if found. 



**Args:**
 
 - <b>``file_path` (str)`</b>:  The path to the file. 
 - <b>``word` (str)`</b>:  The word to search for. 
 - <b>``logs` (Optional[LoggerHandle], optional)`</b>:  An instance of the `LoggerHandle` class for logging purposes. 



**Returns:**
 None 



**Raises:**
 
 - <b>`FileNotFoundError`</b>:  If the specified file is not found. 



**Example:**
 ```python
    # Search for the word 'hello' in a file
    search_str_by_line('example.txt', 'hello')
    # Output:
    # [hello] exists in the file.
    # Line Number: 2
    # Line: This is a hello world example.
``` 



**Notes:**

> - This function reads each line of the file and checks if the specified word is present on each line. - The `logs` parameter is optional. If provided, it should be an instance of the `LoggerHandle` class for logging purposes. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L1288"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `search_and_replace`

```python
search_and_replace(
    file_path: str,
    word: str,
    replace: str = None,
    logs: Optional[LoggerHandle] = None
) → None
```

Search for a word in a file and optionally replace it with a new word. 



**Args:**
 
 - <b>``file_path` (str)`</b>:  The path to the file. 
 - <b>``word` (str)`</b>:  The word to search for. 
 - <b>``replace` (str, optional)`</b>:  The word to replace the found word with. Defaults to None. 
 - <b>``logs` (bool, optional)`</b>:  The Enable output logs. 



**Returns:**
 None 



**Raises:**
 
 - <b>`FileNotFoundError`</b>:  If the specified file is not found. 



**Example:**
 ```python
    # Search for the word 'hello' in a file and replace it with 'world'
    >>> search_and_replace('example.txt', 'hello', 'world')
    # Output:
    # [hello] exists in the file.
    # Replaced [hello] with [world] in the file.
``` 



**Notes:**

> - This function reads the content of the file, searches for the specified word, and replaces it if a replacement word is provided. - If the word is found in the file, it prints a message indicating its presence and, if specified, replaces it with the provided replacement word. - If the word is not found, it prints a message indicating its absence. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L1340"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `threading_manager_functions`

```python
threading_manager_functions(
    thread_name: str = None,
    function: object = None,
    args: Iterable = (),
    kwargs: Dict[str, Any] = None,
    daemon: bool = None,
    timer: bool = None,
    time: float = 1
) → Union[Thread, Timer, Exception]
```

Manage threading operations by creating and returning either a Thread or a Timer object. 



**Args:**
 
 - <b>``thread_name` (str, optional)`</b>:  The name of the thread. Defaults to None. 
 - <b>``function` (object, optional)`</b>:  The target function to be executed by the thread. Defaults to None. 
 - <b>``args` (Iterable, optional)`</b>:  The arguments to pass to the target function. Defaults to (). 
 - <b>``kwargs` (Dict[str, Any], optional)`</b>:  The keyword arguments to pass to the target function. Defaults to None. 
 - <b>``daemon` (bool, optional)`</b>:  Whether the thread is a daemon thread. Defaults to None. 
 - <b>``timer` (bool, optional)`</b>:  Whether to create a Timer object instead of a Thread object. Defaults to None. 
 - <b>``time` (float, optional)`</b>:  The time interval for the Timer object, in seconds. Defaults to 1. 



**Returns:**
 
 - <b>`Union[Thread, Timer, Exception]`</b>:  A Thread or Timer object, or an Exception if an error occurs. 



**Raises:**
 
 - <b>`Exception`</b>:  If an error occurs while creating the Thread or Timer object. 



**Example:**
 ```python
    def my_function():
         # Function code here
         pass

    # Example usage of threading_manager_functions() to create a Thread object
    >>> thread = threading_manager_functions(thread_name="MyThread", my_function, args=(arg1_value, arg2_value), kwargs={"arg1": value1, "arg2": value2}, daemon=True)
    >>> thread.start()

    # Example usage of threading_manager_functions() to create a Timer object
    >>> timer = threading_manager_functions(function=my_function, timer=True, time=5)
    >>> timer.start()
``` 



**Notes:**

> This function provides a convenient way to manage threading operations by creating either a Thread or a Timer object based on the specified parameters. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L1398"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `search_scanne_folder`

```python
search_scanne_folder(
    folder_path: str,
    ext_specific: Optional[List[str]] = None
) → Tuple[List[dict], int]
```

Scan a folder and return the list of files and other relevant information. 



**Args:**
 
 - <b>``folder_path` (str, optional)`</b>:  The folder path to scan.. 
 - <b>``ext_specific` (List[str], optional)`</b>:  List of specific file extensions to include. Defaults to None. 



**Returns:**
 
 - <b>`Tuple[List[dict], int]`</b>:  A tuple containing the list of dictionaries containing file information and the total file count. 



**Raises:**
 
 - <b>`FileNotFoundError`</b>:  If the specified folder is not found. 



**Example:**
 ```python
    folder_path = '/path/to/folder'
    extensions_list = ['.txt', '.csv', '.xlsx']
    files, total_count = scan_folder(folder_path, ext_specific=extensions_list)

    print(f"Total files: {total_count}")

    for file in files:
         print(file)
``` 



**Notes:**

> - This function scans the specified folder and retrieves information about each file in the folder, including the file path, name, size, and extension. - If a list of extensions is provided, only files with those extensions will be included in the result. If no extensions are provided, all files in the folder will be included. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L1457"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_data_from_csv_xlsx`

```python
get_data_from_csv_xlsx(
    filename: str = None,
    mode: str = 'r',
    insert_data: str = None,
    index: int = 0,
    col_csv: int = 0,
    skips_heading: bool = False
) → List[str]
```

Get data from a CSV or XLSX file and return it as a list. 



**Args:**
 
 - <b>``filename` (str, optional)`</b>:  The path to the file. Defaults to None. 
 - <b>``mode` (str, optional)`</b>:  The mode in which the file should be opened. Defaults to 'r'. 
 - <b>``insert_data` (str, optional)`</b>:  Data to be inserted at a specific index in the list. Defaults to None. 
 - <b>``index` (int, optional)`</b>:  The index at which the data should be inserted. Defaults to 0. 
 - <b>``col_csv` (int, optional)`</b>:  The column index to extract data from in case of a CSV file. Defaults to 0. 
 - <b>``skips_heading` (bool, optional)`</b>:  Whether to skip the heading in a CSV file. Defaults to False. 



**Returns:**
 
 - <b>`List[str]`</b>:  A list of items read from the file. 



**Raises:**
 
 - <b>`Exception`</b>:  If there is an error while processing the file. 



**Example:**
 ```python
    filename = 'data.csv'
    data = get_data_from_csv_xlsx(filename, mode='r', insert_data='Inserted Data', index=0, col_csv=0, skips_heading=True)
    print(data)
    # Output: ['Inserted Data', 'Value 1', 'Value 2', ...]
``` 



**Notes:**

> - This function reads data from a CSV or XLSX file and returns it as a list. - By default, it assumes that the file is a text file, where each line is an element in the list. - If the file extension is '.csv', it assumes a comma-separated values format and extracts data from the specified column index. - The optional `insert_data` parameter allows inserting additional data into the list at a specified index. - If an error occurs during file processing, an exception is raised. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L1522"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `edit_file_txt`

```python
edit_file_txt(
    filename: str,
    add_on_star: str = None,
    add_on_end: str = None,
    word_old: str = None,
    word_new: str = None,
    remove_duplicates: bool = False,
    splitlines: bool = True,
    overwrite_file: bool = True
) → None
```

Edit a text file by adding, replacing, or removing content. 



**Args:**
 
 - <b>``filename` (str)`</b>:  The path to the text file. 
 - <b>``add_on_star` (str, optional)`</b>:  The content to add at the start of each line. Defaults to None. 
 - <b>``add_on_end` (str, optional)`</b>:  The content to add at the end of each line. Defaults to None. 
 - <b>``word_old` (str, optional)`</b>:  The old word to replace. Defaults to None. 
 - <b>``word_new` (str, optional)`</b>:  The new word to replace the old word with. Defaults to None. 
 - <b>``remove_duplicates` (bool, optional)`</b>:  Whether to remove duplicate lines. Defaults to False. 
 - <b>``splitlines` (bool, optional)`</b>:  Whether to split the file into lines or keep it as a single string. Defaults to True. 
 - <b>``overwrite_file` (bool, optional)`</b>:  Whether to overwrite the original file or create a new file. Defaults to True. 



**Returns:**
 None 



**Raises:**
 
 - <b>`ValueError`</b>:  If remove_duplicates is True and overwrite_file is True. 



**Example:**
 ```python
    # Example usage of edit_file_txt()
    file_path = "path/to/file.txt"  # Replace with the path to your file

    # Add content at the start of each line
    edit_file_txt(file_path, add_on_star="* ")

    # Replace a word with a new word
    edit_file_txt(file_path, word_old="old", word_new="new")

    # Add content at the end of each line
    edit_file_txt(file_path, add_on_end=" [end]")

    # Remove duplicate lines
    edit_file_txt(file_path, remove_duplicates=True)

    # Split the file into lines
    edit_file_txt(file_path, splitlines=True)

    # Create a new file instead of overwriting the original file
    edit_file_txt(file_path, overwrite_file=False)
``` 



**Notes:**

> - This function edits a text file by adding, replacing, or removing content based on the provided arguments. - It can add text at the start or end of each line, replace words, and remove duplicate lines. - By default, the function splits lines when reading the file and overwrites the original file with the edited content. - If `remove_duplicates` is set to True, the function removes duplicate lines from the file. - If `overwrite_file` is set to False, a new file with the edited content is created instead of overwriting the original file. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L1657"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `temporary_file`

```python
temporary_file(
    bytes_data: bytes,
    suffix_ext: Optional[str] = 'test.txt',
    dir: Optional[str] = None,
    delete: bool = False
) → str
```

Create a temporary file and write the bytes data to it. 



**Args:**
 
 - <b>``bytes_data` (bytes)`</b>:  The bytes data to write to the temporary file. 
 - <b>``suffix_ext` (str, optional)`</b>:  The suffix or extension of the temporary file. Defaults to 'test.txt'. 
 - <b>``dir` (str, optional)`</b>:  The directory in which to create the temporary file. Defaults to None. 
 - <b>``delete` (bool, optional)`</b>:  Whether to delete the temporary file when closed. Defaults to False. 



**Returns:**
 
 - <b>`str`</b>:  The path of the temporary file that was created. 



**Raises:**
 
 - <b>`Exception`</b>:  If an error occurs during the creation of the temporary file. 



**Example:**
 ```python
    # Example usage of temporary_file()
    data = b"Hello, World!"  # Replace with your bytes data

    # Create a temporary file with the bytes data
    temp_file_path = temporary_file(data)

    # Access the path of the temporary file
    print("Temporary file path:", temp_file_path)

    # Example usage with custom suffix and directory
    data = b"Lorem ipsum dolor sit amet."

    # Create a temporary file with custom suffix and directory
    temp_file_path = temporary_file(data, suffix_ext=".bin", dir="/path/to/temp")

    # Access the path of the temporary file
    print("Temporary file path:", temp_file_path)
``` 



**Notes:**

> - This function creates a temporary file using the `NamedTemporaryFile` function from the `tempfile` module. - The `bytes_data` is written to the temporary file in binary mode. - The `suffix_ext` parameter allows specifying the suffix or extension of the temporary file. - The `dir` parameter specifies the directory where the temporary file will be created. If None, the default system directory is used. - The `delete` parameter determines whether the temporary file will be deleted when closed. If True, the file is automatically deleted. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L1711"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `search_and_edite_module`

```python
search_and_edite_module(
    object_defined: object,
    object_content_old: object = None,
    content_old: str = None,
    content_new: str = None,
    overwrite_file: bool = False,
    logs: Optional[LoggerHandle] = None
) → Any
```

Searches for a specified content in a module file and replaces it with new content. 



**Args:**
 
 - <b>``object_defined` (object)`</b>:  The object defined in the module. 
 - <b>``object_content_old` (object, optional)`</b>:  The object that contains the old content. Defaults to None. 
 - <b>``content_old` (str, optional)`</b>:  The old content to search for. Use this argument if object_content_old is not provided. Defaults to None. 
 - <b>``content_new` (str, optional)`</b>:  The new content to replace with. Defaults to None. 
 - <b>``overwrite_file` (bool, optional)`</b>:  Whether to overwrite the module file with the resulting data. Defaults to False. 
 - <b>``logs` (Optional[LoggerHandle], optional)`</b>:  An instance of the `LoggerHandle` class for logging purposes. 



**Returns:**
 None 



**Raises:**
 
 - <b>`ModuleNotFoundError`</b>:  If the module is not found. 



**Example:**
 ```python
    class MyClass:
         def __init__(self):
             self.value = 42

    # Search and replace content in the module
    search_and_edite_module(MyClass, content_old='value = 42', content_new='value = 50')
``` 



**Notes:**

> - This function searches for the specified content (old content) in the module file and replaces it with new content. - The content can be provided either through the `object_content_old` argument, which takes an object and extracts its source code, or directly through the `content_old` argument. - The `content_new` argument specifies the new content to replace the old content. - If `overwrite_file` is True, the original module file is overwritten with the resulting changes. Otherwise, a new file with the edits is created. - The encoding of the module file is automatically detected using the `chardet` library. - A backup file with the extension `.bak` is created before overwriting the original file. - The function returns True if the content was successfully replaced, and False otherwise. - If the module is not found, a `ModuleNotFoundError` is raised. - The `logs` parameter is optional. If provided, it should be an instance of the `LoggerHandle` class for logging purposes. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L1818"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `encode_file_bytes`

```python
encode_file_bytes(
    encoding_file: Optional[str, List[str], Tuple[str]] = None,
    file_output: bool = True,
    overwrite_file: bool = False
) → str
```

Encode a file into base64 and optionally write the encoded data to a file. 



**Args:**
 
 - <b>``encoding_file` (Optional[Union[str, List[str], Tuple[str]]])`</b>:  A path to a single file or a list of file paths to encode. 
 - <b>``file_output` (bool, optional)`</b>:  Flag to determine if the encoded data should be written to a file or returned as a list. 
 - <b>``overwrite_file` (bool, optional)`</b>:  Flag to determine if the existing file should be overwritten when saving the encoded data. 



**Returns:**
 
 - <b>`str`</b>:  A list of encoded file data if `file_output` is False. 



**Raises:**
 
 - <b>`FileNotFoundError`</b>:  If the specified file path is not found. 



**Example:**
 ```python
    # Replace the values of the arguments as per your requirement
    encoding_file = "path/to/file.txt"  # The path to the file to encode
    file_output = True  # Whether to write the encoded data to a file
    overwrite_file = False  # Whether to overwrite the output file if it already exists (applicable only when file_output is True)

    # Encode the file and optionally write the encoded data to a file
    encode_file_bytes(encoding_file, file_output, overwrite_file)

    # Example usage with multiple files
    # Replace the values of the arguments as per your requirement
    encoding_files = ["path/to/file1.txt", "path/to/file2.txt"]  # The paths to the files to encode

    # Encode the files and write the encoded data to separate files
    encode_file_bytes(encoding_files)

    # Example usage without file output
    # Replace the values of the arguments as per your requirement
    encoding_file = "path/to/file.txt"  # The path to the file to encode
    file_output = False  # Do not write the encoded data to a file

    # Encode the file and retrieve the encoded data as a string
    encoded_data = encode_file_bytes(encoding_file, file_output)

    # Check the encoded data
    print(encoded_data)
``` 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L1945"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `decode_file_bytes`

```python
decode_file_bytes(decode_file: bytes = None) → bytes
```

Decode a file encoded with base64. 



**Args:**
 
 - <b>``decode_file` (bytes)`</b>:  The file data encoded in base64. 



**Returns:**
 
 - <b>`bytes`</b>:  The decoded file content as bytes. 



**Example:**
 ```python
    # Replace the value of decode_file with the encoded file data as bytes
    decode_file = b'encoded_file_data'

    # Decode the file and retrieve the decoded content as bytes
    decoded_content = decode_file_bytes(decode_file)

    # Example usage with encoded file data stored in a variable
    # Replace the value of encoded_data with the encoded file data as bytes
    encoded_data = b'encoded_file_data'

    # Decode the file data and retrieve the decoded content as bytes
    decoded_content = decode_file_bytes(encoded_data)

    # Check the decoded content
    print(decoded_content)
``` 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L1979"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `detect_variable`

```python
detect_variable(arge: Any = None) → bool
```

Detect if the given argument is a function. 



**Args:**
 
 - <b>``arge` (Any)`</b>:  The variable to check. 



**Returns:**
 
 - <b>`bool`</b>:  True if the variable is a function, False otherwise. 



**Example:**
 ```python
    # Check if a variable is a function
    >>> detect_variable(print)
    # Output:
    # True
``` 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L2003"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `measuring_average_color_lightness`

```python
measuring_average_color_lightness(
    r: int = 0,
    g: int = 0,
    b: int = 0,
    factor: float = 0.1,
    measuring: Literal['Max', 'Average', 'Between', 'Geometric'] = None
) → Tuple[int, int, int]
```

Measure the average color lightness based on different methods. 



**Args:**
 
 - <b>``r` (int, optional)`</b>:  The red component of the color (default is 0). 
 - <b>``g` (int, optional)`</b>:  The green component of the color (default is 0). 
 - <b>``b` (int, optional)`</b>:  The blue component of the color (default is 0). 
 - <b>``factor` (float, optional)`</b>:  The scaling factor for lightness (default is 0.1). 
 - <b>``measuring` (Literal['Max', 'Average', 'Between', 'Geometric'], optional)`</b>:  The method to measure lightness.  Can be one of 'Max', 'Average', 'Between', 'Geometric'. Defaults to None. 



**Returns:**
 
 - <b>`Tuple[int, int, int]`</b>:  The RGB values of the resulting color. 



**Example:**
 ```python
    # Measure average color lightness using the 'Max' method
    >>> measuring_average_color_lightness(100, 150, 200, measuring='Max')
    # Output:
    # (100, 150, 200)

    # Measure average color lightness using the 'Average' method with a lightness factor of 0.2
    >>> measuring_average_color_lightness(100, 150, 200, factor=0.2, measuring='Average')
    # Output:
    # (96, 143, 191)
``` 



**Notes:**

> - This function calculates the average color lightness based on different methods: 'Max', 'Average', 'Between', 'Geometric'. - The resulting color is returned as RGB values. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L2072"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `wrapper_decorator_timetask`

```python
wrapper_decorator_timetask(
    suffix: str = 'Execution time seconds:',
    seconds: bool = True,
    logs: Optional[LoggerHandle] = None
)
```

Decorator function to measure the execution time of a given function. 



**Args:**
 
 - <b>``suffix` (str, optional)`</b>:  The suffix to be used in the output. Defaults to 'Execution time:'. 
 - <b>``seconds` (bool, optional)`</b>:  Whether to display the time in seconds or formatted time. Defaults to True. 
 - <b>``logs` (Optional[LoggerHandle], optional)`</b>:  An instance of the `LoggerHandle` class for logging purposes. 



**Returns:**
 
 - <b>`Callable[..., Any]`</b>:  The wrapper function that measures the execution time. 



**Example:**
 ```python
    # Define a function to be timed
    def my_function():
         time.sleep(1)
         print("Task complete")

    # Apply the time measurement decorator to the function
    @wrapper_decorator_timetask(suffix="Elapsed time:", seconds=False)
    def timed_function():
         my_function()

    # Call the timed function
    timed_function()
    # Output:
    # Task complete
    # Elapsed time: 00h:00m:01s
``` 



**Notes:**

> - The `logs` parameter is optional. If provided, it should be an instance of the `LoggerHandle` class for logging purposes. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L2135"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `wrapper_decorator`

```python
wrapper_decorator()
```

Decorator sample. 



**Returns:**
  The decorator function. 



**Notes:**

> - You can use this decorator by applying the `@wrapper_decorator` decorator above any function definition. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L2154"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `wrapper_decorator_threaded`

```python
wrapper_decorator_threaded(name_thread: str = None, daemon: bool = True)
```

Decorator to create threaded functions. 



**Args:**
 
 - <b>``name_thread` (str, optional)`</b>:  The name of the thread. Defaults to None. 
 - <b>``daemon` (bool, optional)`</b>:  Whether the thread should be a daemon thread. Defaults to True. 



**Returns:**
 
 - <b>`Callable[..., threading.Thread]`</b>:  The wrapper function that creates and starts the thread. 



**Example:**
 ```python
    # Apply the decorator to a function
    @wrapper_decorator_threaded(name_thread='my_thread', daemon=True)
    def my_function(delay: int, message: str):
         time.sleep(delay)
         return f"Threaded function: {message}"

    # Call the decorated function
    my_thread = my_function(3, "Hello, world!")

    # Wait for the thread to finish
    my_thread.join()

    # Get the result from the thread's result queue
    result = my_thread.result_queue.get() # <= for get result of function

    # Print the result
    print(result)
``` 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L2210"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `platform_system_detect`

```python
platform_system_detect() → Optional[str]
```

Detects the current platform or operating system. 



**Returns:**
 
 - <b>`Optional[str]`</b>:  The platform name. Can be one of the following: 
        - `'Windows'` for Windows systems. 
        - `'Mac'` for macOS systems. 
        - `'Linux'` for Linux systems. 
        - `'emscripten'` for emscripten platform. 
        - `None` if the platform cannot be determined. 



**Example:**
 ```python
    platform = platform_system_detect()
    print(platform)
    # Output: 'Windows' (if running on Windows)
``` 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L2242"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `split_file_path`

```python
split_file_path(file_path: str) → tuple[str, str, str]
```

Splits a file path into its directory name, base name, and extension. 



**Args:**
 
 - <b>``file_path` (str)`</b>:  The file path to split. 



**Returns:**
 
 - <b>`tuple[str, str, str]`</b>:  A tuple containing the directory name, base name, and extension of the file. 



**Raises:**
 
 - <b>`TypeError`</b>:  If the input argument `file` is not a string. 



**Example:**
 ```python
    dirname, basename, extension = split_file_path('/path/to/file.txt')
    print(dirname) # <= '/path/to'
    print(basename) # <= 'file'
    print(extension) # <= '.txt'
``` 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L2272"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_h_w_c_to_image`

```python
get_h_w_c_to_image(image_array: ndarray) → Tuple[int, int, int]
```

Returns the height, width, and number of channels of an image. 



**Args:**
 
 - <b>``image_array` (np.ndarray)`</b>:  The image array. 



**Returns:**
 
 - <b>`Tuple[int, int, int]`</b>:  A tuple containing the height, width, and number of channels of the image. 



**Raises:**
 
 - <b>`ValueError`</b>:  If the input array is not a valid image. 



**Example:**
 ```python
    image = np.zeros((100, 200, 3))  # Create a 100x200 RGB image
    height, width, channels = get_h_w_c_to_image(image)
    print(height)
    # Output: 100
    print(width)
    # Output: 200
    print(channels)
    # Output: 3
``` 



**Notes:**

> - This function assumes that the input array represents a valid image. - The height and width are obtained from the first two dimensions of the array shape. - If the array has a dimension of 2, it is treated as a grayscale image with one channel. - For color images, the number of channels is obtained from the third dimension of the array shape. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L2311"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_opencv_formats`

```python
get_opencv_formats() → list
```

Returns a list of available image file formats supported by OpenCV. 



**Returns:**
 
 - <b>`list`</b>:  A list of available image file formats. 



**Example:**
 ```python
    formats = get_opencv_formats()
    print(formats)
    [".bmp", ".dib", ".jpg", ".jpeg", ".jpe", ".jp2", ".png", ".webp", ".tif", ".tiff", ".pbm", ".pgm", ".ppm", ".pxm", ".pnm", ".sr", ".ras", ".exr", ".hdr", ".pic"]
``` 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L2356"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_pillow_formats`

```python
get_pillow_formats() → list
```

Returns a list of available image file formats supported by Pillow. 



**Returns:**
 
 - <b>`list`</b>:  A list of available image file formats. 



**Example:**
 ```python
    formats = get_pillow_formats()
    print(formats)
    [".bmp", ".dib", ".xbm", ".dds", ".eps", ".psd", ".gif", ".icns", ".ico", ".jpg", ".jpeg", ".jfif", ".jp2", ".jpx", ".msp", ".pcx", ".sgi", ".png", ".webp", ".tiff", ".tif", ".apng", ".pbm", ".pgm", ".ppm", ".pnm", ".tga"]
``` 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L2413"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `import_from`

```python
import_from(module: str, name: str)
```

Imports module from a file path. and returns an object from a specified module. 



**Args:**
 
 - <b>``module` (str)`</b>:  The module path. 
 - <b>``name` (str)`</b>:  The name of the object to import. 



**Returns:**
 
 - <b>`Any`</b>:  The imported object. 



**Example:**
 ```python
    path_file_module = "folder0.folder1.folder2.myfile.mymethod"
    name_function = "my_function"

    my_function = import_from(path_file_module, name_function)
    my_function()
``` 



**Notes:**

> - This function uses the `__import__` function to import the module dynamically. - The `fromlist` parameter is provided to ensure the specified name is included in the imported module. - The `getattr` function is used to retrieve the specified name from the imported module. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L2442"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `import_lib`

```python
import_lib(module_name: str, file_path: str) → object
```

Imports a module from a file path. 



**Args:**
 
 - <b>``module_name` (str)`</b>:  The name of the module. 
 - <b>``file_path` (str)`</b>:  The path to the module file. 



**Returns:**
 
 - <b>`object`</b>:  The imported module. 



**Raises:**
 
 - <b>`Exception`</b>:  If an error occurs during the import process. 



**Example:**
 ```python
    # Import the module "my_module" from the file "my_module.py"
    my_module = import_lib("my_module", "/path/to/my_module.py")
    my_module()
``` 



**Notes:**

> - This function uses the `util.spec_from_file_location` function to create a module specification based on the file path and desired module name. - The `util.module_from_spec` function is used to create a new module object from the module specification. - The `sys.modules` dictionary is updated with the newly created module object using the desired module name as the key. - The `exec_module` method of the module specification loader is called to execute the module and populate it with its contents. - The imported module object is returned. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L2480"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `retrieves_modules_from_dir`

```python
retrieves_modules_from_dir(
    directory_path: str = '',
    specific_file_name: Optional[str] = None,
    skip_file: Optional[List[str]] = None,
    skip_module: Optional[List[str]] = None,
    get_classes: bool = True,
    get_functions: bool = True
) → Union[Dict[str, type], Dict[str, <built-in function callable>], Tuple[Dict[str, type], Dict[str, <built-in function callable>]]]
```

Retrieves classes and/or functions from modules in a directory. 



**Args:**
 
 - <b>``directory_path` (str)`</b>:  The path to the directory containing the modules. 
 - <b>``specific_file_name` (str, optional)`</b>:  The name of a specific file to retrieve modules from. Use '*.py' to get all .py files. Defaults to None. 
 - <b>``skip_file` (List[str], optional)`</b>:  A list of files to skip. Defaults to None. 
 - <b>``skip_module` (List[str], optional)`</b>:  A list of modules to skip. Defaults to None. 
 - <b>``get_classes` (bool, optional)`</b>:  Whether to retrieve classes from the modules. Defaults to True. 
 - <b>``get_functions` (bool, optional)`</b>:  Whether to retrieve functions from the modules. Defaults to True. 



**Returns:**
 Union[Dict[str, type], Dict[str, callable], Tuple[Dict[str, type], Dict[str, callable]]]:  A dictionary of classes, a dictionary of functions, or a tuple containing both dictionaries. 



**Raises:**
 None. 



**Example:**
 ```python
    # Retrieve all classes from the modules in the specified directory
    classes = retrieves_modules_from_dir(directory_path='/path/to/modules_directory', get_classes=True, get_functions=False)

    # Retrieve all functions from the modules in the specified directory
    functions = retrieves_modules_from_dir(directory_path='/path/to/modules_directory', get_classes=False, get_functions=True)

    # Retrieve both classes and functions from the modules in the specified directory
    classes, functions = retrieves_modules_from_dir(directory_path='/path/to/modules_directory', get_classes=True, get_functions=True)
``` 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L2601"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `retrieves_image_from_dir`

```python
retrieves_image_from_dir(
    directory_path: str,
    pattern_extensions: Optional[List[str]] = None,
    return_names: bool = True,
    return_paths: bool = False
) → Union[List[str], Tuple[List[str], List[str]]]
```

Retrieves image names or paths from a directory. 



**Args:**
 
 - <b>``directory_path` (str)`</b>:  The path to the directory containing the images. 
 - <b>``pattern_extensions` (List[str], optional)`</b>:  A list of file extensions to filter the images. Defaults to None. 
 - <b>``return_names` (bool, optional)`</b>:  Whether to return image names. Defaults to True. 
 - <b>``return_paths` (bool, optional)`</b>:  Whether to return image paths. Defaults to False. 



**Returns:**
 Union[List[str], List[str], Tuple[List[str], List[str]]]:  A list of image names, a list of image paths, or a tuple containing both lists. 



**Raises:**
 None. 



**Example:**
 ```python
    # Retrieve image names from the directory
    image_names = retrieves_image_from_dir(directory_path='/path/to/images_directory', return_names=True, return_paths=False)

    # Retrieve image paths from the directory
    image_paths = retrieves_image_from_dir(directory_path='/path/to/images_directory', return_names=False, return_paths=True)

    # Retrieve both image paths and names from the directory
    image_paths, image_names = retrieves_image_from_dir(directory_path='/path/to/images_directory', return_names=True, return_paths=True)
``` 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L2660"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `safe_exception_execute`

```python
safe_exception_execute(
    exception: Union[Any, Tuple[Any]] = <class 'Exception'>,
    default: Any = None,
    target: Optional[Any] = None,
    args: List[Any] = [],
    kwargs: Optional[Dict[Any, Any]] = None
) → Any
```

Executes a target function or action safely, catching specified exceptions and returning a default value or the exception itself. 



**Args:**
 
 - <b>``exception` (Union[Any, Tuple[Any]])`</b>:  The exception or tuple of exceptions to catch. 
 - <b>``default` (Any, optional)`</b>:  The default value to return if an exception is caught. Defaults to None. 
 - <b>``target` (Optional[Any], optional)`</b>:  The function or action to execute. Defaults to None. 
 - <b>``args` (List[Any], optional)`</b>:  The arguments to pass to the target function. Defaults to []. 
 - <b>``kwargs` (Optional[Dict[Any, Any]], optional)`</b>:  The keyword arguments to pass to the target function. Defaults to None. 



**Returns:**
 
 - <b>`Any`</b>:  The result of the target function or the default value if an exception is caught. 



**Raises:**
 
 - <b>`Exception`</b>:  If the target function raises an exception and no default value is provided. 



**Example:**
 ```python
    # Example 1: Safely execute a function and return the result or a default value
    result = safe_exception_execute(exception=ZeroDivisionError, default=0, target=lambda: 10 / 0)

    # Example 2: Safely execute a function with arguments and return the result or a default value
    result = safe_exception_execute(exception=FileNotFoundError, default='Not found', target=open, args=['nonexistent.txt'], kwargs={'mode': 'r'})

    # Example 3: Safely execute a function and raise the caught exception if no default value is provided
    result = safe_exception_execute(exception=KeyError, target=lambda: my_dict['key'])
``` 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L2716"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_list_parameter_names_from_fun`

```python
get_list_parameter_names_from_fun(
    func_or_method: Any,
    method_py2: bool = False
) → Union[FullArgSpec, Signature]
```

Retrieves a list of parameter names from a Python function, method, or class. 



**Args:**
 
 - <b>``func_or_method` (Any)`</b>:  The function, method, or class to inspect. 
 - <b>``method_py2` (bool, optional)`</b>:  Flag indicating whether to use Python 2 or Python 3 method for retrieval. Defaults to False (Python 3). 



**Returns:**
 
 - <b>`Union[inspect.FullArgSpec, inspect.Signature]`</b>:  The parameter information retrieved from the function, method, or class. 



**Raises:**
 
 - <b>`TypeError`</b>:  If the provided object is not a function, method, or class. 



**Example:**
 ```python
    # Example 1: Get parameter names from a function
    def my_function(param1, param2, param3='default'):
         pass

    parameters = get_list_parameter_names_from_fun(my_function)
    print(parameters)  # Output: (['param1', 'param2', 'param3'], None, None, ('default',))

    # Example 2: Get parameter names from a method
    class MyClass:
         def my_method(self, param1, param2):
             pass

    instance = MyClass()
    parameters = get_list_parameter_names_from_fun(instance.my_method)
    print(parameters)  # Output: (['self', 'param1', 'param2'], None, None, None)

    # Example 3: Get parameter names from a class
    class MyClass:
         def __init__(self, param1, param2):
             pass

    parameters = get_list_parameter_names_from_fun(MyClass)
    print(parameters)  # Output: (['self', 'param1', 'param2'], None, None, None)
``` 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L2766"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `checked_instances`

```python
checked_instances(
    inspecter: Any,
    type_checker: Literal['function', 'method', 'class', 'code', 'object', 'list', 'int', 'str', 'bool', 'none'] = 'str',
    logs: Optional[LoggerHandle] = None
) → bool
```

Checks the type of the provided object against the specified type checker. 



**Args:**
 
 - <b>``inspecter` (Any)`</b>:  The object to check the type of. `type_checker` (Literal['function', 'method', 'class', 'code', 'object', 'list', 'int', 'str', 'bool', 'none'], optional):  The type checker to use. Defaults to 'str'. 
 - <b>``logs` (Optional[LoggerHandle], optional)`</b>:  An instance of the `LoggerHandle` class for logging purposes. 



**Returns:**
 
 - <b>`bool`</b>:  True if the object matches the specified type checker, False otherwise. 



**Raises:**
 
 - <b>`Exception`</b>:  If an error occurs during type checking. 



**Example:**
 ```python
    # Example 1: Check if an object is a function
    def my_function():
         pass

    is_function = checked_instances(my_function, type_checker='function')
    print(is_function)  # Output: True

    # Example 2: Check if an object is a method
    class MyClass:
         def my_method(self):
             pass

    instance = MyClass()
    is_method = checked_instances(instance.my_method, type_checker='method')
    print(is_method)  # Output: True

    # Example 3: Check if an object is a class
    class MyClass:
         pass

    is_class = checked_instances(MyClass, type_checker='class')
    print(is_class)  # Output: True

    # Example 4: Check if an object is a code object
    code = compile('print("Hello")', '<string>', 'exec')
    is_code = checked_instances(code, type_checker='code')
    print(is_code)  # Output: True

    # Example 5: Check if an object is a list
    my_list = [1, 2, 3]
    is_list = checked_instances(my_list, type_checker='list')
    print(is_list)  # Output: True

    # Example 6: Check if an object is an integer
    my_int = 10
    is_int = checked_instances(my_int, type_checker='int')
    print(is_int)  # Output: True

    # Example 7: Check if an object is a string
    my_str = "Hello"
    is_str = checked_instances(my_str, type_checker='str')
    print(is_str)  # Output: True

    # Example 8: Check if an object is a boolean
    my_bool = True
    is_bool = checked_instances(my_bool, type_checker='bool')
    print(is_bool)  # Output: True

    # Example 9: Check if an object is None
    my_none = None
    is_none = checked_instances(my_none, type_checker='none')
    print(is_none)  # Output: True
``` 



**Notes:**

> - The `logs` parameter is optional. If provided, it should be an instance of the `LoggerHandle` class for logging purposes. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L2868"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `strTobool`

```python
strTobool(val: str)
```

Convert a string representation to an actual boolean value. 



**Args:**
 
 - <b>``val` (str)`</b>:  The string value to convert. 



**Returns:**
 
 - <b>`bool`</b>:  The boolean value corresponding to the string representation. 



**Raises:**
 
 - <b>`ValueError`</b>:  If the input string is not a valid truth value. 



**Example:**
 ```python
    value1 = strTobool("True")
    print(value1)  # Output: True

    value2 = strTobool("yes")
    print(value2)  # Output: True

    value9 = strTobool("invalid")
    # Output: ValueError: invalid truth value invalid
``` 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L2901"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `create_archive_tar_gz`

```python
create_archive_tar_gz(
    archive_name: Optional[str],
    source_paths: Optional[str, list],
    output_path: Optional[str] = None,
    logs: Optional[LoggerHandle] = None
) → None
```

Create a tar.gz archive containing specified files and directories. 



**Args:**
 
 - <b>``archive_name` (Optional[str])`</b>:  The name of the output archive file with extension `name.tar.gz`. 
 - <b>``output_path` (Optional[str])`</b>:  The path of the output archive file. Defaults to None. 
 - <b>``source_paths` (Optional[Union[str, list]])`</b>:  A string or list of strings representing the paths of files or directories  to be included in the archive. Each string can be a file path or a directory path. 
 - <b>``logs` (Optional[LoggerHandle], optional)`</b>:  An instance of the `LoggerHandle` class for logging purposes. 



**Returns:**
 None 



**Raises:**
 
 - <b>`Exception`</b>:  If any of the specified paths does not exist. 



**Example:**
 ```python
    source_paths = "folder1"
    archive_name = "archive.tar.gz"
    create_tar_gz(archive_name, source_paths)

    # or list.

    source_paths = [
         "file1.txt",
         "folder1",
         "folder2/file2.txt"
    ]
    archive_name = "archive.tar.gz"
    create_tar_gz(archive_name, source_paths)

    # The archive 'archive.tar.gz' should be created successfully,
    # containing the 'squardot_utils_contrib.egg-info' folder and its contents.
``` 



**Notes:**

> - If the source_paths parameter is a string, it adds the individual file or directory to the archive. - If the source_paths parameter is a list, it adds multiple files or directories to the archive. - The archive file will be compressed using the tar.gz format. - The `logs` parameter is optional. If provided, it should be an instance of the `LoggerHandle` class for logging purposes. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\.environment\lib\site-packages\loguru\_logger.py#L2977"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `check_signature_object`

```python
check_signature_object(
    func: Callable,
    logs: Optional[LoggerHandle] = None
) → None
```

introspect function parameters. 



**Args:**
 
 - <b>``func` (Callable)`</b>:  The function for check signature parameters. 
 - <b>``logs` (Optional[LoggerHandle], optional)`</b>:  An instance of the LoggerHandle class for logging. 



**Raises:**
 
 - <b>`ValueError`</b>:  has no signature 



**Returns:**
 None 



**Example:**
 ```python
    def foo(a:str, b:int, t:bool=None, **kwargs):
         pass

    check_signature_object(foo)
    # Output
    # Signature foo: (a: str, b: int, t: bool = None, **kwargs)
    # position: 0 name: a          kind=positional_or_keyword | default=required | annotation=<class 'str'>
    # position: 1 name: b          kind=positional_or_keyword | default=required | annotation=<class 'int'>
    # position: 2 name: t          kind=positional_or_keyword | default=None | annotation=<class 'bool'>
    # position: 3 name: kwargs     kind=variadic_keyword | default=required | annotation=<empty>
``` 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L3017"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `check_string_match_pattern`

```python
check_string_match_pattern(
    string: str,
    pattern: str,
    lower_character: bool = None
)
```

Check if the characters in the string match the pattern. 



**Args:**
 
 - <b>``string` (str)`</b>:  The string to be checked. 
 - <b>``pattern` (str)`</b>:  The pattern to be matched. 
 - <b>``lower_character` (bool)`</b>:  Whether to match the pattern in lowercase. 



**Returns:**
 
 - <b>`boolen`</b>:  if True the first characters in the string match the pattern, False otherwise. 



**Example:**
 ```python
    string = "mana"
    sequence = "na"

    if check_string_match_pattern(string, sequence):
         print("ok")
    else:
         raise ValueError("The first characters of the string do not match the sequence")
``` 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L3049"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_string_before_pattern`

```python
get_string_before_pattern(string: str, pattern: str = None)
```

Get the string before the specified character pattern in the string. 



**Args:**
 
 - <b>``string` (str)`</b>:  The string to be processed. 
 - <b>``pattern` (str)`</b>:  The character pattern to be matched   The specified character the first occurrence of the string. 



**Returns:**
 
 - <b>`str`</b>:  The string before the pattern, or the entire string if the pattern is not found. 



**Example:**
 ```python
    string = "TEN_K_ROUNDED"
    pattern = "_"
    result = get_string_before_pattern(string, pattern)
    print(result) # Output => TEN
``` 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L3076"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `time_sleep_accuracy`

```python
time_sleep_accuracy(
    sleep_time: Union[int, float],
    measuring_time: Optional[Literal['monotonic', 'performance']] = None
)
```

The time sleep duration with higher accuracy. 



**Args:**
 
 - <b>``sleep_time` (Union[int, float])`</b>:  The seconds duration of sleep. 
 - <b>``measuring_time` (Union[str, None])`</b>:  The measuring time intervals calculation you can choice "monotonic", "performance". 



**Returns:**
 None. 



**Notes:**

> - `performance`: The it calculates measuring time intervals value (in fractional seconds) of a clock with the highest available resolution on the system. - This is suitable for measuring short durations and is primarily used for performance benchmarking and timing operations. - The value returned is based on the system's monotonic clock but may include fractions of a second for higher precision. - It can be affected by system clock adjustments, such as time adjustments made by the user or network time synchronization. 
>- `monotonic`: It returns the value (in fractional seconds) of a clock that cannot go backward and is unaffected by system clock adjustments. - This is intended for measuring elapsed time between two points, independent of the system clock. - It's useful for tasks such as measuring timeouts, calculating durations, or synchronizing activities. - The value returned does not represent an actual date or time; it's only a relative measure of time. - It guarantees monotonically increasing values, ensuring that it never goes backward even if the system clock is adjusted. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L3113"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `check_is_matching_pattern`

```python
check_is_matching_pattern(
    sequence_string: str,
    pattern: Union[str, List],
    operator: Literal['search', 'findall'] = 'search'
)
```

Check if any of the patterns match the characters or strings. 



**Args:**
 
 - <b>``sequence_string` (str)`</b>:  The input string to be to check for matches. 
 - <b>``pattern` (Union[str, List])`</b>:  The pattern to match or a list of regular expression patterns to   match has an 'r' prefix (indicating it is a raw string). 
 - <b>``operator` (Literal["search", "findall"])`</b>:  The check operator the way to check matching   if use `"search"` returns boolen for first result, or use `"findall"` to returns list for an found all result. 



**Returns:**
 
 - <b>`(bool | list | None)`</b>:  if use "search" returns boolen, or use "findall" to returns list 



**Example:**
 ```python

    # DESC => You can use list patterns with has an 'r' prefix (indicating it is a raw string).
    patterns = [r"\d+", r"[a-z]+"] # DESC => This list contains two patterns: digits and lowercase letters.
    input_string = "abc123xyz"

    if check_is_matching_pattern(input_string, patterns):
         print("Pattern matched in the input string.")
    else:
         print("No match found in the input string.")

    # DESC => You can use a list patterns in string with has an 'r' prefix (indicating it is a raw string).
    patterns = r"\d+|[a-z]+"
    input_string = "abc123xyz"

    if check_is_matching_pattern(input_string, patterns):
         print("Pattern matched in the input string.")
    else:
         print("No match found in the input string.")

    # DESC => You can use patterns a string with has an 'r' prefix (indicating it is a raw string).
    patterns = r"quick.*fox"
    input_string = "The quick brown fox jumps over the lazy dog."
    
    if check_is_matching_pattern(input_string, patterns):
         print("Pattern matched in the input string.")
    else:
         print("No match found in the input string.")

    # DESC => You can use patterns a string without has an 'r' prefix (indicating it is a raw string).
    patterns = "hello"
    input_string = "Hello, world!"
    
    if check_is_matching_pattern(input_string, patterns):
         print("Pattern matched in the input string.")
    else:
         print("No match found in the input string.")

    # DESC => You can use operator "findall" with patterns a string without has an 'r' prefix (indicating it is a raw string).
    patterns = "hello"
    input_string = "Hello, world!"
    
    check = check_is_matching_pattern(input_string, patterns, operator="findall")
    if check:
         print(check) # output => ["hello"]
    else:
         print(check)

    # DESC => ou can use operator "findall" with patterns a string has an 'r' prefix (indicating it is a raw string).
    patterns = r"name|hi"
    input_string = "Hello, world!"
    
    check = check_is_matching_pattern(input_string, patterns, operator="findall")
    if check:
         print(check)
    else:
         print(check) # output => []
``` 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L99"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `LoggerHandle`
LoggerHandle functionality and exception handling in applications. 

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L101"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    file_handles: bool = False,
    rotation: str = '10 MB',
    retention: str = '5 days',
    context: str = None,
    *args,
    **kwargs
)
```

LoggerHandle functionality and exception handling in applications. 

LoggerHandle is a lightweight logging class that wraps the Loguru library, offering easy-to-use logging functionality and exception handling in applications. 



**Args:**
 
 - <b>``file_handles` (bool)`</b>:  A flag indicating whether to open a file for writing logs. 
 - <b>``rotation` (str, optional)`</b>:  The rotation interval for log files. Automatically rotate too big file Examples: `"10 KB"`, `"100 MB"`, `"0.5 GB"`, `"1 month 2 weeks"`, `"4 days"`, `"10h"` `"10s"`.  Defaults to "10 MB". 
 - <b>``retention` (str, optional)`</b>:  The rotation interval for log files. Cleanup after some time. Examples `"1 month 2 weeks"`, `"4 days"`, `"10h"` `"10s"`  Defaults to "10 days". 
 - <b>``context` (str, optional)`</b>:  Custom context to be added to each logged message record.  Defaults to None.  



**Notes:**

> - LoggerHandle is a lightweight logging class that wraps the Loguru library, offering easy-to-use logging functionality and exception handling in applications. 




---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L149"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `catch`

```python
catch(
    exception: Optional[Tuple[BaseException]] = <class 'Exception'>,
    level: Union[str, int] = 'ERROR',
    reraise: Optional[bool] = False,
    onerror: Optional[<built-in function callable>] = <function LoggerHandle.<lambda> at 0x000001A517BA6EE0>,
    exclude: Optional[BaseException, Tuple[BaseException]] = (),
    default: Optional[str] = None,
    message: Optional[str] = "An error has been caught in function '{record[function]}', process '{record[process].name}' ({record[process].id}), thread '{record[thread].name}' ({record[thread].id}):"
)
```

Catch an exception and log it with the 'exception' level. 



**Args:**
 
 - <b>``exception` (Optional[Tuple[BaseException]], optional)`</b>:  The type of exception to intercept. If several types should be caught, a tuple of exceptions can be used too..  Defaults to Exception. 
 - <b>``level` (Union[str, int], optional)`</b>:  The level name or severity with which the message should be logged. 
 - <b>`List name Level`</b>:  ['`TRACE`', '`DEBUG`', '`INFO`', '`SUCCESS`', '`WARNING`', '`ERROR`', '`CRITICAL`']. Defaults to 'ERROR'. 
 - <b>``reraise` (Optional[bool], optional)`</b>:  Whether the exception should be raised again and hence propagated to the caller.  Defaults to False. 
 - <b>``onerror` (Optional[callable], optional)`</b>:  A function that will be called if an error occurs, once the message has been logged. It should accept the exception instance as it sole argument..  Defaults to None. 
 - <b>``exclude` (Optional[Exception], optional)`</b>:  A function that will be called if an error occurs, once the message has been logged. It should accept the exception instance as it sole argument..  Defaults to None. 
 - <b>``default` (Optional[str], optional)`</b>:  The value to be returned by the decorated function if an error occurred without being re-raised.  Defaults to None. 
 - <b>``message` (_type_, optional)`</b>:  The message that will be automatically logged if an exception occurs. 
 - <b>`Defaults to "An error has been caught in function '{record[function]}', process '{record[process].name}' ({record[process].id}), thread '{record[thread].name}' ({record[thread].id})`</b>: ". 



**Returns:**
 
 - <b>`Callable`</b>:  A decorator that can be used to wrap a function and log any caught exceptions.  Return a decorator to automatically log possibly caught error in wrapped function. 



**Example:**
 ```python
    logger = LoggerHandle()
    @logger.catch()
    def my_function():
         ...
``` 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L377"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `critical`

```python
critical(message: Optional[str], **kwargs: Any) → None
```

Log a message with the 'CRITICAL' level. 



**Args:**
 
 - <b>``message` (Optional[str])`</b>:  The logged message. 
 - <b>``**kwargs` (Optional[Any])`</b>:  This is used to add custom context to each logging call message record. 



**Returns:**
 None 



**Example:**
 ```python
    logger = LoggerHandle()
    logger.critical("That's it, beautiful and simple logging!")
    # Output
    # That's it, beautiful and simple logging!

    logger.critical("That's it, beautiful and simple logging! {extra}", extra="record message.")
    # Output
    # That's it, beautiful and simple logging! record message.
``` 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L247"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `debug`

```python
debug(message: Optional[str], **kwargs: Any) → None
```

Log a message with the 'DEBUG' level. 



**Args:**
 
 - <b>``message` (Optional[str])`</b>:  The logged message. 
 - <b>``**kwargs` (Optional[Any])`</b>:  This is used to add custom context to each logging call message record. 



**Returns:**
 None 



**Example:**
 ```python
    logger = LoggerHandle()
    logger.debug("That's it, beautiful and simple logging!")
    # Output
    # That's it, beautiful and simple logging!

    logger.debug("That's it, beautiful and simple logging! {extra}", extra="record message.")
    # Output
    # That's it, beautiful and simple logging! record message.
``` 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L351"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `error`

```python
error(message: Optional[str], **kwargs: Any) → None
```

Log a message with the 'ERROR' level. 



**Args:**
 
 - <b>``message` (Optional[str])`</b>:  The logged message. 
 - <b>``**kwargs` (Optional[Any])`</b>:  This is used to add custom context to each logging call message record. 



**Returns:**
 None 



**Example:**
 ```python
    logger = LoggerHandle()
    logger.error("That's it, beautiful and simple logging!")
    # Output
    # That's it, beautiful and simple logging!

    logger.error("That's it, beautiful and simple logging! {extra}", extra="record message.")
    # Output
    # That's it, beautiful and simple logging! record message.
``` 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L404"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `exception`

```python
exception(message: Optional[str], **kwargs: Any) → None
```

Log a message with the 'CRITICAL' level. 



**Args:**
 
 - <b>``message` (Optional[str])`</b>:  The logged message. 
 - <b>``**kwargs` (Optional[Any])`</b>:  This is used to add custom context to each logging call message record. 



**Returns:**
 None 



**Example:**
 ```python
    logger = LoggerHandle()
    logger.exception("That's it, beautiful and simple logging!")
    # Output
    # That's it, beautiful and simple logging!

    logger.exception("That's it, beautiful and simple logging! {extra}", extra="record message.")
    # Output
    # That's it, beautiful and simple logging! record message.
``` 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L273"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `info`

```python
info(message: Optional[str], **kwargs: Any) → None
```

Log a message with the 'INFO' level. 



**Args:**
 
 - <b>``message` (Optional[str])`</b>:  The logged message. 
 - <b>`*`*kwargs` (Optional[Any])`</b>:  This is used to add custom context to each logging call message record. 



**Returns:**
 None 



**Example:**
 ```python
    logger = LoggerHandle()
    logger.info("That's it, beautiful and simple logging!")
    # Output
    # That's it, beautiful and simple logging!

    logger.info("That's it, beautiful and simple logging! {extra}", extra="record message.")
    # Output
    # That's it, beautiful and simple logging! record message.
``` 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L190"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `log`

```python
log(level: Union[str, int], message: Optional[str], **kwargs: Any) → None
```

Log a message with the specified level. 



**Args:**
 
 - <b>``level` (Union[str, int])`</b>:  Level name ['`TRACE`', '`DEBUG`', '`INFO`', '`SUCCESS`', '`WARNING`', '`ERROR`', '`CRITICAL`'].  Level severity value ['`5`', '`10`', '`20`', '`25`', '`30`', '`40`', '`50`']. 
 - <b>``message` (Optional[str])`</b>:  The logged message. 
 - <b>``**kwargs` (Optional[Any])`</b>:  This is used to add custom context to each logging call message record. 



**Returns:**
 None 



**Example:**
 ```python
    logger = LoggerHandle()
    logger.log("That's it, beautiful and simple logging!")
    # Output
    # That's it, beautiful and simple logging!

    logger.log("That's it, beautiful and simple logging! {extra}", extra="record message.")
    # Output
    # That's it, beautiful and simple logging! record message.
``` 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L299"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `success`

```python
success(message: Optional[str], **kwargs: Any) → None
```

Log a message with the 'INFO' level. 



**Args:**
 
 - <b>``message` (Optional[str])`</b>:  The logged message. 
 - <b>``**kwargs` (Optional[Any])`</b>:  This is used to add custom context to each logging call message record. 



**Returns:**
 None 



**Example:**
 ```python
    logger = LoggerHandle()
    logger.success("That's it, beautiful and simple logging!")
    # Output
    # That's it, beautiful and simple logging!

    logger.success("That's it, beautiful and simple logging! {extra}", extra="record message.")
    # Output
    # That's it, beautiful and simple logging! record message.
``` 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L221"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `trace`

```python
trace(message: Optional[str], **kwargs: Any) → None
```

Log a message with the 'TRACE' level. 



**Args:**
 
 - <b>``message` (Optional[str])`</b>:  The logged message. 
 - <b>``**kwargs` (Optional[Any])`</b>:  This is used to add custom context to each logging call message record. 



**Returns:**
 None 



**Example:**
 ```python
    logger = LoggerHandle()
    logger.trace("That's it, beautiful and simple logging!")
    # Output
    # That's it, beautiful and simple logging!

    logger.trace("That's it, beautiful and simple logging! {extra}", extra="record message.")
    # Output
    # That's it, beautiful and simple logging! record message.
``` 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L325"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `warning`

```python
warning(message: Optional[str], **kwargs: Any) → None
```

Log a message with the 'WARNING' level. 



**Args:**
 
 - <b>``message` (Optional[str])`</b>:  The logged message. 
 - <b>``**kwargs` (Optional[Any])`</b>:  This is used to add custom context to each logging call message record. 



**Returns:**
 None 



**Example:**
 ```python
    logger = LoggerHandle()
    logger.warning("That's it, beautiful and simple logging!")
    # Output
    # That's it, beautiful and simple logging!

    logger.warning("That's it, beautiful and simple logging! {extra}", extra="record message.")
    # Output
    # That's it, beautiful and simple logging! record message.
``` 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L3213"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `TaskTimer`
Task Execution Timer.  

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L3215"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(*args, **kwargs)
```

Initialize the TaskTimer object.  




---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L3230"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `end_time`

```python
end_time()
```

End the timer for task execution. 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L3236"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `finishe`

```python
finishe(
    suffix: str = 'Task Execution Time:',
    seconds: bool = True,
    logs: Optional[LoggerHandle] = None
) → str
```

Calculate and return the task execution time. 



**Args:**
 
 - <b>``suffix` (str, optional)`</b>:  The suffix to prepend to the output. Defaults to 'Task Execution Time:'. 
 - <b>``seconds` (bool, optional)`</b>:  Whether to return the time in seconds or formatted time. Defaults to True. 
 - <b>``logs` (Optional[LoggerHandle], optional)`</b>:  An instance of the `LoggerHandle` class for logging purposes. 



**Returns:**
 
 - <b>`str`</b>:  The task execution time. 



**Example:**
 ```python
    timer = TaskTimer()
    timer.start_time()
    time.sleep(2)
    timer.end_time()
    print(timer.finishe())  # Output: Task Execution Time: 2.0 seconds
``` 



**Notes:**

> - The `logs` parameter is optional. If provided, it should be an instance of the `LoggerHandle` class for logging purposes. 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L3224"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `start_time`

```python
start_time()
```

Start the timer for task execution. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L3276"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Threaded`
Threaded  

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L3278"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    name_thread: str = '',
    target_function: Any = None,
    args: list = (),
    kwargs: dict = None,
    daemon: bool = True,
    logs: Optional[LoggerHandle] = None
)
```

Initialize the Threaded object. 



**Args:**
 
 - <b>``name_thread` (str, optional)`</b>:  The name of the thread. Defaults to an empty string. 
 - <b>``target_function` (Any, optional)`</b>:  The target function to execute in the thread. Defaults to None. 
 - <b>``args` (list, optional)`</b>:  The arguments to pass to the target function. Defaults to an empty list. 
 - <b>``kwargs` (dict, optional)`</b>:  The keyword arguments to pass to the target function. Defaults to None. 
 - <b>``daemon` (bool, optional)`</b>:  Whether the thread is a daemon thread or not. Defaults to True. 
 - <b>``logs` (Optional[LoggerHandle], optional)`</b>:  An instance of the `LoggerHandle` class for logging purposes. 



**Example:**
 ```python
    def task_function(a, b, param):
         # Perform some task
         pass

    thread = Threaded(name_thread='MyThread', target_function=task_function, args=(1, 2), kwargs={'param': 'value'})
    thread.start()
    print(thread.status())  # Output: (True, 'Thread is running..')
    thread.join()
    print(thread.get_results())  # Output: <thread results>
``` 



**Notes:**

> - The `logs` parameter is optional. If provided, it should be an instance of the `LoggerHandle` class for logging purposes. 


---

#### <kbd>property</kbd> daemon

A boolean value indicating whether this thread is a daemon thread. 

This must be set before start() is called, otherwise RuntimeError is raised. Its initial value is inherited from the creating thread; the main thread is not a daemon thread and therefore all threads created in the main thread default to daemon = False. 

The entire Python program exits when only daemon threads are left. 

---

#### <kbd>property</kbd> ident

Thread identifier of this thread or None if it has not been started. 

This is a nonzero integer. See the get_ident() function. Thread identifiers may be recycled when a thread exits and another thread is created. The identifier is available even after the thread has exited. 

---

#### <kbd>property</kbd> name

A string used for identification purposes only. 

It has no semantics. Multiple threads may be given the same name. The initial name is set by the constructor. 

---

#### <kbd>property</kbd> native_id

Native integral thread ID of this thread, or None if it has not been started. 

This is a non-negative integer. See the get_native_id() function. This represents the Thread ID as reported by the kernel. 



---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L3363"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_results`

```python
get_results()
```

Get the results of the thread execution. 



**Returns:**
 
 - <b>`Any`</b>:  The results of the thread execution. 



**Example:**
 ```python
    thread = Threaded()
    thread.start()
    thread.join()
    print(thread.get_results())  # Output: <thread results>
``` 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L3317"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `join`

```python
join()
```

Wait for the thread to complete. 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L3311"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run()
```

Run the thread and execute the target function. 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L3321"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `status`

```python
status() → bool
```

Check the status of the thread.  



**Returns:**
 
 - <b>`bool`</b>:  The status value. 



**Example:**
 ```python
    thread = Threaded()
    thread.start()
    print(thread.status())  # Output: (True, 'Thread is running..')
    thread.join()
    print(thread.status())  # Output: (False, 'Thread is finished.')
``` 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L3343"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `stop`

```python
stop()
```

Set the stop event to stop the thread. 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L3347"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `stopped`

```python
stopped()
```

Check if the thread has stopped. 



**Returns:**
 
 - <b>`bool`</b>:  True if the thread has stopped, False otherwise. 



**Example:**
 ```python
    thread = Threaded()
    thread.start()
    thread.stop()
    print(thread.stopped())  # Output: True
``` 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L3382"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ColorsConstants`
Provide RGB color constants and a colors dictionary with elements formatted.  

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L3384"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__()
```

Initialize the ColorsConstants object. 



**Returns:**
  None 



**Example:**
 ```python

     constants = ColorsConstants()
     thread.start()
     thread.join()
     print(thread.get_results())  # Output: <thread results>
``` 



**Notes:**

> - [colors constants perview](../data/colors_constants.md) 




---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L4545"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `colors_hex`

```python
colors_hex() → dict
```

Return a dictionary of color variables in hexadecimal format. 



**Returns:**
 
 - <b>`dict{str`</b>:  str}: A dictionary containing color variables in hexadecimal format. 



**Example:**
 ```python
    colors = ColorsConstants()
    hex_colors = colors.colors_hex()
    print(hex_colors)  # Output: {'ALICEBLUE': '#F0F8FF', ...}
``` 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L5118"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `colors_rgb`

```python
colors_rgb() → dict
```

Return a dictionary of color variables in RGB format. 



**Returns:**
 
 - <b>`dict{str`</b>:  tuple}: A dictionary containing color variables in RGB format. 



**Example:**
 ```python
    colors = ColorsConstants()
    rgb_colors = colors.colors_rgb()
    print(rgb_colors)  # Output: {'ALICEBLUE': (240, 248, 255), ...}
``` 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L5691"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `colors_rgb_name`

```python
colors_rgb_name() → dict
```

Return a dictionary of color variables in RGB format with color names as keys. 



**Returns:**
 
 - <b>`dict`</b>:  A dictionary containing color variables in RGB format with color names as keys. 



**Example:**
 ```python
    colors = ColorsConstants()
    rgb_colors = colors.colors_rgb_name()
    print(rgb_colors)  # Output: {'ALICEBLUE': RGB(red=240, green=248, blue=255), ...}
``` 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L3405"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `keys_hex`

```python
keys_hex() → str
```

Return of color constants variables in hexadecimal format. 



**Returns:**
 
 - <b>`str`</b>:  variables keys. 



**Example:**
 ```python
    colors = ColorsConstants()
    hex_keys = colors.keys_hex().AQUA
    print(hex_keys)  # Output: #00FFFF
``` 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L3975"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `keys_rgb`

```python
keys_rgb() → tuple
```

Return of color constants variables in RGB format. 



**Returns:**
 
 - <b>`tuple[str, str, str]`</b>:  variables keys. 



**Example:**
 ```python
    colors = ColorsConstants()
    rgb_keys = colors.keys_rgb().ALICEBLUE
    print(rgb_keys)  # Output: (240, 248, 255)
``` 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L6300"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ColorsConvartor`
Color converter class for different color formats. 

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L6302"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__()
```

Initialize the ColorsConvartor object.  






---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L6307"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `cmyk_to_rgb`

```python
cmyk_to_rgb(
    cyan: float = 0,
    magenta: float = 0,
    yellow: float = 0,
    black: float = 0
)
```

Convert CMYK color to RGB format. 



**Args:**
 
 - <b>``cyan` (float, optional)`</b>:  Cyan component (0-100). Defaults to 0. 
 - <b>``magenta` (float, optional)`</b>:  Magenta component (0-100). Defaults to 0. 
 - <b>``yellow` (float, optional)`</b>:  Yellow component (0-100). Defaults to 0. 
 - <b>``black` (float, optional)`</b>:  Black component (0-100). Defaults to 0. 



**Returns:**
 
 - <b>`tuple`</b>:  RGB color tuple (red, green, blue). 



**Example:**
 ```python
    converter = ColorsConverter()
    rgb = converter.cmyk_to_rgb(cyan=50, magenta=30, yellow=10, black=0)
    print(rgb)  # Output: (159, 191, 217)
``` 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L6387"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `hex_to_rgb`

```python
hex_to_rgb(hex)
```

Convert hexadecimal color to RGB format. 



**Args:**
 
 - <b>``hex_value` (str)`</b>:  Color in hexadecimal format. 



**Returns:**
 
 - <b>`tuple`</b>:  RGB color tuple (red, green, blue). 



**Example:**
 ```python
    converter = ColorsConverter()
    rgb = converter.hex_to_rgb('#9FBFD9')
    print(rgb)  # Output: (159, 191, 217)
``` 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L6428"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `hls_to_rgb`

```python
hls_to_rgb(hue: float = 0, lightness: float = 0, saturation: float = 0)
```

Convert HLS color to RGB format. 



**Args:**
 
 - <b>``hue` (float, optional)`</b>:  Hue component (0-1). 
 - <b>``lightness` (float, optional)`</b>:  Hue component (0-1). 
 - <b>``saturation` (float, optional)`</b>:  Saturation component (0-1). 



**Returns:**
 
 - <b>`tuple`</b>:  RGB color tuple (red, green, blue). 



**Example:**
 ```python
    converter = ColorsConverter()
    rgb = converter.hls_to_rgb(hue=0.58, lightness=0.669, saturation=0.389)
    print(rgb)  # Output: (159, 191, 217)
``` 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L6334"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `rgb_to_cmyk`

```python
rgb_to_cmyk(red: int = 0, green: int = 0, blue: int = 0)
```

Convert RGB color to CMYK format. 



**Args:**
 
 - <b>``red` (int, optional)`</b>:  Red component (0-255). 
 - <b>``green` (int, optional)`</b>:  Green component (0-255). 
 - <b>``blue` (int, optional)`</b>:  Blue component (0-255). 



**Returns:**
 
 - <b>`tuple`</b>:  CMYK color tuple (cyan, magenta, yellow, black). 



**Example:**
 ```python
    converter = ColorsConverter()
    cmyk = converter.rgb_to_cmyk(red=159, green=191, blue=217)
    print(cmyk)  # Output: (26.667, 12.084, 0.0, 15.686)
``` 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L6367"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `rgb_to_hex`

```python
rgb_to_hex(red: int = 0, green: int = 0, blue: int = 0)
```

Convert RGB color to hexadecimal format. 



**Args:**
 
 - <b>``red` (int, optional)`</b>:  Red component (0-255). 
 - <b>``green` (int, optional)`</b>:  Green component (0-255). 
 - <b>``blue` (int, optional)`</b>:  Blue component (0-255). 



**Returns:**
 
 - <b>`str`</b>:  Color in hexadecimal format. 



**Example:**
 ```python
    converter = ColorsConverter()
    hex_value = converter.rgb_to_hex(red=159, green=191, blue=217)
    print(hex_value)  # Output: '#9FBFD9'
``` 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L6407"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `rgb_to_hls`

```python
rgb_to_hls(red: int = 0, green: int = 0, blue: int = 0)
```

Convert RGB color to HLS format. 



**Args:**
 
 - <b>``red` (int, optional)`</b>:  Red component (0-255). 
 - <b>``green` (int, optional)`</b>:  Green component (0-255). 
 - <b>``blue` (int, optional)`</b>:  Blue component (0-255). 



**Returns:**
 
 - <b>`tuple`</b>:  HLS color tuple (hue, lightness, saturation). 



**Example:**
 ```python
    converter = ColorsConverter()
    hls = converter.rgb_to_hls(red=159, green=191, blue=217)
    print(hls)  # Output: (0.58, 0.669, 0.389)
``` 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L6449"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Promise`
A simplified implementation of promises in Python. 

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L6451"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(executor: Callable[[Callable, Callable], NoneType]) → None
```

Initializes a new Promise object. 



**Args:**
  `executor` (Callable[[Callable[[Any], None], Callable[[Exception], None]], None]):  A function that takes two arguments, `resolve` and `reject`.  It performs an asynchronous operation and calls `resolve` with the result  or `reject` with an error if the operation fails. 

**Example:**
 ```python
     def async_operation(name: str):
         try:
             return name
         except Exception as error:
             raise error

     # Create a new promise using the executor() method
     promise = Promise.executor(function=async_operation, args=['name'])
     # Attach callback functions using then and catch
     promise.then(lambda result: print("Promise resolved with result:", result)).catch(lambda error: print("Promise rejected with error:", error))
``` 



**Notes:**

> - This implementation of promises follows a simplified approach and may not cover all the features of full-fledged promise libraries. - Promises can be useful for handling asynchronous operations and managing their outcomes in a more structured manner. 




---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L6544"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `catch`

```python
catch(on_rejected: Callable[[Exception], NoneType]) → Promise
```

Attaches a callback function to the promise for rejection. 



**Args:**
  `on_rejected` (Callable[[Exception], None]):  A function that takes the rejected error as an argument and handles the error. 



**Returns:**
 
 - <b>`Promise`</b>:  The Promise object itself. 



**Example:**
 ```python
    # Example usage of the catch() method
    promise.catch(lambda error: print("Promise rejected with error:", error))
``` 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L6568"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `executor`

```python
executor(function: Callable[, Any], args: tuple) → Promise
```

Creates a new promise using an executor function. 



**Args:**
 
 - <b>``function` (Callable)`</b>:  The function to execute asynchronously 
 - <b>``args` (tuple)`</b>:  The arguments to pass to the function. 



**Returns:**
 
 - <b>`Promise`</b>:  A Promise instance that represents the asynchronous operation. 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L6520"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `then`

```python
then(on_fulfilled: Callable[[Any], NoneType]) → Promise
```

Attaches a callback function to the promise for fulfillment. 



**Args:**
  `on_fulfilled` (Callable[[Any], None]):  A function that takes the fulfilled value as an argument and performs further actions. 



**Returns:**
 
 - <b>`Promise`</b>:  A new Promise object. 



**Example:**
 ```python
    # Example usage of the then() method
    promise.then(lambda result: print("Promise resolved with result:", result))
``` 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L6591"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ExceptionsBase`
Class that defines variables for built-in exceptions derived from BaseException. 



**Notes:**

> - Access the exception classes directly using the class name followed by the exception variable name. For example, EXCEPTIONS.BASE_EXCEPTION represents the BaseException class. - Exception variables can be used for handling specific exception types or for type hinting purposes. 
>

**Example:**
 ```python
     try:
         # Some code that may raise an exception
     except EXCEPTIONS.ZERO_DIVISION_ERROR as e:
         # Handle ZeroDivisionError

     def my_function() -> EXCEPTIONS.TYPE_ERROR:
         # Function annotation indicating that the return type should be TypeError
``` 





---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L6825"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Argparse`
Argparse - Extended Argument Parser for Command-Line Argument Handling.  

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L6827"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    prog: Optional[str, Any] = None,
    usage: Optional[str] = None,
    description: Optional[str] = None,
    epilog: Optional[str] = None,
    prefix_chars: Optional[str] = '-',
    argument_default=None,
    conflict_handler: Optional[str] = 'error',
    add_help: bool = True,
    allow_abbrev: bool = True,
    exit_on_error: bool = True
)
```

Initialize the Argparse object. 



**Args:**
 
 - <b>``prog` (Optional[Union[str, Any]], optional)`</b>:  The name of the program.  Defaults to sys.argv[0]. Example ('myprogram') 
 - <b>``usage` (Optional[str], optional)`</b>:  A usage to customize the usage message that is displayed.  Defaults to None to auto-generated from arguments. Example (`'%(prog)s [options] <input>'`) 
 - <b>``description` (Optional[str], optional)`</b>:  A description of what the program does.  Defaults to None. 
 - <b>``epilog` (Optional[str], optional)`</b>:  Text following the argument descriptions.  to add additional text at the end of the help message.  Defaults to None. Example ('Additional information goes here') 
 - <b>``prefix_chars` (Optional[str], optional)`</b>:  By default, argparse recognizes options  with either a single dash (`-`) or double dash (`--`) prefix. Defaults to '-'. 
 - <b>``argument_default` (_type_, optional)`</b>:  The default value for all arguments.  Defaults to None. 
 - <b>``conflict_handler` (Optional[str], optional)`</b>:  String indicating how to handle conflicts.  Defaults to 'error'. 
 - <b>``add_help` (bool, optional)`</b>:  Add automatically adds a `-h` / `--help` option  to display the help message. Defaults to True. 
 - <b>``allow_abbrev` (bool, optional)`</b>:  By default, allows long option names abbreviations.  Setting to False disables this behavior, requiring users to provide the full option names. Defaults to True. 
 - <b>``exit_on_error` (bool, optional)`</b>:  Determines whether or not ArgumentParser exits.  with error info when an error occurs. Defaults to True. 



**Example:**
 ```python
    >>> parser = Argparse()
    >>> parser.add_args('name', help_message='Path to the input file')
    >>> parser.add_args('-f', '--file', help_message='Path to the input file')
    >>> args = parser.get_args_namespace()
    >>> print(args.name, args.file)
    >>> python script.py jone --file 'file/file1'
    # Output => jone file/file1

    >>> args = parser.get_args_dictionary()
    >>> print(args['name'], args['file'])
    # Output => jone file/file1

    # Example to demonstrate the usage of pramater nargs:
    >>> parser = Argparse()
    >>> parser.add_args('--files', nargs='+', help='Specify input files')
    >>> python script.py --files file1.txt file2.txt
    >>> args = parser.get_args_namespace()
    >>> if args.files:
    >>>     print(f'Input files: {args.files}')
    # Output => Input files: file1.txt
    # Output => Input files: file2.txt
``` 



**Notes:**

> - This class extends the `ArgumentParser` class from the `argparse` module and provides additional functionality for handling command-line arguments. 




---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L6897"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `add_args`

```python
add_args(
    *name_or_flags: str,
    arg_type: Optional[str, int, float, bool, <built-in function dir>, FileType] = Ellipsis,
    choices: Optional[Iterable] = None,
    action: Optional[str] = Ellipsis,
    default: Optional[Any] = Ellipsis,
    nargs: Optional[int, Literal['?', '*', '+']] = None,
    help_message: str = None
)
```

Add command-line arguments to the argument group. 



**Args:**
 
 - <b>``name_or_flags` (tuple[str, ...])`</b>: The name or flags for the argument.  You can use positional Example (`'name'`) or optional arguments   Example (`'-h'`, `'--help'`). 


 - <b>``arg_type` (Optional[Union[str, int, float, bool]], optional)`</b>:  Automatically convert an argument   to the given type of input Here's a list 
 - <b>``str` (default)`</b>:  Accepts any string value. 
 - <b>``int``</b>:  Accepts an integer value. 
 - <b>``float``</b>:  Accepts a floating-point value. 
 - <b>``bool``</b>:  Accepts a boolean value.  This type is typically used for flags or options that don't require a value. 
 - <b>``dir``</b>:  Accepts a directory path. 
 - <b>``argparse.FileType``</b>:  Accepts a file path.  It can automatically open the file for reading or writing, depending on  
 - <b>`the specified mode ex`</b>:  (`argparse.FileType('r')`). 


 - <b>``choices` (Optional[Iterable], optional)`</b>:  The should a list, tuple, set, of acceptable  choices for the argument. Accepts one of the specified choices.  ex choices=['a', 'b', 'c']. 


 - <b>``action` (Optional[str], optional)`</b>:  The action to be taken when the argument is encountered.  Here's a list of commonly used action types 
 - <b>``'store'` (default)`</b>:  Stores the value specified for the argument.  This is the default action if no action is specified. 
 - <b>``'store_const`'`</b>:  Stores a constant value specified  by the const parameter when the argument is encountered. 
 - <b>``'store_true'`/`'store_false'``</b>:  Stores True or False respectively when  the argument is encountered. These actions are typically used for boolean flags. 
 - <b>``'append'``</b>:  Appends the value specified for the argument to a list.  This allows you to collect multiple occurrences of the argument. 
 - <b>``'append_const'``</b>:  Appends a constant value specified by the const parameter  to a list when the argument is encountered. 
 - <b>``'count'``</b>:  Counts the number of times the argument is encountered  and stores the count. 
 - <b>``'help'``</b>:  Displays the help message and exits the program. 


 - <b>``default` (Optional[Any], optional)`</b>:  The default value for the argument.  you can set default values for command-line arguments  Here's a list of ways to specify default values. 


 - <b>``nargs` (Optional[Any], optional)`</b>:  The allows you to specify the number of command line arguments.  that should be consumed for a given option. Here are some possible values 
 - <b>``None` (default)`</b>:  This is the default value when nargs is not specified explicitly.  It means that a single command-line argument is expected for the option. 
 - <b>``'?'``</b>:  Specifies that the option should match zero or one command-line argument.  If the option is not provided, the default value for the option will be used. 
 - <b>``'*'``</b>:  Allows zero or more command-line arguments for the option.  All the arguments will be collected into a list. 
 - <b>``'+'``</b>:  Requires one or more command-line arguments for the option.  Like *, the arguments will be collected into a list. 
 - <b>``int``</b>:  Allows a specific number of command-line arguments to be consumed.  For example, nargs=3 means that three arguments are required for the option. 
 - <b>``argparse.REMAINDER``</b>:  Collects all the remaining command-line arguments into a list,  regardless of their number. 


 - <b>``help_message` (str, optional)`</b>:  The help message for the argument you can provide.  help messages for command-line arguments on how to use your script. 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L6990"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_args_dictionary`

```python
get_args_dictionary()
```

Parse the command-line arguments and return a dictionary. 



**Returns:**
 
 - <b>`dict`</b>:  The parsed command-line arguments as a dictionary. 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L6980"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_args_namespace`

```python
get_args_namespace()
```

Parse the command-line arguments and return the namespace. 



**Returns:**
 
 - <b>`Namespace`</b>:  The parsed command-line arguments as a namespace. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L7000"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `EventsSignature`
EventsSignature class. 

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L7002"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__()
```

Initialize the EventsSignature object. 

The EventsSignature class is used to set and get attributes, and signature the callback object function and init event. 

Methods:  `setattribute(attribute_name: str, value: Any)`:   Sets the named attribute of the object to the specified value.  `getattribute(attribute_name: str)`:   Get a named attribute from object.  `signature_obj_and_init_callback(callback: Callable, init_event: Any = None)`:   Signature of callback the object function and init event. 



**Example:**
 ```python
     >>> EVENTS = EventsSignature()
     >>> EVENTS.setattribute("init", None)
     >>> print(EVENTS.getattribute("init"))
     # Output.
     # None

     >>> EVENTS.setattribute("index", 100)
     >>> print(EVENTS.getattribute("index"))
     # Output.
     # 100

     >>> EVENTS.setattribute("name", "flet")
     >>> print(EVENTS.name))
     # Output.
     # flet

     >>> expression = lambda e: print(e.data)
     >>> EVENTS.setattribute("data", "flet")
     >>> EVENTS.signature_obj_and_init_callback(expression, init_event=EVENTS)
     # Output.
     # flet
``` 




---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L7056"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `getattribute`

```python
getattribute(attribute_name: str)
```

Get a named attribute from object. 



**Args:**
 
 - <b>``attribute_name` (str)`</b>:  The name of the attribute. 



**Returns:**
 
 - <b>`value`</b>:  the value of attribute. 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L7043"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `setattribute`

```python
setattribute(attribute_name: str, value: Any)
```

Sets the named attribute of the object to the specified value. 



**Args:**
 
 - <b>``attribute_name` (str)`</b>:  The name of the attribute. 
 - <b>``value` (Any)`</b>:  The value of the attribute. 



**Returns:**
 None 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L7068"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `signature_obj_and_init_callback`

```python
signature_obj_and_init_callback(callback: Callable, init_event: Any = None)
```

Signature of callback the object function and init event. 



**Args:**
 
 - <b>``callback` (Callable)`</b>:  The represent any callable object, such as a function,  a method, or a lambda expression. 
 - <b>``event` (Any, EventsSignature)`</b>:  The send Events data to callback object. Defaults to None. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L7089"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AxisCalc`
Calculate the top, bottom, right, and left coordinates of an object based on its axis. 

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L7091"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    local_x: Union[int, float] = None,
    local_y: Union[int, float] = None,
    global_x: Union[int, float] = None,
    global_y: Union[int, float] = None
)
```

Initialize the AxisCalc object. 



**Args:**
 
 - <b>``local_x` (Union[int, float])`</b>:  The axis local x-coordinate of the object. 
 - <b>``local_y` (Union[int, float])`</b>:  The axis local y-coordinate of the object. 
 - <b>``global_x` (Union[int, float])`</b>:  The axis global x-coordinate of the object. 
 - <b>``global_y` (Union[int, float])`</b>:  The axis global y-coordinate of the object. 

Methods: `calculate_top_bottom_right_left_of_local_global()`:   Calculate the top, bottom, right, and left of an object given its local and global coordinates. `calculate_top_bottom_right_left_of_global()`:   Calculate the top, bottom, right, and left of an object given its global coordinates. `calculate_top_bottom_right_left_of_local()`:   Calculate the top, bottom, right, and left of an object given its local coordinates. 




---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L7139"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `calculate_top_bottom_right_left_of_global`

```python
calculate_top_bottom_right_left_of_global()
```

Calculate the top, bottom, right, and left of an object given its global coordinates. 



**Returns:**
 
 - <b>``top` (float)`</b>:  The top coordinate of the object. 
 - <b>``bottom` (float)`</b>:  The bottom coordinate of the object. 
 - <b>``right` (float)`</b>:  The right coordinate of the object. 
 - <b>``left` (float)`</b>:  The left coordinate of the object. 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L7158"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `calculate_top_bottom_right_left_of_local`

```python
calculate_top_bottom_right_left_of_local()
```

Calculate the top, bottom, right, and left of an object given its local coordinates. 



**Returns:**
 
 - <b>``top` (float)`</b>:  The top coordinate of the object. 
 - <b>``bottom` (float)`</b>:  The bottom coordinate of the object. 
 - <b>``right` (float)`</b>:  The right coordinate of the object. 
 - <b>``left` (float)`</b>:  The left coordinate of the object. 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L7119"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `calculate_top_bottom_right_left_of_local_global`

```python
calculate_top_bottom_right_left_of_local_global()
```

Calculate the top, bottom, right, and left of an object given its local and global coordinates. 



**Returns:**
 
 - <b>``top` (float)`</b>:  The top coordinate of the object. 
 - <b>``bottom` (float)`</b>:  The bottom coordinate of the object. 
 - <b>``right` (float)`</b>:  The right coordinate of the object. 
 - <b>``left` (float)`</b>:  The left coordinate of the object. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L7177"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `GenerateID`
A class to generate a unique id 

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L7179"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__()
```

Initialize the GenerateID object. 

Methods:  `generate_random_id()`: Generate a unique id random.  `generate_md5_id()`: Generate a unique id of MD5 hash namespace.  `generate_sha1_id()`: Generate a unique id of SHA-1 hash namespace.  `check_name_md5()`: Check id of uuid version 3 the MD5 hash it match name.  `check_name_sha1()`: Check id of uuid version 5 the SHA-1 hash it match name. 



**Example:**
 ```python
     gen = GenerateID()

     gen.generate_random_id(hex_id=None, short_id=None) # DESC => The method 1.
     # output => c89fe448-ae91-4fce-ac5d-a48a6d580665
     
     gen.generate_random_id(hex_id=None, short_id=8) # DESC => The method 2.
     # output => c89fe448

     gen.generate_random_id(hex_id=True, short_id=None) # DESC => The method 3.
     # output => c89fe448ae914fceac5da48a6d580665

     md5 = gen.generate_md5_id(namespace="example") # DESC => The method 4.
     # output => c5e5f349-28ef-3f5a-98d6-0b32ee4d1743

     gen.check_name_md5(namespace="example", md5=md5) # DESC => The method 5.
     # output => True

     sha1 = gen.generate_sha1_id(namespace="example") # DESC => The method 6.
     # output => 7cb48787-6d91-5b9f-bc60-f30298ea5736

     gen.check_name_sha1(namespace="example", sha1=sha1) # DESC => The method 7.
     # output => True
``` 




---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L7261"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `check_name_md5`

```python
check_name_md5(namespace: str, md5: UUID)
```

Check id of uuid version 3 the MD5 hash it match name. 



**Args:**
 
 - <b>``namespace` (str)`</b>:  The name to checke a match. 
 - <b>``md5` (Optional[uuid.UUID, str])`</b>:  The id of uuid version 3 to checke a match same name. 



**Returns:**
 
 - <b>`bool`</b>:  If the provided UUID match, it returns True; otherwise, it returns False. 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L7280"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `check_name_sha1`

```python
check_name_sha1(namespace: str, sha1: UUID)
```

Check id of uuid version 5 the SHA-1 hash it match name. 



**Args:**
 
 - <b>``namespace` (str)`</b>:  The name to checke a match. 
 - <b>``sha1` (Optional[uuid.UUID, str])`</b>:  The id of uuid version 5 to checke a match same name. 



**Returns:**
 
 - <b>`bool`</b>:  If the provided UUID match, it returns True; otherwise, it returns False. 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L7237"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `generate_md5_id`

```python
generate_md5_id(namespace: str)
```

Generate a unique id of MD5 hash namespace. 



**Args:**
 
 - <b>``namespace` (str)`</b>:  Set any name for generate id to same name. 



**Returns:**
 UUID. 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L7217"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `generate_random_id`

```python
generate_random_id(
    hex_id: Optional[bool] = None,
    short_id: Optional[int] = None
)
```

Generate a unique id random. 



**Args:**
 
 - <b>``hex_id` (Optional[bool], optional)`</b>:  Set hexadecimal representation of id. Defaults to None. 
 - <b>``short_id` (Optional[int], optional)`</b>:  Set short id. Defaults to None. 



**Returns:**
 str. 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L7249"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `generate_sha1_id`

```python
generate_sha1_id(namespace: str)
```

Generate a unique id of SHA-1 hash namespace. 



**Args:**
 
 - <b>``namespace` (str)`</b>:  Set any name for generate id to same name. 



**Returns:**
 UUID. 


---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L7299"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AttrRegisterMap`
A class AttrRegisterMap the attributes register and manages map. 

Methods:  `setattribute`(attribute_name: str, value: Any, attribute_update: bool = True): Sets the named attribute of the object to the specified value.  `getattribute`(attribute_name: str): Gets the named attribute from object. 



**Example:**
 ```python
     # DESC => Set attributes.
     AttrRegisterMap.setattribute(attribute_name="Main", value={'control': self, 'locals': locals()})
     
     print(AttrRegisterMap.getattribute("Main"))
     # DESC => {'control': self, 'locals': locals()}
``` 



**Notes:**

> - `setattribute`: This for set attribute object to the specified value. if attribute exists and attributeis whether (Dict or List or Tuple or Set) and `attribute_update` is True it add a new values to attribute object. 




---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L7368"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `getattribute`

```python
getattribute(attribute_name: str)
```

Get a named attribute from object. 



**Args:**
 
 - <b>``attribute_name` (str)`</b>:  The name of the attribute. 



**Returns:**
 
 - <b>`Any`</b>:  The returns value of attribute. 

---

<a href="https://github.com/MrYassinox/utils-standard/blob/main\utils_standard\modules\utils.py#L7323"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `setattribute`

```python
setattribute(attribute_name: str, value: Any, attribute_update: bool = True)
```

Sets the named attribute of the object to the specified value. 



**Args:**
 
 - <b>``attribute_name` (str)`</b>:  The name of the attribute. 
 - <b>``value` (Any)`</b>:  The value of the attribute. 
 - <b>``attribute_update` (bool)`</b>:  if whether True it add a new values to attribute object.  of type (Dict or List or Tuple or Set). 



**Returns:**
 None 



**Notes:**

> - `setattribute`: This for set attribute object to the specified value. if attribute exists and attributeis whether (Dict or List or Tuple or Set) and `attribute_update` is True it add a new values to attribute object. 


