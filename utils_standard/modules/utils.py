''' Utils a standard toolkits for devlops. '''
########################################################################################################################
# TODO DOCUMENT
########################################################################################################################
# |   ├──  | 
# |   |    └── doc: 

########################################################################################################################
# TODO IMPORTING NECESSARY LIBRARYIES
########################################################################################################################
# LIB => python libraryies
import os
import sys
import tempfile
import time
import shlex
import shutil
import platform
import subprocess
import webbrowser
import inspect
import base64
import colorsys
import importlib
import csv
import tarfile
import argparse
import uuid
import re
from argparse import ArgumentParser
from collections import namedtuple
from glob import glob
from types import SimpleNamespace, FunctionType
from typing import List, Any, Dict, Set, Callable, Union, Tuple, Iterable, Literal, Optional
from io import BytesIO
from pathlib import Path
from importlib import util
from urllib.request import Request, urlopen
from fnmatch import fnmatch
from threading import Thread, Timer, Event
from queue import Queue

# LIB => loguru libraryies
from loguru import logger as loguru

# LIB => setuptools libraryies
import pkg_resources

# LIB => requests libraryies
import requests

# LIB => numpy libraryies
import numpy as np

# LIB => chardet libraryies
import chardet

########################################################################################################################
# TODO SET UP
########################################################################################################################
# DESC => This module defines a set of variables that provide information about the Python environment and the current directory.
python = sys.executable
"""`str`: The path to the Python executable being used."""

platform_sys = platform.system()
"""`str`: The name of the operating system (e.g., 'Windows', 'Linux', 'Darwin')."""

platform_arch = platform.architecture()[0]
"""`str`: The architecture of the operating system (e.g., '32bit', '64bit')."""

platform_form = platform.platform()
"""`str`: A string describing the platform in a concise way."""

platform_procs = platform.processor()
"""`str`: The processor architecture name of the computer running the script."""

platform_info = platform.uname()
"""`tuple`: A tuple containing various system information, including the operating system, node name, release, version, and machine."""

platform_pyth = platform.python_version()
"""`str`: The version of Python being used."""

system = f"Python {sys.version}"
"""`str`: A representing the Python version."""

# DESC => initialization a root path.
current_working_dir = os.getcwd()
"""`str`: get current working directory."""

root_path = os.path.realpath(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
"""`str`: The root path of the current script file."""

# DESC => add a specific path to system for interpreter to search.
sys.path.append(os.path.abspath(os.path.join(root_path)))

########################################################################################################################
# TODO FUNCTIONS MODULES
########################################################################################################################
class LoggerHandle:
    """LoggerHandle functionality and exception handling in applications."""
    def __init__(self, file_handles: bool=False, rotation: str="10 MB", retention: str="5 days", context: str=None, *args, **kwargs): # DESC => initialize constructor
        """LoggerHandle functionality and exception handling in applications.

        LoggerHandle is a lightweight logging class that wraps the Loguru library, offering easy-to-use logging functionality and exception handling in applications.

        Args:
            `file_handles` (bool): A flag indicating whether to open a file for writing logs.
            `rotation` (str, optional): The rotation interval for log files. Automatically rotate too big file Examples: `"10 KB"`, `"100 MB"`, `"0.5 GB"`, `"1 month 2 weeks"`, `"4 days"`, `"10h"` `"10s"`.
                Defaults to "10 MB".
            `retention` (str, optional): The rotation interval for log files. Cleanup after some time. Examples `"1 month 2 weeks"`, `"4 days"`, `"10h"` `"10s"`
                Defaults to "10 days".
            `context` (str, optional): Custom context to be added to each logged message record.
                Defaults to None.
                
        Notes:
            - LoggerHandle is a lightweight logging class that wraps the Loguru library, offering easy-to-use logging functionality and exception handling in applications.
        """
        super(LoggerHandle, self).__init__()
        # DESC => store the value attribute

        if file_handles:
            self.config = {
                "handlers": [
                    {
                        "sink": sys.stdout,
                        "format": "<green>{time:YYYY-MM-DD at HH:mm:ss}</green> | <level>{level: <2}</level> | <cyan>{module}</cyan>::<cyan>{function}</cyan>::<cyan>{line}</cyan>::<cyan>{extra[context]}</cyan> - <level>{message}</level>",
                    },
                    {
                        "sink": 'logs.log', # DESC => name file to created
                        "format": "<green>{time:YYYY-MM-DD at HH:mm:ss}</green> | <level>{level: <2}</level> | <cyan>{module}</cyan>::<cyan>{function}</cyan>::<cyan>{line}</cyan>::<cyan>{extra[context]}</cyan> - <level>{message}</level>",
                        "rotation": rotation, # DESC => Automatically rotate too big file
                        "retention": retention, # DESC => Cleanup after some time
                    },
                ],
            }
        else:
            self.config = {
                "handlers": [
                    {
                        "sink": sys.stdout,
                        "format": "<green>{time:YYYY-MM-DD at HH:mm:ss}</green> | <level>{level: <2}</level> | <cyan>{module}</cyan>::<cyan>{function}</cyan>::<cyan>{line}</cyan>::<cyan>{extra[context]}</cyan> - <level>{message}</level>",
                    },
                ],
            }

        self.logger = loguru.bind(context=context) if context is not None else loguru
        self.logger.configure(**self.config)

    def catch(self,
        exception: Optional[Tuple[BaseException]]=Exception,
        level: Union[str, int]='ERROR',
        reraise: Optional[bool]=False,
        onerror: Optional[callable]=lambda _: sys.exit(1),
        exclude: Optional[Union[BaseException, Tuple[BaseException]]]=(),
        default: Optional[str]=None,
        message: Optional[str]="An error has been caught in function '{record[function]}', process '{record[process].name}' ({record[process].id}), thread '{record[thread].name}' ({record[thread].id}):"):
        """Catch an exception and log it with the 'exception' level.

        Args:
            `exception` (Optional[Tuple[BaseException]], optional): The type of exception to intercept. If several types should be caught, a tuple of exceptions can be used too..
                Defaults to Exception.
            `level` (Union[str, int], optional): The level name or severity with which the message should be logged.
                List name Level: ['`TRACE`', '`DEBUG`', '`INFO`', '`SUCCESS`', '`WARNING`', '`ERROR`', '`CRITICAL`']. Defaults to 'ERROR'.
            `reraise` (Optional[bool], optional): Whether the exception should be raised again and hence propagated to the caller.
                Defaults to False.
            `onerror` (Optional[callable], optional): A function that will be called if an error occurs, once the message has been logged. It should accept the exception instance as it sole argument..
                Defaults to None.
            `exclude` (Optional[Exception], optional): A function that will be called if an error occurs, once the message has been logged. It should accept the exception instance as it sole argument..
                Defaults to None.
            `default` (Optional[str], optional): The value to be returned by the decorated function if an error occurred without being re-raised.
                Defaults to None.
            `message` (_type_, optional): The message that will be automatically logged if an exception occurs.
                Defaults to "An error has been caught in function '{record[function]}', process '{record[process].name}' ({record[process].id}), thread '{record[thread].name}' ({record[thread].id}):".

        Returns:
            Callable: A decorator that can be used to wrap a function and log any caught exceptions.
                Return a decorator to automatically log possibly caught error in wrapped function.

        Example:
        ```python
            logger = LoggerHandle()
            @logger.catch()
            def my_function():
                ...
        ```
        """
        if isinstance(level, str):
            level = level.upper()
        return self.logger.catch(exception=exception, level=level, reraise=reraise, onerror=onerror, exclude=exclude, default=default, message=message)
    def log(self, level: Union[str, int], message: Optional[str], **kwargs: Any) -> None:
        """Log a message with the specified level.

        Args:
            `level` (Union[str, int]): Level name ['`TRACE`', '`DEBUG`', '`INFO`', '`SUCCESS`', '`WARNING`', '`ERROR`', '`CRITICAL`'].
                Level severity value ['`5`', '`10`', '`20`', '`25`', '`30`', '`40`', '`50`'].
            `message` (Optional[str]): The logged message.
            `**kwargs` (Optional[Any]): This is used to add custom context to each logging call message record.

        Returns:
            None

        Example:
        ```python
            logger = LoggerHandle()
            logger.log("That's it, beautiful and simple logging!")
            # Output
            # That's it, beautiful and simple logging!

            logger.log("That's it, beautiful and simple logging! {extra}", extra="record message.")
            # Output
            # That's it, beautiful and simple logging! record message.
        ```
        """
        if isinstance(level, str):
            level = level.upper()

        # DESC => Accessing kwargs
        for key, value in kwargs.items():
            self.logger.bind(key=value)
        return self.logger.log(level, message, **kwargs)
    def trace(self, message: Optional[str], **kwargs: Any) -> None:
        """Log a message with the 'TRACE' level.

        Args:
            `message` (Optional[str]): The logged message.
            `**kwargs` (Optional[Any]): This is used to add custom context to each logging call message record.

        Returns:
            None

        Example:
        ```python
            logger = LoggerHandle()
            logger.trace("That's it, beautiful and simple logging!")
            # Output
            # That's it, beautiful and simple logging!

            logger.trace("That's it, beautiful and simple logging! {extra}", extra="record message.")
            # Output
            # That's it, beautiful and simple logging! record message.
        ```
        """
        # DESC => Accessing kwargs
        for key, value in kwargs.items():
            self.logger.bind(key=value)
        return self.logger.trace(message, **kwargs)
    def debug(self, message: Optional[str], **kwargs: Any) -> None:
        """Log a message with the 'DEBUG' level.

        Args:
            `message` (Optional[str]): The logged message.
            `**kwargs` (Optional[Any]): This is used to add custom context to each logging call message record.

        Returns:
            None

        Example:
        ```python
            logger = LoggerHandle()
            logger.debug("That's it, beautiful and simple logging!")
            # Output
            # That's it, beautiful and simple logging!

            logger.debug("That's it, beautiful and simple logging! {extra}", extra="record message.")
            # Output
            # That's it, beautiful and simple logging! record message.
        ```
        """
        # DESC => Accessing kwargs
        for key, value in kwargs.items():
            self.logger.bind(key=value)
        return self.logger.debug(message, **kwargs)
    def info(self, message: Optional[str], **kwargs: Any) -> None:
        """Log a message with the 'INFO' level.

        Args:
            `message` (Optional[str]): The logged message.
            *`*kwargs` (Optional[Any]): This is used to add custom context to each logging call message record.

        Returns:
            None

        Example:
        ```python
            logger = LoggerHandle()
            logger.info("That's it, beautiful and simple logging!")
            # Output
            # That's it, beautiful and simple logging!

            logger.info("That's it, beautiful and simple logging! {extra}", extra="record message.")
            # Output
            # That's it, beautiful and simple logging! record message.
        ```
        """
        # DESC => Accessing kwargs
        for key, value in kwargs.items():
            self.logger.bind(key=value)
        return self.logger.info(message, **kwargs)
    def success(self, message: Optional[str], **kwargs: Any) -> None:
        """Log a message with the 'INFO' level.

        Args:
            `message` (Optional[str]): The logged message.
            `**kwargs` (Optional[Any]): This is used to add custom context to each logging call message record.

        Returns:
            None

        Example:
        ```python
            logger = LoggerHandle()
            logger.success("That's it, beautiful and simple logging!")
            # Output
            # That's it, beautiful and simple logging!

            logger.success("That's it, beautiful and simple logging! {extra}", extra="record message.")
            # Output
            # That's it, beautiful and simple logging! record message.
        ```
        """
        # DESC => Accessing kwargs
        for key, value in kwargs.items():
            self.logger.bind(key=value)
        return self.logger.success(message, **kwargs)
    def warning(self, message: Optional[str], **kwargs: Any) -> None:
        """Log a message with the 'WARNING' level.

        Args:
            `message` (Optional[str]): The logged message.
            `**kwargs` (Optional[Any]): This is used to add custom context to each logging call message record.

        Returns:
            None

        Example:
        ```python
            logger = LoggerHandle()
            logger.warning("That's it, beautiful and simple logging!")
            # Output
            # That's it, beautiful and simple logging!

            logger.warning("That's it, beautiful and simple logging! {extra}", extra="record message.")
            # Output
            # That's it, beautiful and simple logging! record message.
        ```
        """
        # DESC => Accessing kwargs
        for key, value in kwargs.items():
            self.logger.bind(key=value)
        return self.logger.warning(message, **kwargs)
    def error(self, message: Optional[str], **kwargs: Any) -> None:
        """Log a message with the 'ERROR' level.

        Args:
            `message` (Optional[str]): The logged message.
            `**kwargs` (Optional[Any]): This is used to add custom context to each logging call message record.

        Returns:
            None

        Example:
        ```python
            logger = LoggerHandle()
            logger.error("That's it, beautiful and simple logging!")
            # Output
            # That's it, beautiful and simple logging!

            logger.error("That's it, beautiful and simple logging! {extra}", extra="record message.")
            # Output
            # That's it, beautiful and simple logging! record message.
        ```
        """
        # DESC => Accessing kwargs
        for key, value in kwargs.items():
            self.logger.bind(key=value)
        return self.logger.error(message, **kwargs)
    def critical(self, message: Optional[str], **kwargs: Any) -> None:
        """Log a message with the 'CRITICAL' level.

        Args:
            `message` (Optional[str]): The logged message.
            `**kwargs` (Optional[Any]): This is used to add custom context to each logging call message record.

        Returns:
            None

        Example:
        ```python
            logger = LoggerHandle()
            logger.critical("That's it, beautiful and simple logging!")
            # Output
            # That's it, beautiful and simple logging!

            logger.critical("That's it, beautiful and simple logging! {extra}", extra="record message.")
            # Output
            # That's it, beautiful and simple logging! record message.
        ```
        """
        # DESC => Accessing kwargs
        for key, value in kwargs.items():
            self.logger.bind(key=value)

        return self.logger.critical(message, **kwargs)
    def exception(self, message: Optional[str], **kwargs: Any) -> None:
        """Log a message with the 'CRITICAL' level.

        Args:
            `message` (Optional[str]): The logged message.
            `**kwargs` (Optional[Any]): This is used to add custom context to each logging call message record.

        Returns:
            None

        Example:
        ```python
            logger = LoggerHandle()
            logger.exception("That's it, beautiful and simple logging!")
            # Output
            # That's it, beautiful and simple logging!

            logger.exception("That's it, beautiful and simple logging! {extra}", extra="record message.")
            # Output
            # That's it, beautiful and simple logging! record message.
        ```
        """
        # DESC => Accessing kwargs
        for key, value in kwargs.items():
            self.logger.bind(key=value)

        return self.logger.exception(message, **kwargs)
logger = LoggerHandle(context='DEV')

# NOTE => Get the current Python version number info.
def get_current_py_version(major: bool = True, minor: bool = True, micro: bool = True)-> str:
    """Get the current Python version number info.

    Args:
        `major` (bool, optional): The current version major. Defaults to True.
        `minor` (bool, optional): The current version minor. Defaults to True.
        `micro` (bool, optional): The current version micro. Defaults to True.

    Returns:
        str: Returns version number.
    """
    current_version = sys.version_info # DESC => Get the current Python version number info.
    _major, _minor, _micro = current_version.major, current_version.minor, current_version.micro

    if major and minor and micro:
        return f"{_major}.{_minor}.{_micro}"
    elif major and minor and micro is False:
        return f"{_major}.{_minor}"
    elif major and minor is False and micro is False:
        return f"{_major}"
    elif major is False and minor and micro is False:
        return f"{_minor}"
    elif major is False and minor is False and micro:
        return f"{_micro}"
    else:
        return ""

# NOTE => Gets all Python versions available on the system.
def get_py_versions_available() -> None:
    """Gets all Python versions available on the system."""
    run_shell_command(command="-0", shell="system")

# NOTE => initialization a temp folder path
def setup_temp(path: str = root_path) -> str:
    """Initialize a temporary folder path.

    Args:
        `path` (str, optional): The root path for the temporary folder.
            Defaults to root_path.

    Returns:
        str: The path to the temporary folder.
    """
    if not os.path.exists(os.path.join(path, 'temp')):
        os.makedirs(os.path.join(path, 'temp'), exist_ok=True)
    temp_path = os.path.join(path, 'temp')
    return temp_path

# NOTE => Create a directory.
def create_directory(folder: str, exist_ok: bool = True) -> str:
    """Create a directory.

    Args:
        `folder` (str, optional): The name or path of the directory to create.
            Defaults to None.
        `exist_ok` (bool, optional): set to True, which avoids raising an error if the directory already exists.

    Returns:
        str: The path to the folder created.

    Raises:
        Exception: If no folder name is provided.

    Notes:
        - This function creates the directory using `os.makedirs`.
        - The `exist_ok` parameter is set to True, which avoids raising an error if the directory already exists.
        - If no folder name is provided, an exception is raised.
    """
    if folder:
        os.makedirs(folder, exist_ok=exist_ok)
        return folder
    else:
        raise Exception('Not name folder input')

# NOTE => Clear the screen.
def clear() -> None:
    """Clear the screen.

    Notes:
        - This function clears the screen for Windows using 'cls' command
            and for Mac and Linux using 'clear' command.
    """
    name = os.name
    if name == 'nt':
        # DESC => for Windows(here, os.name is 'nt')
        _ = os.system('cls')
    else:
        # DESC => for mac and linux(here, os.name is 'posix')
        _ = os.system('clear')

# NOTE => Remove files that are older than specified days.
@logger.catch()
def remove_files_older(path_dir: str, days_old: int = 0, logs: Optional[LoggerHandle]=None) -> None:
    """Remove files that are older than specified days.

    Args:
        `path_dir` (str, optional): Path to the directory containing the files.
        `days_old` (int, optional): Number of days old the files should be. Defaults to 0.
        `logs` (Optional[LoggerHandle], optional): An instance of the `LoggerHandle` class for logging purposes.

    Returns:
        None

    Example:
    ```python
        # Remove files older than 7 days in the specified directory
        remove_files(days_old=7, path_dir='/path/to/directory')

        # Remove files older than 30 days in the current directory
        remove_files(days_old=30)
    ```

    Notes:
        - This function checks the modified timestamp of each file in the specified directory.
        - If a file's timestamp is older than the specified number of days, it is removed.
        - The function logs the count of files found to be days old and the count of successfully removed files.
        - If the logs flag is set to True, the function logs additional debug messages for file removal.
        - The `logs` parameter is optional. If provided, it should be an instance of the `LoggerHandle` class for logging purposes.
    """
    # DESC => specify days the files days old
    for file_name in os.listdir(path_dir):
        # DESC => checking whether the file is present in path or not
        if os.path.exists(path_dir):
            file_stamp = os.stat(os.path.join(path_dir, file_name)).st_mtime
            file_count = len(os.listdir(path_dir))

            # DESC => converting days to seconds
            # DESC => time.time() returns current time in seconds
            seconds = time.time() - (int(days_old) * 24 * 60 * 60)
            file_compare = seconds

            # DESC => comparing files with the days
            if file_stamp < file_compare:
                logs.info(f'{file_count} : is found files be to days old.') if isinstance(logs, LoggerHandle) else None
                if not os.remove(os.path.join(path_dir, file_name)):
                    os.remove(os.path.join(path_dir, file_name))
                    logs.info(f'{file_count} : is removed files successfully.') if isinstance(logs, LoggerHandle) else None
                else:
                    logs.debug(f'Unable to delete the {file_count}') if isinstance(logs, LoggerHandle) else None
            else:
                logs.debug(f'Not found files be to days old in folders: {path_dir}') if isinstance(logs, LoggerHandle) else None
        else:
            logs.debug(f'"{path_dir}" - is not found.') if isinstance(logs, LoggerHandle) else None

# NOTE => Get the distribution information for a package.
def get_pkg_distribution(pkg: str = 'utils_dev') -> pkg_resources.Distribution:
    """Get the distribution information for a package.

    Args:
        `pkg` (str, optional): The name of the package. Defaults to 'utils_dev'.

    Returns:
        pkg_resources.Distribution: The distribution information for the package.

    Example:
    ```python
        # Get the distribution information for a package
        distribution = get_pkg_distribution('utils_dev')

        # Print the package details
        print(distribution.project_name)
        print(distribution.version)
        print(distribution.location)
    ```
    """
    pkg = pkg_resources.get_distribution(dist=pkg)
    return pkg

# NOTE => Return a list of environment variables.
def os_environ_list() -> list:
    """Return a list of environment variables.

    Returns:
        list: A list of tuples containing the environment variable name-value pairs.
    """
    environ = os.environ.items()
    environ_list = []
    for i in environ:
        environ_list.append(i)
    return environ_list

# NOTE => Set an environment variable locally.
def os_environ_set(environ_name: str, environ_value = None) -> None:
    """Set an environment variable locally.

    Args:
        `environ_name` (str, optional): The name of the environment variable.
        `environ_value` (Any, optional): The value to set for the environment variable.
            Defaults to None.

    Returns:
        None

    Example:
    ```python
        # Set the 'PATH' environment variable to '/usr/bin'
        >>> os_environ_set('PATH', '/usr/bin')
    ```

    Notes:
        - This function sets the environment variable locally.
        - It modifies the `os.environ` dictionary.
    """
    os.environ[environ_name.upper()] = environ_value # <= DESC Set environment variables locally

# NOTE => Get the value of an environment variable.
def os_environ_get(environ_name: str) -> str:
    """Get the value of an environment variable.

    Args:
        `environ_name` (str, optional): The name of the environment variable.

    Returns:
        str: The value of the environment variable.

    Example:
    ```python
        # Get the value of the 'GIT_HOME' environment variable
        >>> os_environ_get('GIT_HOME')
        # Output: '/path/to/git'
    ```

    Notes:
        - This function retrieves the value of the environment variable from the `os.environ` dictionary.
    """
    git_environ = os.environ[environ_name]
    return git_environ

# NOTE => Check if a module exists.
def module_exists(module_name: str = None, logs: Optional[LoggerHandle]=None) -> bool:
    """Check if a module exists.

    Args:
        `module_name` (str, optional): The name of the module. Defaults to None.
        `logs` (Optional[LoggerHandle], optional): An instance of the `LoggerHandle` class for logging purposes.

    Returns:
        bool: True if the module exists, False otherwise.

    Example:
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

    Notes:
        - This function uses `util.find_spec` to check if the module exists.
        - If the module is not found, a warning message is logged if the logs flag is set to True.
        - The `logs` parameter is optional. If provided, it should be an instance of the `LoggerHandle` class for logging purposes.
    """
    try:
        spec = util.find_spec(module_name)
    except ModuleNotFoundError:
        logs.warning("Module not found error!") if isinstance(logs, LoggerHandle) else None
        return False
    return spec is not None

# NOTE => Run a shell command python and capture the output.
@logger.catch()
def run_shell_command(command: str, shell: Optional[Literal["system", "popen", "subprocess"]] = None):
    """Run a shell command python and capture the output.

    Args:
        `command` (str): The command to run on shell. Example "-h" or "--help".
        `shell` (Optional["system", "popen", "subprocess"], optional): The shell of to run command. Defaults to "system".

    Returns:
        (str | None): if use shell `subprocess` Returns output as string else return none.

    Notes:
        - `system`:  This will run the command and return any output.
        - `popen`: This will run the command and not return any output.
        - `subprocess`: Can then process or display the output and returned as a string.
    """
    PYTHON = sys.executable # DESC => getting path to python executable (full path of deployed python).
    name = os.name

    if name == 'nt':
        # DESC => for Windows(here, os.name is 'nt')
        PYTHON = "py"
    else: 
        # DESC => for mac and linux(here, os.name is 'posix')
        PYTHON = "python"

    # DESC => initialize cmd
    cmd_command = '{} {}'.format(PYTHON, command)

    if shell == "system":
        os.system(cmd_command) # DESC => This will run the command and return any output.
    elif shell == "popen":
        os.popen(cmd_command).read() # DESC => This will run the command and not return any output.
    elif shell == "subprocess":
        output = subprocess.check_output(cmd_command, shell=True, text=True) # DESC => can then process or display the output and returned as a string
        return output
    else:
        os.system(cmd_command) # DESC => This will run the command and return any output.

# NOTE => Run a subprocess command and capture the output.
@logger.catch()
def sub_run(command: str = None, desc: str = None, errdesc: str = None, logs: Optional[LoggerHandle]=None) -> str:
    """Run a subprocess command and capture the output.

    Args:
        `command` (str, optional): The command to run. Defaults to None.
        `desc` (str, optional): The description of the command. Defaults to None.
        `errdesc` (str, optional): The error description. Defaults to None.
        `logs` (Optional[LoggerHandle], optional): An instance of the `LoggerHandle` class for logging purposes.

    Returns:
        str: The captured stdout output.

    Raises:
        RuntimeError: If the command execution returns a non-zero return code.

    Example:
    ```python
        # Run a command and capture the output
        output = sub_run("ls -l", desc="Listing files")

        # Run a command and handle errors
        try:
            output = sub_run("some_invalid_command", desc="Running invalid command", errdesc="Error occurred")
        except RuntimeError as e:
            print(e)
    ```

    Notes:
        - This function uses `subprocess.run` to execute the command.
        - If an error occurs during command execution, a `RuntimeError` is raised.
        - The `logs` parameter is optional. If provided, it should be an instance of the `LoggerHandle` class for logging purposes.
    """
    if desc is not None:
        logs.info(desc) if isinstance(logs, LoggerHandle) else None

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    if result.returncode != 0:
        message = f"""{errdesc or 'Error running command'}.
        Command: {command}
        Error code: {result.returncode}
        stdout: {result.stdout.decode(encoding="utf8", errors="ignore") if len(result.stdout)>0 else '<empty>'}
        stderr: {result.stderr.decode(encoding="utf8", errors="ignore") if len(result.stderr)>0 else '<empty>'}
        """
        logs.error(message) if isinstance(logs, LoggerHandle) else None
        raise RuntimeError(message)
    return result.stdout.decode(encoding="utf8", errors="ignore")

# NOTE => Check if a command runs successfully.
@logger.catch()
def check_run(command) -> bool:
    """Check if a command runs successfully.

    Args:
        `command` (str): The command to run.

    Returns:
        bool: True if the command runs successfully, False otherwise.

    Notes:
        - You can use this function by providing the desired command as a string to the command parameter.
            The function will execute the command using subprocess.run and capture the return code.
            If the return code is 0, it means the command ran successfully, and the function will return True.
            Otherwise, it will return False.
    """
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    return result.returncode == 0

# NOTE => Run a Python command and capture the output.
@logger.catch()
def run_python(command: str = None, desc: str = None, errdesc: str = None) -> str:
    """Run a Python command and capture the output.

    Args:
        `command` (str, optional): The Python command to run. Defaults to None.
        `desc` (str, optional): Description of the command. Defaults to None.
        `errdesc` (str, optional): Description of the error message. Defaults to None.

    Returns:
        str: The output of the `sub_run` function.

    Example:
    ```python
        # Run a Python command
        run_python('print("Hello, world!")', desc='Print a greeting')
        # Output: 'Hello, world!'
    ```

    Notes:
        - This function uses the `sub_run` function to execute the Python command.
        - This function utilizes the sub_run function, passing the Python command to be executed as a shell command It captures the stdout 
            output and returns it as a string To use this function, provide the Python command as a string to the command paramete
            You can also optionally provide a description for the command using the desc parameter and an error description using the errdesc parameter
            The function will execute the command and return the captured stdout output.
    """
    return sub_run(f'"{python}" -c "{command}"', desc, errdesc)

# NOTE => Clone a Git repository from a given URL.
@logger.catch()
def sub_gitclone(url: str, targetdir: str = None, branch: str = None, logs: Optional[LoggerHandle]=None) -> None:
    """Clone a Git repository from a given URL.

    Args:
        `url` (str): The URL of the Git repository.
        `targetdir` (str, optional): The target directory to clone the repository into. Defaults to None.
        `branch` (str, optional): The branch to clone. Defaults to None.
        `logs` (bool, optional): Flag to determine whether to log the results.

    Returns:
        None

    Raises:
        Exception: If an error occurs during cloning or path manipulation.

    Example:
    ```python
        sub_gitclone('https://github.com/example/repo.git', targetdir='/path/to/destination', branch='main')
        sub_gitclone('https://github.com/example/repo.git', targetdir='myrepo', branch='main')
    ```

    Notes:
        - This example will clone the Git repository from the given URL `(https://github.com/example/repo.git)`
            into the specified target directory `(/path/to/destination)` and checkout the `main` branch.
        - Make sure you have the git command-line tool installed and accessible in your environment for this function to work properly
    """
    try:
        git = os.environ.get('GIT', 'git')
        response = requests.get(url=url)

        if response.status_code == 200:
            logs.info('Requests status: ok') if isinstance(logs, LoggerHandle) else None

            if targetdir:
                if branch is None:
                    res = subprocess.run([git, 'clone', url, targetdir], stdout=subprocess.PIPE).stdout.decode('utf-8')
                else:
                    res = subprocess.run([git, 'clone', '--branch', branch, url, targetdir], stdout=subprocess.PIPE).stdout.decode('utf-8')
            else:
                if branch is None:
                    res = subprocess.run([git, 'clone', url], stdout=subprocess.PIPE).stdout.decode('utf-8')
                else:
                    res = subprocess.run([git, 'clone', '--branch', branch, url], stdout=subprocess.PIPE).stdout.decode('utf-8')
            
            logs.info(res) if isinstance(logs, LoggerHandle) else None
    except Exception as error:
        logs.error(f'Failed to download: {url}') if isinstance(logs, LoggerHandle) else None
        raise Exception(f'Error: {error}')

# NOTE => Clone and Manage repositories.
@logger.catch()
def repositories(cachDir: str = 'cachname', nameEnv: str = 'name', repoUrl: str = 'https://github.com/', branch: str = None, customDir: str = None, logs: Optional[LoggerHandle]=None) -> None:
    """Manage repositories.

    Args:
        `cachDir` (str, optional): The cache directory name. Defaults to 'cachname'.
        `nameEnv` (str, optional): The name of the environment variable. Defaults to 'name'.
        `repoUrl` (str, optional): The URL of the repository. Defaults to 'https://github.com/'.
        `branch` (str, optional): The branch to clone. Defaults to None.
        `customDir` (str, optional): The custom directory to clone into. Defaults to None.
        `logs` (Optional[LoggerHandle], optional): An instance of the `LoggerHandle` class for logging purposes.

    Raises:
        Exception: If an error occurs during cloning or path manipulation.
    
    Notes:
        - The `logs` parameter is optional. If provided, it should be an instance of the `LoggerHandle` class for logging purposes.
    """
    # DESC => make folder
    create_directory(folder='repositories')

    # DESC => initialization repositories
    if customDir is None:
        repo_dir = os.path.abspath(os.path.join('repositories', cachDir))
        repo_branch_dir = os.path.abspath(os.path.join('repositories', cachDir, branch))
    else:
        repo_dir = os.path.abspath(os.path.join('repositories', cachDir, customDir))
        repo_branch_dir = os.path.abspath(os.path.join('repositories', cachDir, customDir, branch))

    repo_url = os.environ.get(str(nameEnv.upper() + '_REPO'), repoUrl)

    if branch is None:
        if not os.path.exists(repo_dir):
            logs.info(f"Repositories: {cachDir} is cloning...") if isinstance(logs, LoggerHandle) else None

            # DESC => make folder
            create_directory(repo_dir)

            # DESC => Cloning repositories
            sub_gitclone(repo_url, targetdir=repo_dir, branch=None)
        else:
            logs.info(f"Repositories: {cachDir} checked exists.") if isinstance(logs, LoggerHandle) else None
    else:
        if not os.path.exists(repo_branch_dir):
            logs.info(f"Repositories: {repo_branch_dir} is cloning...") if isinstance(logs, LoggerHandle) else None

            # DESC => make folder
            create_directory(repo_branch_dir)

            # DESC => Cloning repositories
            sub_gitclone(repo_url, targetdir=repo_branch_dir, branch=branch)
        else:
            logs.info(f"Repositories: {repo_branch_dir} checked exists.") if isinstance(logs, LoggerHandle) else None

    if branch is None:
        # DESC => append path to system path list
        sys.path.append(os.path.abspath(os.path.join(root_path, repo_dir)))
    else:
        # DESC => append path to system path list
        sys.path.append(os.path.abspath(os.path.join(root_path, repo_branch_dir)))

# NOTE => Install a Git module.
@logger.catch()
def sub_gitinstall(module: str, logs: Optional[LoggerHandle]=None) -> None:
    """Install a Git module.

    Args:
        `module` (str): The module string to install.
        `logs` (Optional[LoggerHandle], optional): An instance of the `LoggerHandle` class for logging purposes.

    Returns:
        None

    Example:
    ```python
        sub_gitinstall(module='your_module')
        sub_gitinstall('https://github.com/example/module.git', logs=True)
    ```

    Notes:
        - Make sure to have `Git` installed and configured on your system for the function to work correctly.
        - The `logs` parameter is optional. If provided, it should be an instance of the `LoggerHandle` class for logging purposes.
    """
    res = subprocess.run(['git', 'install', '-e', module], stdout=subprocess.PIPE).stdout.decode('utf-8')
    logs.info(res) if isinstance(logs, LoggerHandle) else None

# NOTE => Download a file using wget.
@logger.catch()
def sub_wget(url: str, outputdir: str, logs: Optional[LoggerHandle]=None) -> None:
    """Download a file using wget.

    Args:
        `url` (str): The URL of the file to download.
        `outputdir` (str): The output directory to save the file.
        `logs` (Optional[LoggerHandle], optional): An instance of the `LoggerHandle` class for logging purposes.

    Returns:
        None

    Example:
    ```python
        sub_wget(url='your_url', outputdir='your_output_directory')
        sub_wget('https://example.com/file.zip', '/path/to/output', logs=True)
    ```

    Notes:
        - Make sure to have the `wget` command-line tool installed and accessible in your system's PATH for the function to work correctly.
        - The `logs` parameter is optional. If provided, it should be an instance of the `LoggerHandle` class for logging purposes.
    """
    res = subprocess.run(['wget', url, '--directory-prefix', f'{outputdir}'], stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')
    logs.info(res) if isinstance(logs, LoggerHandle) else None

# NOTE => Download a file using wget.
@logger.catch()
def wget(url: str, outputdir: str, logs: Optional[LoggerHandle]=None) -> None:
    """Download a file using wget.

    Args:
        `url` (str): The URL of the file to download.
        `outputdir` (str): The output directory to save the file.
        `logs` (Optional[LoggerHandle], optional): An instance of the `LoggerHandle` class for logging purposes.

    Raises:
        Exception: If an error occurs during cloning or path manipulation.

    Example:
    ```python
        wget(url='your_url', outputdir='your_output_directory')
    ```
    """
    try:
        logs.info(f"Downloading from {url}...") if isinstance(logs, LoggerHandle) else None

        # DESC => Get the basename of the URL
        basename = os.path.basename(url)

        # DESC => Get the basename of the URL
        with urlopen(url) as source, open(os.path.join(outputdir, basename), 'wb') as output:
            while True:
                # DESC => Read a buffer of data from the source
                buffer = source.read(8192)
                if not buffer:
                    break

                # DESC => Write the buffer to the output file
                output.write(buffer)
        logs.info(f"Write to {outputdir}") if isinstance(logs, LoggerHandle) else None
    except Exception as error:
        logs.error(f"Failed to download {url}") if isinstance(logs, LoggerHandle) else None
        raise Exception(f'Error: {error}')

# NOTE => Download a file using requests.
@logger.catch()
def requests_get(url: str, outputdir: str = None, outputBytesIO: bool = False, stream: bool = False, logs: Optional[LoggerHandle]=None):
    """Download a file using requests.

    Args:
        `url` (str): The URL of the file to download.
        `outputdir` (str, optional): The output directory to save the file. Defaults to None.
        `outputBytesIO` (bool, optional): Whether to return the file content as BytesIO. Defaults to False.
        `stream` (bool, optional): By default, when you make a request, the body of the response is downloaded immediately.
            You can override this behavior and defer downloading the response body until you access the `Response.content`
            attribute with the stream parameter:. Defaults to False.
        `logs` (Optional[LoggerHandle], optional): An instance of the `LoggerHandle` class for logging purposes.

    Returns:
        BytesIO: The file content as BytesIO, if outputBytesIO is True.

    Raises:
        Exception: If an error occurs during request or path manipulation.

    Example:
    ```python
        requests_get(url='your_url', outputdir='your_output_directory', outputBytesIO=False)
    ```

    Notes:
        - Note that connections are only released back to the pool for reuse once all body data has been read; be sure to either
            set stream to False or read the content property of the Response object
        - The `logs` parameter is optional. If provided, it should be an instance of the `LoggerHandle` class for logging purposes.
    """
    try:
        # DESC => Get the basename of the URL
        basename = os.path.basename(url)

        # DESC => Send a GET request to the URL
        response = requests.get(url=url, stream=stream)

        if response.status_code == 200:
            logs.info(f"Downloading from {url}...") if isinstance(logs, LoggerHandle) else None

            if outputdir is not None:
                # DESC => Save the file to the output directory
                with open(os.path.join(outputdir, basename), 'wb') as f:
                    for chunk in response:
                        f.write(chunk)
                    logs.info(f"File saved to {outputdir}") if isinstance(logs, LoggerHandle) else None

            if outputBytesIO:
                logs.info("File content return is data BytesIO") if isinstance(logs, LoggerHandle) else None

                # DESC => Return the file content as BytesIO
                bytesIO = BytesIO(response.content)
                return bytesIO
    except Exception as error:
        logs.error(f"Failed to download: {url}") if isinstance(logs, LoggerHandle) else None
        raise Exception(f'Error: {error}')

# NOTE => Get the file size in bytes and convert it to bytes, KB, MB, GB, or TB.
@logger.catch()
def get_file_size(file_pathe: str, include_unit: bool=True) -> str:
    """Get the file size in bytes and convert it to bytes, KB, MB, GB, or TB.

    Args:
        `file_pathe` (str): The path to the file.
        `include_unit` (bool): The include unit if false then return size by integer without unit.

    Returns:
        str: The file size with the corresponding unit. in bytes, KB, MB, GB, or TB.

    Example:
    ```python
        file_path = 'path_to_your_file'
        size = get_file_size(file_path)
        print(f"The size of {file_path} is: {size}")
    ```
    """
    # DESC => Get the size of the file
    file_size = os.path.getsize(file_pathe)

    # DESC => Convert bytes size to KB, MB, GB, or TB
    for unit in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if file_size < 1024.0: # NOTE => conditional to less than
            if include_unit:
                return "%3.2f %s" % (file_size, unit)
            else:
                return float(round(file_size, 2))
        file_size /= 1024.0

# NOTE => Check if the file size is less than or equal to the allowed size.
@logger.catch()
def check_file_size(foldersize: str, allowed_size: float) -> bool:
    """Check if the file size is less than or equal to the allowed size.

    Args:
        `foldersize` (str): The size of the file in the format "<size> <unit>" (e.g., "10.5 KB").
        `allowed_size` (float): The maximum allowed file size in megabytes (MB).

    Returns:
        bool: True if the file size is less than or equal to the allowed size, False otherwise.

    Example:
    ```python
        file_size = "10.5 KB"
        allowed_limit = 20.0  # Maximum allowed size in megabytes

        is_within_limit = check_file_size(file_size, allowed_limit)
        print(f"The file size is within the allowed limit: {is_within_limit}")
    ```
    """
    # Split the foldersize text to get the value and unit
    split_tup = str(foldersize).split(' ')

    # DESC => Check the unit of the foldersize
    if str(split_tup[1]) == 'bytes':
        # DESC => Convert bytes to megabyte [MB]
        convert_bytesToMb = float(split_tup[0]) / (1024 ** 2)
        if convert_bytesToMb <= allowed_size:
            return True
        else:
            return False

    elif str(split_tup[1]) == 'KB':
        # DESC => convert kilobyte [KB] to megabyte [MB]
        convert_KbToMb = float(split_tup[0])/1024
        if convert_KbToMb <= allowed_size:
            return True
        else:
            return False

    elif str(split_tup[1]) == 'MB':
        if float(split_tup[0]) <= allowed_size:
            return True
        else:
            return False

    elif str(split_tup[1]) == 'GB':
        # DESC => convert gigabyte [GB] to megabyte [MB]
        convert_GbToMb = float(split_tup[0])*1024
        if convert_GbToMb <= allowed_size:
            return True
        else:
            return False

    elif split_tup[1] == 'TB':
        # DESC =>  Convert terabytes to megabytes [MB]
        convert_TbToMb = float(split_tup[0]) * (1024 ** 2)
        if convert_TbToMb <= allowed_size:
            return True
        else:
            return False

# NOTE => Search for a word in a file and print if it exists or not.
@logger.catch()
def search_str(file_path: str, word: str, logs: Optional[LoggerHandle]=None) -> None:
    """Search for a word in a file and print if it exists or not.

    Args:
        `file_path` (str): The path to the file.
        `word` (str): The word to search for.
        `logs` (Optional[LoggerHandle], optional): An instance of the `LoggerHandle` class for logging purposes.

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified file does not exist.

    Example:
    ```python
        >>> search_str('file.txt', 'apple')
        # Output:
        # [apple] exists in the file.

        >>> search_str('file.txt', 'banana')
        # Output:
        # [banana] does not exist in the file.
    ```

    This function searches for a specific word in a file. It opens the file specified by `file_path`,
    reads its content, and checks if the `word` is present in the file. If the word is found, it prints
    "[word] exists in the file.". Otherwise, it prints "[word] does not exist in the file.".

    Notes:
        - The function assumes the file is a text file and reads it in read-only mode.
        - The `logs` parameter is optional. If provided, it should be an instance of the `LoggerHandle` class for logging purposes.
    """
    try:
        with open(file_path, 'r') as file:
            # DESC => read all content of a file
            content = file.read()

            # DESC => check if string present in a file
            if word in content:
                logs.info(f"[{word}] exists in the file.") if isinstance(logs, LoggerHandle) else None
            else:
                logs.info(f"[{word}] does not exist in the file.") if isinstance(logs, LoggerHandle) else None
    except FileNotFoundError as error:
        raise FileNotFoundError(f'Error: {error}')

# NOTE => Search for a word in each line of a file and print the line and line number if found.
@logger.catch()
def search_str_by_line(file_path: str, word: str, logs: Optional[LoggerHandle]=None) -> None:
    """Search for a word in each line of a file and print the line and line number if found.

    Args:
        `file_path` (str): The path to the file.
        `word` (str): The word to search for.
        `logs` (Optional[LoggerHandle], optional): An instance of the `LoggerHandle` class for logging purposes.

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified file is not found.

    Example:
    ```python
        # Search for the word 'hello' in a file
        search_str_by_line('example.txt', 'hello')
        # Output:
        # [hello] exists in the file.
        # Line Number: 2
        # Line: This is a hello world example.
    ```

    Notes:
        - This function reads each line of the file and checks if the specified word is present on each line.
        - The `logs` parameter is optional. If provided, it should be an instance of the `LoggerHandle` class for logging purposes.
    """
    try:
        with open(file_path, 'r') as file:
            # DESC => Read all lines in a list
            lines = file.readlines()

            # DESC => Search for the word in each line
            for line in lines:
                # DESC => Check if the word is present in the current line
                if line.find(word) != -1:
                    logs.info(f"""
                    [{word}] exists in the file.
                    Line Number: {lines.index(line)}
                    Line: {line}
                    """) if isinstance(logs, LoggerHandle) else None
    except FileNotFoundError as error:
        raise FileNotFoundError(f'Error: {error}')

# NOTE => Search for a word in a file and optionally replace it with a new word.
@logger.catch()
def search_and_replace(file_path: str, word: str, replace: str = None, logs: Optional[LoggerHandle]=None) -> None:
    """Search for a word in a file and optionally replace it with a new word.

    Args:
        `file_path` (str): The path to the file.
        `word` (str): The word to search for.
        `replace` (str, optional): The word to replace the found word with. Defaults to None.
        `logs` (bool, optional): The Enable output logs.

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified file is not found.

    Example:
    ```python
        # Search for the word 'hello' in a file and replace it with 'world'
        >>> search_and_replace('example.txt', 'hello', 'world')
        # Output:
        # [hello] exists in the file.
        # Replaced [hello] with [world] in the file.
    ```

    Notes:
        - This function reads the content of the file, searches for the specified word, and replaces it if a replacement word is provided.
        - If the word is found in the file, it prints a message indicating its presence and, if specified, replaces it with the provided replacement word.
        - If the word is not found, it prints a message indicating its absence.
    """
    try:
        with open(file_path, 'r') as read_file:
            # DESC => Read all content of the file
            content = read_file.read()

            # DESC => Check if string is present in the file
            if word in content:
                logs.info(f"[{word}] exists in the file.") if isinstance(logs, LoggerHandle) else None
                if replace is not None:
                    # DESC => Replace the word if a replacement is provided
                    content = content.replace(word, replace)
                    logs.info(f"Replaced [{word}] with [{replace}] in the file.") if isinstance(logs, LoggerHandle) else None
            else:
                logs.info(f"[{word}] does not exist in the file.") if isinstance(logs, LoggerHandle) else None

        # DESC => Write the modified content back to the file
        with open(file_path, 'w') as write_file:
            write_file.write(content)
    except FileNotFoundError as error:
        raise FileNotFoundError(f"Error: {error}")

# NOTE => Create and return a Thread or Timer object based on the provided parameters.
@logger.catch()
def threading_manager_functions(
    thread_name: str = None,
    function: object = None,
    args: Iterable = (),
    kwargs: Dict[str, Any] = None,
    daemon: bool = None,
    timer: bool = None,
    time: float = 1) -> Union[Thread, Timer, Exception]:
    """Manage threading operations by creating and returning either a Thread or a Timer object.

    Args:
        `thread_name` (str, optional): The name of the thread. Defaults to None.
        `function` (object, optional): The target function to be executed by the thread. Defaults to None.
        `args` (Iterable, optional): The arguments to pass to the target function. Defaults to ().
        `kwargs` (Dict[str, Any], optional): The keyword arguments to pass to the target function. Defaults to None.
        `daemon` (bool, optional): Whether the thread is a daemon thread. Defaults to None.
        `timer` (bool, optional): Whether to create a Timer object instead of a Thread object. Defaults to None.
        `time` (float, optional): The time interval for the Timer object, in seconds. Defaults to 1.

    Returns:
        Union[Thread, Timer, Exception]: A Thread or Timer object, or an Exception if an error occurs.

    Raises:
        Exception: If an error occurs while creating the Thread or Timer object.

    Example:
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

    Notes:
        This function provides a convenient way to manage threading operations by creating either a Thread or a Timer
        object based on the specified parameters.
    """
    try:
        if timer is None:
            # DESC => Create a Thread object
            thread_work = Thread(group=None, name=thread_name, target=function, args=args, kwargs=kwargs, daemon=daemon)
            return thread_work
        else:
            # DESC => Create a Timer object
            thread_work_time = Timer(interval=time, function=function, args=args, kwargs=kwargs)
            return thread_work_time
    except Exception as error:
        raise Exception(f'Error: {error}')

# NOTE => Scan a folder and return the list of files and other relevant information.
@logger.catch()
def search_scanne_folder(folder_path: str, ext_specific: Optional[List[str]] = None) -> Tuple[List[dict], int]:
    """Scan a folder and return the list of files and other relevant information.

    Args:
        `folder_path` (str, optional): The folder path to scan..
        `ext_specific` (List[str], optional): List of specific file extensions to include. Defaults to None.

    Returns:
        Tuple[List[dict], int]: A tuple containing the list of dictionaries containing file information and the total file count.

    Raises:
        FileNotFoundError: If the specified folder is not found.

    Example:
    ```python
        folder_path = '/path/to/folder'
        extensions_list = ['.txt', '.csv', '.xlsx']
        files, total_count = scan_folder(folder_path, ext_specific=extensions_list)

        print(f"Total files: {total_count}")

        for file in files:
            print(file)
    ```

    Notes:
        - This function scans the specified folder and retrieves information about each file in the folder, including the file path, name, size, and extension.
        - If a list of extensions is provided, only files with those extensions will be included in the result. If no extensions are provided, all files in the folder will be included.
    """
    try:
        files_info = []
        total_files = 0

        if os.path.isdir(folder_path): # DESC => check if folders exists.
            for root, dirs, filenames in os.walk(folder_path, topdown=True):
                for filename in filenames:
                    # DESC => make path to file
                    file_current_path = os.path.join(root, filename)

                    # DESC => check file extension available in list extensions.
                    if ext_specific is None or os.path.splitext(filename)[1] in ext_specific:
                        file_info = {
                            'file_path': file_current_path,
                            'file_name': filename,
                            'file_size': get_file_size(file_pathe=file_current_path, include_unit=True),
                            'file_extension': os.path.splitext(filename)[1],
                        }

                        files_info.append(file_info) # DESC => append info file
                        total_files += 1 # DESC => count files.

            return files_info, total_files
        else:
            raise FileNotFoundError(f"Not found folder: {folder_path}")
    except FileNotFoundError as error:
        raise FileNotFoundError(f"Error: {error}")

# NOTE => Get data from a CSV or XLSX file and return it as a list.
@logger.catch()
def get_data_from_csv_xlsx(filename: str = None, mode: str = 'r', insert_data: str = None, index: int = 0, col_csv: int = 0, skips_heading: bool = False) -> List[str]:
    """Get data from a CSV or XLSX file and return it as a list.

    Args:
        `filename` (str, optional): The path to the file. Defaults to None.
        `mode` (str, optional): The mode in which the file should be opened. Defaults to 'r'.
        `insert_data` (str, optional): Data to be inserted at a specific index in the list. Defaults to None.
        `index` (int, optional): The index at which the data should be inserted. Defaults to 0.
        `col_csv` (int, optional): The column index to extract data from in case of a CSV file. Defaults to 0.
        `skips_heading` (bool, optional): Whether to skip the heading in a CSV file. Defaults to False.

    Returns:
        List[str]: A list of items read from the file.

    Raises:
        Exception: If there is an error while processing the file.
    
    Example:
    ```python
        filename = 'data.csv'
        data = get_data_from_csv_xlsx(filename, mode='r', insert_data='Inserted Data', index=0, col_csv=0, skips_heading=True)
        print(data)
        # Output: ['Inserted Data', 'Value 1', 'Value 2', ...]
    ```

    Notes:
        - This function reads data from a CSV or XLSX file and returns it as a list.
        - By default, it assumes that the file is a text file, where each line is an element in the list.
        - If the file extension is '.csv', it assumes a comma-separated values format and extracts data from the specified column index.
        - The optional `insert_data` parameter allows inserting additional data into the list at a specified index.
        - If an error occurs during file processing, an exception is raised.
    """
    try:
        # DESC => split text filename
        name, ext = os.path.splitext(os.path.basename(str(filename)))
        exts = ['csv', 'xlsx']

        with open(file=filename, mode=mode, encoding='utf8') as file_open:
        # DESC => While loading the file by specifying path along with filename, if you got any unicode error then append r before path of filename

            if str(ext).endswith(tuple(exts)):
                data_list = []

                # DESC => create reader object by passing the file
                reader = csv.reader(file_open, delimiter=",")

                if skips_heading:
                    # DESC => Skips the heading
                    heading = next(reader)

                for row in reader:
                    data_list.append(str(row[col_csv]))
            else:
                # DESC => preparing list
                data_list = [str(line).strip() for line in file_open]

            if insert_data is not None:
                data_list.insert(index, insert_data) # DESC => ('') is inserted at index 0 (1th position)

            return data_list
    except Exception as error:
        raise Exception(f'Error: {error}')

# NOTE => Edit a text file by adding, replacing, or removing content.
@logger.catch()
def edit_file_txt(
    filename: str,
    add_on_star: str = None,
    add_on_end: str = None,
    word_old: str = None,
    word_new: str = None,
    remove_duplicates: bool = False,
    splitlines: bool = True,
    overwrite_file: bool = True
) -> None:
    """Edit a text file by adding, replacing, or removing content.

    Args:
        `filename` (str): The path to the text file.
        `add_on_star` (str, optional): The content to add at the start of each line. Defaults to None.
        `add_on_end` (str, optional): The content to add at the end of each line. Defaults to None.
        `word_old` (str, optional): The old word to replace. Defaults to None.
        `word_new` (str, optional): The new word to replace the old word with. Defaults to None.
        `remove_duplicates` (bool, optional): Whether to remove duplicate lines. Defaults to False.
        `splitlines` (bool, optional): Whether to split the file into lines or keep it as a single string. Defaults to True.
        `overwrite_file` (bool, optional): Whether to overwrite the original file or create a new file. Defaults to True.

    Returns:
        None

    Raises:
        ValueError: If remove_duplicates is True and overwrite_file is True.

    Example:
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
    
    Notes:
        - This function edits a text file by adding, replacing, or removing content based on the provided arguments.
        - It can add text at the start or end of each line, replace words, and remove duplicate lines.
        - By default, the function splits lines when reading the file and overwrites the original file with the edited content.
        - If `remove_duplicates` is set to True, the function removes duplicate lines from the file.
        - If `overwrite_file` is set to False, a new file with the edited content is created instead of overwriting the original file.
    """
    try:
        # NOTE => split text filename
        name, ext = os.path.splitext(os.path.basename(str(filename)))

        # NOTE => get path to file
        loca = filename
        if loca.find('/') == -1:
            split_location = str('\\'.join(loca.split('\\')[0:-1]))
        else:
            split_location = str('/'.join(loca.split('/')[0:-1]))

        # NOTE => read file
        with open(file=filename, mode='rt') as file_read:
            # NOTE => remove duplicates word
            if remove_duplicates:
                if overwrite_file is not True:
                    # NOTE => read file contents to string
                    content = sorted(file_read.readlines())

                    # NOTE => store word in file to set and sorting a alphabetically
                    storehouse = sorted(set(content))

                else:
                    raise ValueError('remove_duplicates: does not work with overwrite_file=True. Please set overwrite_file to False.')
            else:
                # NOTE => read file contents to string
                if splitlines:
                    content = file_read.read().splitlines()
                else:
                    content = file_read.readlines()

            if overwrite_file:
                # NOTE => overrite the input file with the resulting data
                with open(file=filename, mode='wt') as file_write:
                    # NOTE => for each line in the input file
                    for line in content:
                        if word_old and word_new is not None:
                            # NOTE => replace all occurrences of the required string
                            file_write.write(line.replace(word_old, word_new))
                        elif add_on_end is not None:
                            file_write.write(line + add_on_end)
                        elif add_on_star is not None:
                            file_write.write(add_on_star + line)
                        elif word_old and word_new and add_on_end is not None:
                            file_write.write(line.replace(word_old, word_new))
                            file_write.write(line + add_on_end)
                        elif word_old and word_new and add_on_star is not None:
                            file_write.write(line.replace(word_old, word_new))
                            file_write.write(add_on_star + line)
            else:
                # NOTE => overrite the file with the resulting data
                with open(file=str(os.path.join(split_location, str(name + '_edit' + ext))), mode='wt') as file_write:

                    if remove_duplicates:
                        for line in storehouse:
                            file_write.write(line)

                    # NOTE => for each line in the input file
                    for line in content:
                        if word_old and word_new is not None:
                            file_write.write(line.replace(word_old, word_new))
                        elif add_on_end is not None:
                            file_write.write(line + add_on_end)
                        elif add_on_star is not None:
                            file_write.write(add_on_star + line)
                        elif word_old and word_new and add_on_end is not None:
                            file_write.write(line.replace(word_old, word_new))
                            file_write.write(line + add_on_end)
                        elif word_old and word_new and add_on_star is not None:
                            file_write.write(line.replace(word_old, word_new))
                            file_write.write(add_on_star + line)
    except Exception as error:
        raise Exception(f'Error: {error}')

# NOTE => Create a temporary file and write the bytes data to it.
@logger.catch()
def temporary_file(bytes_data: bytes, suffix_ext: Optional[str]='test.txt', dir: Optional[str]=None, delete: bool=False) -> str:
    """Create a temporary file and write the bytes data to it.

    Args:
        `bytes_data` (bytes): The bytes data to write to the temporary file.
        `suffix_ext` (str, optional): The suffix or extension of the temporary file. Defaults to 'test.txt'.
        `dir` (str, optional): The directory in which to create the temporary file. Defaults to None.
        `delete` (bool, optional): Whether to delete the temporary file when closed. Defaults to False.

    Returns:
        str: The path of the temporary file that was created.

    Raises:
        Exception: If an error occurs during the creation of the temporary file.

    Example:
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

    Notes:
        - This function creates a temporary file using the `NamedTemporaryFile` function from the `tempfile` module.
        - The `bytes_data` is written to the temporary file in binary mode.
        - The `suffix_ext` parameter allows specifying the suffix or extension of the temporary file.
        - The `dir` parameter specifies the directory where the temporary file will be created. If None, the default system directory is used.
        - The `delete` parameter determines whether the temporary file will be deleted when closed. If True, the file is automatically deleted.
    """
    try:
        with tempfile.NamedTemporaryFile(mode='wb', suffix=suffix_ext, prefix=None, encoding=None, dir=dir, delete=delete) as temp_file:
            temp_file.write(bytes_data) # DESC => input as bytes
            temp_file.flush()
            temp_file_path = temp_file.name # DESC => retrieve the name of the temp file just created
    except Exception as error:
        raise Exception(f'Error creating temporary file: {error}')
    return temp_file_path

# NOTE => Searches for a specified content in a module file and replaces it with new content.
@logger.catch()
def search_and_edite_module(
    object_defined: object, 
    object_content_old: object=None, 
    content_old: str=None, 
    content_new: str=None, 
    overwrite_file: bool=False, 
    logs: Optional[LoggerHandle]=None) -> Any:
    """Searches for a specified content in a module file and replaces it with new content.

    Args:
        `object_defined` (object): The object defined in the module.
        `object_content_old` (object, optional): The object that contains the old content. Defaults to None.
        `content_old` (str, optional): The old content to search for. Use this argument if object_content_old is not provided. Defaults to None.
        `content_new` (str, optional): The new content to replace with. Defaults to None.
        `overwrite_file` (bool, optional): Whether to overwrite the module file with the resulting data. Defaults to False.
        `logs` (Optional[LoggerHandle], optional): An instance of the `LoggerHandle` class for logging purposes.

    Returns:
        None

    Raises:
        ModuleNotFoundError: If the module is not found.

    Example:
    ```python
        class MyClass:
            def __init__(self):
                self.value = 42

        # Search and replace content in the module
        search_and_edite_module(MyClass, content_old='value = 42', content_new='value = 50')
    ```

    Notes:
        - This function searches for the specified content (old content) in the module file and replaces it with new content.
        - The content can be provided either through the `object_content_old` argument, which takes an object and extracts its source code, or directly through the `content_old` argument.
        - The `content_new` argument specifies the new content to replace the old content.
        - If `overwrite_file` is True, the original module file is overwritten with the resulting changes. Otherwise, a new file with the edits is created.
        - The encoding of the module file is automatically detected using the `chardet` library.
        - A backup file with the extension `.bak` is created before overwriting the original file.
        - The function returns True if the content was successfully replaced, and False otherwise.
        - If the module is not found, a `ModuleNotFoundError` is raised.
        - The `logs` parameter is optional. If provided, it should be an instance of the `LoggerHandle` class for logging purposes.
    """
    try:
        _PATH_PACKAGES_ = os.path.join(inspect.getfile(object_defined))
        if object_content_old is not None:
            if isinstance(object_content_old, (object)):
                _SOURCE_CODE_PACKAGES_ = inspect.getsource(object_content_old)
        else:
            _SOURCE_CODE_PACKAGES_ = content_old
        CONFIG_CODE = content_new

        # DESC => read string and convert to bytesIO.
        with BytesIO(initial_bytes=_SOURCE_CODE_PACKAGES_.encode()) as _bytesIO_0:
            _content_old_ = _bytesIO_0.read()
            detect_encoding = chardet.detect(_content_old_) # DESC => read and detect encoding

            # DESC => read string and convert to bytesIO.
            with BytesIO(initial_bytes=CONFIG_CODE.encode()) as __bytesIO__1:
                _content_new_ = __bytesIO__1.read()

                # DESC => read file
                with open(file=_PATH_PACKAGES_, mode='rt') as file_read:
                    _bytesIO_file_ = BytesIO(initial_bytes=file_read.read().encode())
                    _content_file_ = _bytesIO_file_.getvalue()

                    # DESC => split text filename
                    name, ext = os.path.splitext(os.path.basename(str(_PATH_PACKAGES_)))

                    # DESC => get path to file
                    loca = _PATH_PACKAGES_
                    if loca.find('/') == -1:
                        split_location = str('\\'.join(loca.split('\\')[0:-1]))
                    else:
                        split_location = str('/'.join(loca.split('/')[0:-1]))

                    if overwrite_file:
                        if not os.path.isfile(str(os.path.join(split_location, str(name + ext + '.bak')))):
                            with open(file=str(os.path.join(split_location, str(name + ext + '.bak'))), mode='wt') as file_write_backup:
                                file_write_backup.write(_content_file_.decode(encoding=detect_encoding['encoding']))
                        # DESC => overrite the input file with the resulting data
                        with open(file=_PATH_PACKAGES_, mode='wt') as file_write:
                            # DESC => check if string present in a file
                            if _content_file_.find(_content_old_) != -1:
                                logs.info(f'[{_content_old_}] <= Exists in file.') if isinstance(logs, LoggerHandle) else None
                                if _content_old_ in _content_file_:
                                    file_write.write(_content_file_.replace(_content_old_, _content_new_).decode(encoding=detect_encoding['encoding']))
                                    return logs.success(f'Content replace in file: {name + ext}') if isinstance(logs, LoggerHandle) else None
                            else:
                                return logs.warning(f'Content does not exist in a file: {name + ext}!') if isinstance(logs, LoggerHandle) else None
                    else:
                        # DESC => overrite the file with the resulting data
                        with open(file=str(os.path.join(split_location, str(name + '_edit' + ext))), mode='wt') as file_write:
                            # DESC => check if string present in a file
                            if _content_file_.find(_content_old_) != -1:
                                logs.info(f'[{_content_old_}] <= Exists in file.') if isinstance(logs, LoggerHandle) else None
                                if _content_old_ in _content_file_:
                                    file_write.write(_content_file_.replace(_content_old_, _content_new_).decode(encoding=detect_encoding['encoding']))
                                    return logs.success(f'Content replace in file: {str(name + "_edit" + ext)}') if isinstance(logs, LoggerHandle) else None
                            else:
                                return logs.warning(f'Content does not exist in a file: {name + ext }!') if isinstance(logs, LoggerHandle) else None
    except ModuleNotFoundError as error:
        raise logs.error(f'Module Not Found!: {object_defined}')

# NOTE => Encode a file into base64 and optionally write the encoded data to a file.
@logger.catch()
def encode_file_bytes(encoding_file: Optional[Union[str, List[str], Tuple[str]]]=None, file_output: bool=True, overwrite_file: bool=False) -> str:
    """Encode a file into base64 and optionally write the encoded data to a file.

    Args:
        `encoding_file` (Optional[Union[str, List[str], Tuple[str]]]): A path to a single file or a list of file paths to encode.
        `file_output` (bool, optional): Flag to determine if the encoded data should be written to a file or returned as a list.
        `overwrite_file` (bool, optional): Flag to determine if the existing file should be overwritten when saving the encoded data.

    Returns:
        str: A list of encoded file data if `file_output` is False.

    Raises:
        FileNotFoundError: If the specified file path is not found.

    Example:
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
    """
    LIST_NAMES = [] # <= NOTE to stored file name.
    LIST_FILES_ENCODE = [] # <= NOTE to stored file in code base64.
    DATA_ENCODE = []

    if isinstance(encoding_file, (str)):
        try:
            STRING_PATH = encoding_file

            # DESC => split text filename
            name, ext = os.path.splitext(os.path.basename(str(STRING_PATH)))

            # DESC => get path to file
            loca = STRING_PATH
            if loca.find('/') == -1:
                split_location = str('\\'.join(loca.split('\\')[0:-1]))
            else:
                split_location = str('/'.join(loca.split('/')[0:-1]))

            # DESC => open and read file as bytes
            with open(file=STRING_PATH, mode='rb') as file_read:
                _content_ = file_read.read()

                # DESC => encoding file with encodebytes16
                encoding_file_base64 = base64.b16encode(_content_)

                LIST_NAMES.append(str(name.replace('-', '_')+ext.replace('.', '_')))
                LIST_FILES_ENCODE.append(encoding_file_base64)
                #LIST_FILES_ENCODE.append(encoding_file_base64.decode(encoding='utf-8')) # <= NOTE the base64 string without 'b'/bytes

            if file_output:
                if overwrite_file:
                    with open(file=str(os.path.join(split_location, str('encode.txt'))), mode='wt') as file_write:
                        file_write.write(f'\n{LIST_NAMES[0]}_data = {LIST_FILES_ENCODE[0]}')
                else:
                    with open(file=str(os.path.join(split_location, str('encode_cp.txt'))), mode='wt') as file_write:
                        file_write.write(f'\n{LIST_NAMES[0]}_data = {LIST_FILES_ENCODE[0]}')
            else:
                for name, encoded_data in zip(LIST_NAMES, LIST_FILES_ENCODE):
                    DATA_ENCODE.append(str(name + ': ' + encoded_data))
                return DATA_ENCODE
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {STRING_PATH}")
    elif isinstance(encoding_file, (list, tuple)):
        STRING_LISTS = encoding_file

        # DESC => open and read file as bytes
        for file in STRING_LISTS:
            # DESC => get path to file
            loca = file
            if loca.find('/') == -1:
                split_location = str('\\'.join(loca.split('\\')[0:-1]))
            else:
                split_location = str('/'.join(loca.split('/')[0:-1]))

            try:
                with open(file=file, mode='rb') as file_read:
                    _content_ = file_read.read()

                    # DESC => encoding file with encodebytes16
                    encoding_file_base64 = base64.b16encode(_content_)

                    # DESC => split text filename
                    name, ext = os.path.splitext(os.path.basename(str(file)))
                    LIST_NAMES.append(str(name.replace('-', '_')+ext.replace('.', '_')))
                    LIST_FILES_ENCODE.append(encoding_file_base64.decode(encoding='utf-8')) # <= NOTE the base64 string without 'b'/bytes
            except FileNotFoundError:
                raise FileNotFoundError(f"File not found: {file}")

        if file_output:
            if overwrite_file:
                with open(file=str(os.path.join(split_location, str('encode.txt'))), mode='wt') as file_write:
                    for name, encoded_data in zip(LIST_NAMES, LIST_FILES_ENCODE):
                        file_write.write(f'\n{name}_data = {encoded_data}')
            else:
                with open(file=str(os.path.join(split_location, str('encode_cp.txt'))), mode='wt') as file_write:
                    for name, encoded_data in zip(LIST_NAMES, LIST_FILES_ENCODE):
                        file_write.write(f'\n{name}_data = {encoded_data}')
        else:
            for name, encoded_data in zip(LIST_NAMES, LIST_FILES_ENCODE):
                DATA_ENCODE.append(str(name + ': ' + encoded_data))
            return DATA_ENCODE

# NOTE => Decode a file encoded with base64.
@logger.catch()
def decode_file_bytes(decode_file: bytes = None) -> bytes:
    """Decode a file encoded with base64.

    Args:
        `decode_file` (bytes): The file data encoded in base64.

    Returns:
        bytes: The decoded file content as bytes.

    Example:
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
    """
    # DESC => decode content with bytes16
    decode_content_base64 = base64.b16decode(decode_file)
    return decode_content_base64

# NOTE => Detect if the given argument is a function.
@logger.catch()
def detect_variable(arge: Any = None) -> bool:
    """Detect if the given argument is a function.

    Args:
        `arge` (Any): The variable to check.

    Returns:
        bool: True if the variable is a function, False otherwise.

    Example:
    ```python
        # Check if a variable is a function
        >>> detect_variable(print)
        # Output:
        # True
    ```
    """
    if isinstance(arge, FunctionType):
        return True
    else:
        return False

# NOTE => Measure the average color lightness based on different methods.
@logger.catch()
def measuring_average_color_lightness(r: int = 0, g: int = 0, b: int = 0, factor: float = 0.1, measuring: Literal['Max', 'Average', 'Between', 'Geometric'] = None) -> Tuple[int, int, int]:
    """Measure the average color lightness based on different methods.

    Args:
        `r` (int, optional): The red component of the color (default is 0).
        `g` (int, optional): The green component of the color (default is 0).
        `b` (int, optional): The blue component of the color (default is 0).
        `factor` (float, optional): The scaling factor for lightness (default is 0.1).
        `measuring` (Literal['Max', 'Average', 'Between', 'Geometric'], optional): The method to measure lightness.
            Can be one of 'Max', 'Average', 'Between', 'Geometric'. Defaults to None.

    Returns:
        Tuple[int, int, int]: The RGB values of the resulting color.

    Example:
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

    Notes:
        - This function calculates the average color lightness based on different methods: 'Max', 'Average', 'Between', 'Geometric'.
        - The resulting color is returned as RGB values.
    """
    # DESC => lightness be equal to the max of the RGB values (L = max(R, G, B) / 255)
    lightness_max = max(r, g, b) / 255

    # DESC => average of the RGB values (L = (R + G + B) / (3 * 255))
    lightness_average = (r + g + b) / (3 * 255)

    # DESC => average of between the smallest min and largest max in RGB values (L = (min(R, G, B) + max(R, G, B)) / (2 * 255))
    lightness_between = (min(r, g, b) + max(r, g, b)) / (2 * 255)

    # DESC => the scaled geometric mean is the next measure of lightness (L = ((R * G * B)^(1/3)) / 255)
    lightness_geometric = ((r * g * b) ** (1/3)) / 255 # DESC => operator is (**) == ^

    # DESC => covert rgb to hls
    hue, lightness, saturation = colorsys.rgb_to_hls(r=(r/255.0), g=(g/255.0), b=(b/255.0))

    # DESC => factor lightness manual
    lightness_factor = max(min(lightness * factor, 1.0), 0.0)

    if measuring is not None:
        if measuring == 'Max':
            # NOTE => covert hls to rgb
            red, green, bleu = colorsys.hls_to_rgb(h=hue, l=lightness_max, s=saturation)
        elif measuring == 'Average':
            # NOTE => covert hls to rgb
            red, green, bleu = colorsys.hls_to_rgb(h=hue, l=lightness_average, s=saturation)
        elif measuring == 'Between':
            # NOTE => covert hls to rgb
            red, green, bleu = colorsys.hls_to_rgb(h=hue, l=lightness_between, s=saturation)
        elif measuring == 'Geometric':
            # NOTE => covert hls to rgb
            red, green, bleu = colorsys.hls_to_rgb(h=hue, l=lightness_geometric, s=saturation)
    else:
        # DESC => covert hls to rgb
        red, green, bleu = colorsys.hls_to_rgb(h=hue, l=lightness_factor, s=saturation)
    return int(red*255), int(green*255), int(bleu*255)

# NOTE => Decorator function to measure the execution time of a given function
@logger.catch()
def wrapper_decorator_timetask(suffix: str='Execution time seconds:', seconds: bool=True, logs: Optional[LoggerHandle]=None):
    """Decorator function to measure the execution time of a given function.

    Args:
        `suffix` (str, optional): The suffix to be used in the output. Defaults to 'Execution time:'.
        `seconds` (bool, optional): Whether to display the time in seconds or formatted time. Defaults to True.
        `logs` (Optional[LoggerHandle], optional): An instance of the `LoggerHandle` class for logging purposes.

    Returns:
        Callable[..., Any]: The wrapper function that measures the execution time.

    Example:
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

    Notes:
        - The `logs` parameter is optional. If provided, it should be an instance of the `LoggerHandle` class for logging purposes.
    """
    # DESC => The wrapper function serves as the actual decorator. It takes the decorated function as its argument.
    def wrapper(function: Callable[..., None]) -> Callable[..., None]:
        def wrapped_function(*args, **kwargs) -> str:
            # DESC => get the start task time
            start_task_time = time.time()
            start_CPU_execution_time = time.process_time()

            # DESC => function execution here
            function(*args, **kwargs)

            # DESC => get the end task time
            end_task_time = time.time()
            end_CPU_execution_time = time.process_time()
            
            elapsed_time = end_task_time - start_task_time
            elapsed_CPU_time = end_CPU_execution_time - start_CPU_execution_time
            time_format = time.strftime("%H{}:%M{}:%S{}", time.gmtime(elapsed_time)).format('h', 'm', 's')

            if seconds:
                elapsed_str = str(f'{suffix} {round(elapsed_time, 2)}s')
            else:
                elapsed_str = str(f'{suffix} {time_format}')
            
            logs.info(elapsed_str) if isinstance(logs, LoggerHandle) else None
            return elapsed_str
        return wrapped_function
    return wrapper

# NOTE => Decorator sample.
def wrapper_decorator():
    """Decorator sample.

    Returns:
        The decorator function.

    Notes:
        - You can use this decorator by applying the `@wrapper_decorator` decorator above any function definition.
    """
    def wrapper(function):
        def wrap_function(*args, **kwargs):
            '''this function calls the decorated function'''
            # => DESC function execution here
            function(*args, **kwargs)
            # => DESC function execution here
        return wrap_function
    return wrapper

# NOTE => Decorator to create threaded functions.
@logger.catch()
def wrapper_decorator_threaded(name_thread: str=None, daemon: bool=True):
    """Decorator to create threaded functions.

    Args:
        `name_thread` (str, optional): The name of the thread. Defaults to None.
        `daemon` (bool, optional): Whether the thread should be a daemon thread. Defaults to True.

    Returns:
        Callable[..., threading.Thread]: The wrapper function that creates and starts the thread.

    Example:
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
    """
    # DESC => The wrapper function serves as the actual decorator. It takes the decorated function as its argument.
    def wrapper(function: Callable[..., None]) -> Callable[..., Thread]:
        def wrapped_function(queue: Queue, *args, **kwargs):
            """function is responsible for calling the decorated function and putting the result in a queue.
            It takes a queue and the arguments of the decorated function as its parameters."""
            result = function(*args, **kwargs)
            queue.put(result)

        def wrap(*args, **kwargs):
            """function is the function returned from the decorator.
            It creates a new thread and attaches a result queue to the thread object.
            This function starts the thread, executes the decorated function in the thread,
            and returns the thread object."""

            result_queue = Queue()
            thread = Thread(name=name_thread, target=wrapped_function, args=(result_queue,)+args, kwargs=kwargs, daemon=daemon)
            thread.start()
            thread.result_queue = result_queue
            return thread

        return wrap
    return wrapper

# NOTE => Detects the current platform or operating system.
@logger.catch()
def platform_system_detect() -> Optional[str]:
    """Detects the current platform or operating system.

    Returns:
        Optional[str]: The platform name. Can be one of the following:
            - `'Windows'` for Windows systems.
            - `'Mac'` for macOS systems.
            - `'Linux'` for Linux systems.
            - `'emscripten'` for emscripten platform.
            - `None` if the platform cannot be determined.

    Example:
    ```python
        platform = platform_system_detect()
        print(platform)
        # Output: 'Windows' (if running on Windows)
    ```
    """
    if platform.system() == 'Windows':
        platform_is = 'Windows'
    elif platform.system() == 'Darwin':
        platform_is = 'Mac'
    elif platform.system() == 'Linux':
        platform_is = 'Linux'
    elif sys.platform == "emscripten":
        platform_is = 'emscripten'
    else:
        platform_is = None
    return platform_is

# NOTE => Splits a file path into its directory name, base name, and extension.
@logger.catch()
def split_file_path(file_path: str) -> tuple[str, str, str]:
    """Splits a file path into its directory name, base name, and extension.

    Args:
        `file_path` (str): The file path to split.

    Returns:
        tuple[str, str, str]: A tuple containing the directory name, base name, and extension of the file.

    Raises:
        TypeError: If the input argument `file` is not a string.

    Example:
    ```python
        dirname, basename, extension = split_file_path('/path/to/file.txt')
        print(dirname) # <= '/path/to'
        print(basename) # <= 'file'
        print(extension) # <= '.txt'
    ```
    """
    if not isinstance(file_path, str):
        raise TypeError("The input argument 'file' must be a string.")

    # NOTE => split file path
    basename, extension = os.path.splitext(os.path.basename(file_path))
    dirname, basename = os.path.split(os.path.splitext(file_path)[0])
    return dirname, basename, extension

# NOTE => Returns the height, width, and number of channels of an image.
@logger.catch()
def get_h_w_c_to_image(image_array: np.ndarray) -> Tuple[int, int, int]:
    """Returns the height, width, and number of channels of an image.

    Args:
        `image_array` (np.ndarray): The image array.

    Returns:
        Tuple[int, int, int]: A tuple containing the height, width, and number of channels of the image.

    Raises:
        ValueError: If the input array is not a valid image.

    Example:
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

    Notes:
        - This function assumes that the input array represents a valid image.
        - The height and width are obtained from the first two dimensions of the array shape.
        - If the array has a dimension of 2, it is treated as a grayscale image with one channel.
        - For color images, the number of channels is obtained from the third dimension of the array shape.
    """
    if not isinstance(image_array, np.ndarray):
        raise ValueError("Input must be a NumPy array.")

    height, width = image_array.shape[:2]
    channels = 1 if image_array.ndim == 2 else image_array.shape[2]
    return height, width, channels

# NOTE => Returns a list of available image file formats supported by OpenCV.
def get_opencv_formats() -> list:
    """Returns a list of available image file formats supported by OpenCV.

    Returns:
        list: A list of available image file formats.

    Example:
    ```python
        formats = get_opencv_formats()
        print(formats)
        [".bmp", ".dib", ".jpg", ".jpeg", ".jpe", ".jp2", ".png", ".webp", ".tif", ".tiff", ".pbm", ".pgm", ".ppm", ".pxm", ".pnm", ".sr", ".ras", ".exr", ".hdr", ".pic"]
    ```
    """
    available_formats = [
        # NOTE Bitmaps
        ".bmp",
        ".dib",
        # NOTE JPEG
        ".jpg",
        ".jpeg",
        ".jpe",
        ".jp2",
        # NOTE Portable Network Graphics
        ".png",
        ".webp",
        ".tif",
        ".tiff",
        # NOTE Portable image format
        ".pbm",
        ".pgm",
        ".ppm",
        ".pxm",
        ".pnm",
        # NOTE Sun Rasters
        ".sr",
        ".ras",
        # NOTE OpenEXR
        ".exr",
        # NOTE Radiance HDR
        ".hdr",
        ".pic",
    ]
    return available_formats

# NOTE => Returns a list of available image file formats supported by Pillow.
def get_pillow_formats() -> list:
    """Returns a list of available image file formats supported by Pillow.

    Returns:
        list: A list of available image file formats.

    Example:
    ```python
        formats = get_pillow_formats()
        print(formats)
        [".bmp", ".dib", ".xbm", ".dds", ".eps", ".psd", ".gif", ".icns", ".ico", ".jpg", ".jpeg", ".jfif", ".jp2", ".jpx", ".msp", ".pcx", ".sgi", ".png", ".webp", ".tiff", ".tif", ".apng", ".pbm", ".pgm", ".ppm", ".pnm", ".tga"]
    ```
    """
    available_formats = [
        # NOTE Bitmaps
        ".bmp",
        ".dib",
        ".xbm",
        # NOTE DDS
        ".dds",
        # NOTE EPS
        ".eps",
        # NOTE PSD
        ".psd",
        # NOTE GIF
        ".gif",
        # NOTE Icons
        ".icns",
        ".ico",
        # NOTE JPEG
        ".jpg",
        ".jpeg",
        ".jfif",
        ".jp2",
        ".jpx",
        # NOTE Randoms
        ".msp",
        ".pcx",
        ".sgi",
        # NOTE Portable Network Graphics
        ".png",
        ".webp",
        ".tiff",
        ".tif",
        # NOTE APNG
        ".apng",
        # NOTE Portable image format
        ".pbm",
        ".pgm",
        ".ppm",
        ".pnm",
        # NOTE TGA
        ".tga",
    ]
    return available_formats

# NOTE => Imports module from a file path. and returns an object from a specified module.
@logger.catch()
def import_from(module: str, name: str):
    """Imports module from a file path. and returns an object from a specified module.

    Args:
        `module` (str): The module path.
        `name` (str): The name of the object to import.

    Returns:
        Any: The imported object.

    Example:
    ```python
        path_file_module = "folder0.folder1.folder2.myfile.mymethod"
        name_function = "my_function"

        my_function = import_from(path_file_module, name_function)
        my_function()
    ```

    Notes:
        - This function uses the `__import__` function to import the module dynamically.
        - The `fromlist` parameter is provided to ensure the specified name is included in the imported module.
        - The `getattr` function is used to retrieve the specified name from the imported module.
    """
    module = __import__(str(module), fromlist=[str(name)])
    return getattr(module, name)

# NOTE => Imports a module from a file path.
@logger.catch()
def import_lib(module_name: str, file_path: str) -> object:
    """Imports a module from a file path.

    Args:
        `module_name` (str): The name of the module.
        `file_path` (str): The path to the module file.

    Returns:
        object: The imported module.

    Raises:
        Exception: If an error occurs during the import process.

    Example:
    ```python
        # Import the module "my_module" from the file "my_module.py"
        my_module = import_lib("my_module", "/path/to/my_module.py")
        my_module()
    ```

    Notes:
        - This function uses the `util.spec_from_file_location` function to create a module specification based on the file path and desired module name.
        - The `util.module_from_spec` function is used to create a new module object from the module specification.
        - The `sys.modules` dictionary is updated with the newly created module object using the desired module name as the key.
        - The `exec_module` method of the module specification loader is called to execute the module and populate it with its contents.
        - The imported module object is returned.
    """
    try:
        spec = util.spec_from_file_location(module_name, file_path)
        module = util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        return module
    except Exception as error:
        raise Exception(f'Error: {error}')

# NOTE => Retrieves classes and/or functions from modules in a directory.
@logger.catch()
def retrieves_modules_from_dir(
    directory_path: str = '',
    specific_file_name: Optional[str] = None,
    skip_file: Optional[List[str]] = None,
    skip_module: Optional[List[str]] = None,
    get_classes: bool = True,
    get_functions: bool = True
) -> Union[Dict[str, type], Dict[str, callable], Tuple[Dict[str, type], Dict[str, callable]]]:
    """Retrieves classes and/or functions from modules in a directory.

    Args:
        `directory_path` (str): The path to the directory containing the modules.
        `specific_file_name` (str, optional): The name of a specific file to retrieve modules from. Use '*.py' to get all .py files. Defaults to None.
        `skip_file` (List[str], optional): A list of files to skip. Defaults to None.
        `skip_module` (List[str], optional): A list of modules to skip. Defaults to None.
        `get_classes` (bool, optional): Whether to retrieve classes from the modules. Defaults to True.
        `get_functions` (bool, optional): Whether to retrieve functions from the modules. Defaults to True.

    Returns:
        Union[Dict[str, type], Dict[str, callable], Tuple[Dict[str, type], Dict[str, callable]]]:
            A dictionary of classes, a dictionary of functions, or a tuple containing both dictionaries.

    Raises:
        None.

    Example:
    ```python
        # Retrieve all classes from the modules in the specified directory
        classes = retrieves_modules_from_dir(directory_path='/path/to/modules_directory', get_classes=True, get_functions=False)

        # Retrieve all functions from the modules in the specified directory
        functions = retrieves_modules_from_dir(directory_path='/path/to/modules_directory', get_classes=False, get_functions=True)

        # Retrieve both classes and functions from the modules in the specified directory
        classes, functions = retrieves_modules_from_dir(directory_path='/path/to/modules_directory', get_classes=True, get_functions=True)
    ```


    """
    # DESC => Initialization
    package_directory_path = os.path.join(directory_path)
    package_name = os.path.basename(package_directory_path)

    get_files = glob(os.path.join(package_directory_path, f'{specific_file_name}.py'))
    pattern_extensions = ['.py']

    skip_file = [] if skip_file is None else skip_file
    skip_module = [] if skip_module is None else skip_module

    all_base_classes = {}
    all_base_functions = {}

    # DESC => Process specific file or all files in the directory
    if specific_file_name is not None:
        if os.path.isdir(package_directory_path): # DESC => check if folders exists.
            for file in get_files:
                if str(file).endswith(tuple(pattern_extensions)): # DESC => check if file extension available in list extensions.
                    file_current = os.path.abspath(os.path.join(file)) # DESC => make path to file
                    filename_current = os.path.splitext(os.path.basename(file_current))[0]

                    if filename_current not in skip_file:
                        try:
                            # DESC => trying to find module on sys.path
                            #module_name = __import__(filename_current)
                            module_name = importlib.import_module(filename_current, package=package_name)
                        except:
                            try:
                                module_name = import_lib(filename_current, file_current)
                            except:
                                module_name = importlib.import_module('.' + filename_current, package=package_name)
                        for item in dir(module_name):
                            if item not in skip_module:

                                item_getattr = getattr(module_name, item)
                                if not item.startswith('__'): # DESC => Ignore __ files
                                    if inspect.isclass(item_getattr):
                                        if get_classes:
                                            all_base_classes[item] = item_getattr
                                    if inspect.isfunction(item_getattr):
                                        if get_functions:
                                            all_base_functions[item] = item_getattr
    else:
        if os.path.isdir(package_directory_path): # DESC => check if folders exists.
            for foldername, subfolders, filenames in os.walk(package_directory_path, topdown=True):
                for filename in filenames:
                    if str(filename).endswith(tuple(pattern_extensions)): # DESC => check if file extension available in list extensions.
                        file_current = os.path.abspath((os.path.join(foldername, filename))) # DESC => make path to file
                        filename_current = os.path.splitext(os.path.basename(file_current))[0]

                        if filename_current not in skip_file:
                            try:
                                # DESC => trying to find module on sys.path
                                #module_name = __import__(filename_current)
                                module_name = importlib.import_module(filename_current, package=package_name)
                            except:
                                try:
                                    module_name = import_lib(filename_current, file_current)
                                except:
                                    module_name = importlib.import_module('.' + filename_current, package=package_name)
                            for item in dir(module_name):
                                if item not in skip_module:

                                    item_getattr = getattr(module_name, item)
                                    if not item.startswith('__'): # DESC => Ignore __ files
                                        if inspect.isclass(item_getattr):
                                            if get_classes:
                                                all_base_classes[item] = item_getattr
                                        if inspect.isfunction(item_getattr):
                                            if get_functions:
                                                all_base_functions[item] = item_getattr

    # DESC => Return retrieved classes, functions, or both
    if get_classes and get_functions is False:
        return all_base_classes
    elif get_functions and get_classes is False:
        return all_base_functions
    else:
        return all_base_classes, all_base_functions

# NOTE => Retrieves image names or paths from a directory.
@logger.catch()
def retrieves_image_from_dir(
    directory_path: str,
    pattern_extensions: Optional[List[str]] = None,
    return_names: bool = True,
    return_paths: bool = False
) -> Union[List[str], List[str], Tuple[List[str], List[str]]]:
    """Retrieves image names or paths from a directory.

    Args:
        `directory_path` (str): The path to the directory containing the images.
        `pattern_extensions` (List[str], optional): A list of file extensions to filter the images. Defaults to None.
        `return_names` (bool, optional): Whether to return image names. Defaults to True.
        `return_paths` (bool, optional): Whether to return image paths. Defaults to False.

    Returns:
        Union[List[str], List[str], Tuple[List[str], List[str]]]:
            A list of image names, a list of image paths, or a tuple containing both lists.

    Raises:
        None.

    Example:
    ```python
        # Retrieve image names from the directory
        image_names = retrieves_image_from_dir(directory_path='/path/to/images_directory', return_names=True, return_paths=False)

        # Retrieve image paths from the directory
        image_paths = retrieves_image_from_dir(directory_path='/path/to/images_directory', return_names=False, return_paths=True)

        # Retrieve both image paths and names from the directory
        image_paths, image_names = retrieves_image_from_dir(directory_path='/path/to/images_directory', return_names=True, return_paths=True)
    ```
    """
    # DESC => Initialization
    directory = directory_path
    pattern_extensions = [] if pattern_extensions is None else pattern_extensions
    images_path = []
    images_name = []

    # DESC => Retrieve images from the directory
    if os.path.isdir(directory): # DESC => check if folders exists.
        for file in glob(pathname=os.path.join(directory, '*')):
            if str(file).endswith(tuple(pattern_extensions)): # DESC => check if file extension available in list extensions.
                file_current = os.path.abspath(os.path.join(file)) # DESC => make path to file
                filename_current = os.path.splitext(os.path.basename(file_current))[0]

                images_name.append(filename_current)
                images_path.append(file_current)

    # DESC => Return image names, image paths, or both
    if return_names and return_paths is False:
        return images_name
    elif return_paths and return_names is False:
        return images_path
    else:
        return images_path, images_name

# NOTE => Executes a target function or action safely, catching specified exceptions and returning a default value or the exception itself.
@logger.catch()
def safe_exception_execute(
    exception: Union[Any, Tuple[Any]]=Exception,
    default: Any = None,
    target: Optional[Any] = None,
    args: List[Any] = [],
    kwargs: Optional[Dict[Any, Any]] = None
) -> Any:
    """Executes a target function or action safely, catching specified exceptions and returning a default value or the exception itself.

    Args:
        `exception` (Union[Any, Tuple[Any]]): The exception or tuple of exceptions to catch.
        `default` (Any, optional): The default value to return if an exception is caught. Defaults to None.
        `target` (Optional[Any], optional): The function or action to execute. Defaults to None.
        `args` (List[Any], optional): The arguments to pass to the target function. Defaults to [].
        `kwargs` (Optional[Dict[Any, Any]], optional): The keyword arguments to pass to the target function. Defaults to None.

    Returns:
        Any: The result of the target function or the default value if an exception is caught.

    Raises:
        Exception: If the target function raises an exception and no default value is provided.

    Example:
    ```python
        # Example 1: Safely execute a function and return the result or a default value
        result = safe_exception_execute(exception=ZeroDivisionError, default=0, target=lambda: 10 / 0)

        # Example 2: Safely execute a function with arguments and return the result or a default value
        result = safe_exception_execute(exception=FileNotFoundError, default='Not found', target=open, args=['nonexistent.txt'], kwargs={'mode': 'r'})

        # Example 3: Safely execute a function and raise the caught exception if no default value is provided
        result = safe_exception_execute(exception=KeyError, target=lambda: my_dict['key'])
    ```
    """
    if len(args) != 0:
        if kwargs is not None:
            try:
                action = target(*args, **kwargs)
                return action
            except exception as value:
                if default is not None:
                    return default
                else:
                    return value
    else:
        try:
            action = target()
            return action
        except exception as value:
            if default is not None:
                return default
            else:
                return value

# NOTE => Retrieves a list of parameter names from a Python function, method, or class.
@logger.catch()
def get_list_parameter_names_from_fun(func_or_method: Any, method_py2: bool=False) -> Union[inspect.FullArgSpec, inspect.Signature]:
    """Retrieves a list of parameter names from a Python function, method, or class.

    Args:
        `func_or_method` (Any): The function, method, or class to inspect.
        `method_py2` (bool, optional): Flag indicating whether to use Python 2 or Python 3 method for retrieval. Defaults to False (Python 3).

    Returns:
        Union[inspect.FullArgSpec, inspect.Signature]: The parameter information retrieved from the function, method, or class.

    Raises:
        TypeError: If the provided object is not a function, method, or class.

    Example:
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
    """
    if checked_instances(func_or_method, 'function') or checked_instances(func_or_method, 'method') or checked_instances(func_or_method, 'class'):
        if method_py2:
            return inspect.getargspec(func_or_method)  # <= DESC => For Python 2
        else:
            return inspect.signature(func_or_method)  # <= DESC => For Python 3
    else:
        raise TypeError("The provided object is not a function, method, or class.")

# NOTE => Checks the type of the provided object against the specified type checker.
@logger.catch()
def checked_instances(inspecter: Any, type_checker: Literal['function', 'method', 'class', 'code', 'object', 'list', 'int', 'str', 'bool', 'none']='str', logs: Optional[LoggerHandle]=None) -> bool:
    """Checks the type of the provided object against the specified type checker.

    Args:
        `inspecter` (Any): The object to check the type of.
        `type_checker` (Literal['function', 'method', 'class', 'code', 'object', 'list', 'int', 'str', 'bool', 'none'], optional):
            The type checker to use. Defaults to 'str'.
        `logs` (Optional[LoggerHandle], optional): An instance of the `LoggerHandle` class for logging purposes.

    Returns:
        bool: True if the object matches the specified type checker, False otherwise.

    Raises:
        Exception: If an error occurs during type checking.

    Example:
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

    Notes:
        - The `logs` parameter is optional. If provided, it should be an instance of the `LoggerHandle` class for logging purposes.
    """
    try:
        if type_checker == 'function':
            return inspect.isfunction(inspecter)
        elif type_checker == 'method':
            return inspect.ismethod(inspecter)
        elif type_checker == 'class':
            return inspect.isclass(inspecter)
        elif type_checker == 'code':
            return inspect.iscode(inspecter)
        elif type_checker == 'list':
            return isinstance(inspecter, List)
        elif type_checker == 'object':
            return isinstance(inspecter, object)
        elif type_checker == 'int':
            return isinstance(inspecter, int)
        elif type_checker == 'str':
            return isinstance(inspecter, str)
        elif type_checker == 'bool':
            return isinstance(inspecter, bool)
        elif type_checker == 'none':
            return inspecter is None
        else:
            logs.info(f'The name: {type_checker} is not in the list of type checkers.') if isinstance(logs, LoggerHandle) else None
    except Exception as error:
        raise logs.error(f'Error: {error}') if isinstance(logs, LoggerHandle) else None

# NOTE => Convert a string representation to an actual boolean value.
def strTobool(val: str):
    """Convert a string representation to an actual boolean value.

    Args:
        `val` (str): The string value to convert.

    Returns:
        bool: The boolean value corresponding to the string representation.

    Raises:
        ValueError: If the input string is not a valid truth value.

    Example:
    ```python
        value1 = strTobool("True")
        print(value1)  # Output: True

        value2 = strTobool("yes")
        print(value2)  # Output: True

        value9 = strTobool("invalid")
        # Output: ValueError: invalid truth value invalid
    ```
    """
    val = val.lower()
    if val in ('y', 'yes', 't', 'true', 'on', '1'):
        return True
    elif val in ('n', 'no', 'f', 'false', 'off', '0'):
        return False
    else:
        raise ValueError(f"Invalid truth value {val}")

# NOTE => Create a tar.gz archive containing specified files and directories.
@logger.catch()
def create_archive_tar_gz(archive_name: Optional[str], source_paths: Optional[Union[str, list]], output_path: Optional[str]=None, logs: Optional[LoggerHandle]=None) -> None:
    """Create a tar.gz archive containing specified files and directories.

    Args:
        `archive_name` (Optional[str]): The name of the output archive file with extension `name.tar.gz`.
        `output_path` (Optional[str]): The path of the output archive file. Defaults to None.
        `source_paths` (Optional[Union[str, list]]): A string or list of strings representing the paths of files or directories
            to be included in the archive. Each string can be a file path or a directory path.
        `logs` (Optional[LoggerHandle], optional): An instance of the `LoggerHandle` class for logging purposes.

    Returns:
        None

    Raises:
        Exception: If any of the specified paths does not exist.

    Example:
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

    Notes:
        - If the source_paths parameter is a string, it adds the individual file or directory
            to the archive.
        - If the source_paths parameter is a list, it adds multiple files or directories to the archive.
        - The archive file will be compressed using the tar.gz format.
        - The `logs` parameter is optional. If provided, it should be an instance of the `LoggerHandle` class for logging purposes.
    """
    try:
        # DESC => Open the tar.gz file for writing
        if output_path is not None:
            output_archive = os.path.join(output_path, archive_name)
        else:
            output_archive = os.path.join(archive_name)

        with tarfile.open(name=output_archive, mode="w:gz") as tar:
            logs.info("I will prepare to created a archive containing files or directories.") if isinstance(logs, LoggerHandle) else None
            if isinstance(source_paths, str):
                # DESC => Add individual file or directory to the archive
                # DESC => Set the arcname to the base name of the file
                if os.path.exists(source_paths):
                    tar.add(source_paths, arcname=os.path.basename(source_paths))
                    logs.success(f"Successful created archive: '{archive_name}' on path {output_archive}") if isinstance(logs, LoggerHandle) else None
                else:
                    logs.error(f"Error: '{source_paths}' does not exist.") if isinstance(logs, LoggerHandle) else None
            elif isinstance(source_paths, list):
                # DESC => Add multiple files or directories to the archive
                for path in source_paths:
                    if os.path.exists(path):
                        # DESC => Add each file with a relative path to preserve directory structure
                        tar.add(path, arcname=os.path.basename(path))
                    else:
                        logs.error(f"Error: '{path}' does not exist.") if isinstance(logs, LoggerHandle) else None
                logs.success(f"Successful created archive: '{archive_name}' on path {output_archive}") if isinstance(logs, LoggerHandle) else None
            else:
                logs.error(f"Error: Invalid '{source_paths}' argument or not a valid directory.") if isinstance(logs, LoggerHandle) else None
    except Exception as error:
        raise Exception(f'Error : {error}')

# NOTE => introspect function parameters.
@logger.catch()
def check_signature_object(func: Callable, logs: Optional[LoggerHandle]=None) -> None:
    """introspect function parameters.

    Args:
        `func` (Callable): The function for check signature parameters.
        `logs` (Optional[LoggerHandle], optional): An instance of the LoggerHandle class for logging.

    Raises:
        ValueError: has no signature

    Returns:
        None

    Example:
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
    """
    try:
        funcname = func.__name__
        sig = inspect.signature(func)

        logs.info(f'Signature {funcname}: {sig}') if isinstance(logs, LoggerHandle) else None

        for position, (name, parameter) in enumerate(sig.parameters.items()):
            logs.info(f"position: {position} name: {name:10.10} kind={parameter.kind.description.replace(' ','_')} | default={parameter.default if parameter.default is not inspect._empty else 'required'} | annotation={parameter.annotation if parameter.annotation is not inspect._empty else '<empty>'}") if isinstance(logs, LoggerHandle) else None
    except ValueError as error:
        raise ValueError(f"`{funcname}` has no signature: ", error)

# NOTE => Check if the first characters in the string match the pattern.
def check_string_match_pattern(string: str, pattern: str, lower_character: bool=None):
    """Check if the characters in the string match the pattern.

    Args:
        `string` (str): The string to be checked.
        `pattern` (str): The pattern to be matched.
        `lower_character` (bool): Whether to match the pattern in lowercase.

    Returns:
        boolen: if True the first characters in the string match the pattern, False otherwise.
    
    Example:
    ```python
        string = "mana"
        sequence = "na"

        if check_string_match_pattern(string, sequence):
            print("ok")
        else:
            raise ValueError("The first characters of the string do not match the sequence")
    ```
    """
    try:
        if lower_character:
            pattern = pattern.lower()
            string = string.lower()

        return pattern == string[:len(pattern)]
    except Exception:
        return False

# NOTE => Get the string before the specified character pattern in the string.
def get_string_before_pattern(string: str, pattern: str=None):
    """Get the string before the specified character pattern in the string.

    Args:
        `string` (str): The string to be processed.
        `pattern` (str): The character pattern to be matched 
            The specified character the first occurrence of the string.

    Returns:
        str: The string before the pattern, or the entire string if the pattern is not found.

    Example:
    ```python
        string = "TEN_K_ROUNDED"
        pattern = "_"
        result = get_string_before_pattern(string, pattern)
        print(result) # Output => TEN
    ```
    """

    index = string.find(pattern)
    if index == -1:
        return string
    else:
        return string[:index]

# NOTE => The time sleep duration with higher accuracy.
def time_sleep_accuracy(sleep_time: Union[int, float], measuring_time: Optional[Literal["monotonic", "performance"]] = None):
    """The time sleep duration with higher accuracy.

    Args:
        `sleep_time` (Union[int, float]): The seconds duration of sleep.
        `measuring_time` (Union[str, None]): The measuring time intervals calculation you can choice "monotonic", "performance".
    
    Returns:
        None.

    Notes:
        - `performance`: The it calculates measuring time intervals value (in fractional seconds) of 
            a clock with the highest available resolution on the system.
            - This is suitable for measuring short durations and is primarily used for performance benchmarking and timing operations.
            - The value returned is based on the system's monotonic clock but may include fractions of a second for higher precision.
            - It can be affected by system clock adjustments, such as time adjustments made by the user or network time synchronization.
        
        - `monotonic`: It returns the value (in fractional seconds) of a clock that cannot go backward and is unaffected by system clock adjustments.
            - This is intended for measuring elapsed time between two points, independent of the system clock.
            - It's useful for tasks such as measuring timeouts, calculating durations, or synchronizing activities.
            - The value returned does not represent an actual date or time; it's only a relative measure of time.
            - It guarantees monotonically increasing values, ensuring that it never goes backward even if the system clock is adjusted.
    """
    if measuring_time == "monotonic":
        measuring = time.monotonic
    elif measuring_time == "performance":
        measuring = time.perf_counter
    else:
        measuring = time.monotonic

    start_time = measuring()
    end_time = start_time + sleep_time
    while measuring() < end_time:
        remaining_time = end_time - measuring()
        time.sleep(remaining_time)

# NOTE => Check if any of the patterns match the characters or strings.
def check_is_matching_pattern(sequence_string: str, pattern: Union[str, List], operator: Literal["search", "findall"] = "search"):
    """Check if any of the patterns match the characters or strings.

    Args:
        `sequence_string` (str): The input string to be to check for matches.
        `pattern` (Union[str, List]): The pattern to match or a list of regular expression patterns to 
            match has an 'r' prefix (indicating it is a raw string).
        `operator` (Literal["search", "findall"]): The check operator the way to check matching 
            if use `"search"` returns boolen for first result, or use `"findall"` to returns list for an found all result.

    Returns:
        (bool | list | None): if use "search" returns boolen, or use "findall" to returns list
    
    Example:
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
    """
    if operator == "search":
        if isinstance(pattern, List):
            # DESC => Combine the elements using the '|' operator.
            pattern = "|".join(pattern)

            # DESC => Find with the combined pattern to find the first match.
            match = re.search(pattern, sequence_string)
        else:
            # DESC => Find the pattern in the input string.
            match = re.search(pattern, sequence_string)
    else:
        if isinstance(pattern, List):
            # DESC => Combine the elements using the '|' operator.
            pattern = "|".join(pattern)

            # DESC => Find with the combined pattern to find the first match.
            match = re.findall(pattern, sequence_string)
        else:
            # DESC => Find the pattern in the input string.
            match = re.findall(pattern, sequence_string)

    # DESC => If a match is found, return True; otherwise, return False.
    return match

########################################################################################################################
# TODO CLASSES MODULES
########################################################################################################################
class TaskTimer:
    """ Task Execution Timer. """
    def __init__(self, *args, **kwargs): # DESC => initialize constructor
        """ Initialize the TaskTimer object. """
        super(TaskTimer, self).__init__(*args, **kwargs)
        # DESC => store the value attribute
        self.start_task_time = None
        self.start_CPU_execution_time = None
        self.end_task_time = None
        self.end_CPU_execution_time = None

    def start_time(self):
        """Start the timer for task execution."""
        # DESC => get the start task time
        self.start_task_time = time.time()
        self.start_CPU_execution_time = time.process_time()

    def end_time(self):
        """End the timer for task execution."""
        # DESC => get the end task time
        self.end_task_time = time.time()
        self.end_CPU_execution_time = time.process_time()

    def finishe(self, suffix: str='Task Execution Time:', seconds: bool=True, logs: Optional[LoggerHandle]=None) -> str:
        """Calculate and return the task execution time.

        Args:
            `suffix` (str, optional): The suffix to prepend to the output. Defaults to 'Task Execution Time:'.
            `seconds` (bool, optional): Whether to return the time in seconds or formatted time. Defaults to True.
            `logs` (Optional[LoggerHandle], optional): An instance of the `LoggerHandle` class for logging purposes.

        Returns:
            str: The task execution time.

        Example:
        ```python
            timer = TaskTimer()
            timer.start_time()
            time.sleep(2)
            timer.end_time()
            print(timer.finishe())  # Output: Task Execution Time: 2.0 seconds
        ```

        Notes:
            - The `logs` parameter is optional. If provided, it should be an instance of the `LoggerHandle` class for logging purposes.
        """
        self.suffix = str(suffix)
        self.seconds = seconds
        self.logs = logs

        self.elapsed_time = self.end_task_time - self.start_task_time
        self.elapsed_CPU_time = self.end_CPU_execution_time - self.start_CPU_execution_time
        self.time_format = time.strftime("%H{}:%M{}:%S{}", time.gmtime(self.elapsed_time)).format('h', 'm', 's')

        if self.seconds:
            _seconds_ = str(f'{self.suffix} {round(self.elapsed_time, 2)}')
            self.logs.info(f"{self.suffix} {round(self.elapsed_time, 2)}") if isinstance(self.logs, LoggerHandle) else None
            return _seconds_
        else:
            _format_ = str(f'{self.suffix} {self.time_format}')
            self.logs.info(f"{self.suffix} {self.time_format}") if isinstance(self.logs, LoggerHandle) else None
            return _format_

class Threaded(Thread):
    """ Threaded """
    def __init__(self, name_thread: str='', target_function: Any=None, args: list=(), kwargs: dict=None, daemon: bool=True, logs: Optional[LoggerHandle]=None): # DESC => initialize constructor
        """Initialize the Threaded object.

        Args:
            `name_thread` (str, optional): The name of the thread. Defaults to an empty string.
            `target_function` (Any, optional): The target function to execute in the thread. Defaults to None.
            `args` (list, optional): The arguments to pass to the target function. Defaults to an empty list.
            `kwargs` (dict, optional): The keyword arguments to pass to the target function. Defaults to None.
            `daemon` (bool, optional): Whether the thread is a daemon thread or not. Defaults to True.
            `logs` (Optional[LoggerHandle], optional): An instance of the `LoggerHandle` class for logging purposes.

        Example:
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

        Notes:
            - The `logs` parameter is optional. If provided, it should be an instance of the `LoggerHandle` class for logging purposes.
        """
        super(Threaded, self).__init__(name=name_thread, target=target_function, args=args, kwargs=kwargs, daemon=daemon)
        # DESC => store the value attribute
        self.logs = logs
        self._return_ = None
        self._stop_event = Event()

    def run(self):
        """Run the thread and execute the target function."""
        if self._target is not None:
            self._return_ = self._target(*self._args, **self._kwargs)
            return self.logs.info(f"Started thread: {self.name}") if isinstance(self.logs, LoggerHandle) else None

    def join(self):
        """Wait for the thread to complete."""
        Thread.join(self)

    def status(self) -> bool:
        """Check the status of the thread.
            
        Returns:
            bool: The status value.

        Example:
        ```python
            thread = Threaded()
            thread.start()
            print(thread.status())  # Output: (True, 'Thread is running..')
            thread.join()
            print(thread.status())  # Output: (False, 'Thread is finished.')
        ```
        """
        if self.is_alive():
            self.logs.info("Thread is running..") if isinstance(self.logs, LoggerHandle) else None
            return True
        else:
            self.logs.info("Thread is finished.") if isinstance(self.logs, LoggerHandle) else None
            return False

    def stop(self):
        """Set the stop event to stop the thread."""
        self._stop_event.set()

    def stopped(self):
        """Check if the thread has stopped.

        Returns:
            bool: True if the thread has stopped, False otherwise.

        Example:
        ```python
            thread = Threaded()
            thread.start()
            thread.stop()
            print(thread.stopped())  # Output: True
        ```
        """
        return self._stop_event.is_set()

    def get_results(self):
        """Get the results of the thread execution.

        Returns:
            Any: The results of the thread execution.

        Example:
        ```python
            thread = Threaded()
            thread.start()
            thread.join()
            print(thread.get_results())  # Output: <thread results>
        ```
        """
        if self.is_alive():
            return self.logs.info("Thread is running..") if isinstance(self.logs, LoggerHandle) else None
        else:
            return self._return_

class ColorsConstants:
    """ Provide RGB color constants and a colors dictionary with elements formatted. """
    def __init__(self): # DESC => initialize constructor
        """Initialize the ColorsConstants object.

        Returns:
            None

        Example:
        ```python

            constants = ColorsConstants()
            thread.start()
            thread.join()
            print(thread.get_results())  # Output: <thread results>
        ```

        Notes:
            - [colors constants perview](../data/colors_constants.md)
        """
        super(ColorsConstants, self).__init__()
        # DESC => store the value attribute

    def keys_hex(self) -> str: # DESC => Color in HEX format keys
        """ Return of color constants variables in hexadecimal format.

        Returns:
            str: variables keys.

        Example:
        ```python
            colors = ColorsConstants()
            hex_keys = colors.keys_hex().AQUA
            print(hex_keys)  # Output: #00FFFF
        ```
        """
        self.ALICEBLUE = self.RGB(240, 248, 255).hex_format()
        self.ANTIQUEWHITE = self.RGB(250, 235, 215).hex_format()
        self.ANTIQUEWHITE1 = self.RGB(255, 239, 219).hex_format()
        self.ANTIQUEWHITE2 = self.RGB(238, 223, 204).hex_format()
        self.ANTIQUEWHITE3 = self.RGB(205, 192, 176).hex_format()
        self.ANTIQUEWHITE4 = self.RGB(139, 131, 120).hex_format()
        self.AQUA = self.RGB(0, 255, 255).hex_format()
        self.AQUAMARINE1 = self.RGB(127, 255, 212).hex_format()
        self.AQUAMARINE2 = self.RGB(118, 238, 198).hex_format()
        self.AQUAMARINE3 = self.RGB(102, 205, 170).hex_format()
        self.AQUAMARINE4 = self.RGB(69, 139, 116).hex_format()
        self.AZURE1 = self.RGB(240, 255, 255).hex_format()
        self.AZURE2 = self.RGB(224, 238, 238).hex_format()
        self.AZURE3 = self.RGB(193, 205, 205).hex_format()
        self.AZURE4 = self.RGB(131, 139, 139).hex_format()
        self.BANANA = self.RGB(227, 207, 87).hex_format()
        self.BEIGE = self.RGB(245, 245, 220).hex_format()
        self.BISQUE1 = self.RGB(255, 228, 196).hex_format()
        self.BISQUE2 = self.RGB(238, 213, 183).hex_format()
        self.BISQUE3 = self.RGB(205, 183, 158).hex_format()
        self.BISQUE4 = self.RGB(139, 125, 107).hex_format()
        self.BLACK = self.RGB(0, 0, 0).hex_format()
        self.BLANCHEDALMOND = self.RGB(255, 235, 205).hex_format()
        self.BLUE = self.RGB(0, 0, 255).hex_format()
        self.BLUE2 = self.RGB(0, 0, 238).hex_format()
        self.BLUE3 = self.RGB(0, 0, 205).hex_format()
        self.BLUE4 = self.RGB(0, 0, 139).hex_format()
        self.BLUEVIOLET = self.RGB(138, 43, 226).hex_format()
        self.BRICK = self.RGB(156, 102, 31).hex_format()
        self.BROWN = self.RGB(165, 42, 42).hex_format()
        self.BROWN1 = self.RGB(255, 64, 64).hex_format()
        self.BROWN2 = self.RGB(238, 59, 59).hex_format()
        self.BROWN3 = self.RGB(205, 51, 51).hex_format()
        self.BROWN4 = self.RGB(139, 35, 35).hex_format()
        self.BURLYWOOD = self.RGB(222, 184, 135).hex_format()
        self.BURLYWOOD1 = self.RGB(255, 211, 155).hex_format()
        self.BURLYWOOD2 = self.RGB(238, 197, 145).hex_format()
        self.BURLYWOOD3 = self.RGB(205, 170, 125).hex_format()
        self.BURLYWOOD4 = self.RGB(139, 115, 85).hex_format()
        self.BURNTSIENNA = self.RGB(138, 54, 15).hex_format()
        self.BURNTUMBER = self.RGB(138, 51, 36).hex_format()
        self.CADETBLUE = self.RGB(95, 158, 160).hex_format()
        self.CADETBLUE1 = self.RGB(152, 245, 255).hex_format()
        self.CADETBLUE2 = self.RGB(142, 229, 238).hex_format()
        self.CADETBLUE3 = self.RGB(122, 197, 205).hex_format()
        self.CADETBLUE4 = self.RGB(83, 134, 139).hex_format()
        self.CADMIUMORANGE = self.RGB(255, 97, 3).hex_format()
        self.CADMIUMYELLOW = self.RGB(255, 153, 18).hex_format()
        self.CARROT = self.RGB(237, 145, 33).hex_format()
        self.CHARTREUSE1 = self.RGB(127, 255, 0).hex_format()
        self.CHARTREUSE2 = self.RGB(118, 238, 0).hex_format()
        self.CHARTREUSE3 = self.RGB(102, 205, 0).hex_format()
        self.CHARTREUSE4 = self.RGB(69, 139, 0).hex_format()
        self.CHOCOLATE = self.RGB(210, 105, 30).hex_format()
        self.CHOCOLATE1 = self.RGB(255, 127, 36).hex_format()
        self.CHOCOLATE2 = self.RGB(238, 118, 33).hex_format()
        self.CHOCOLATE3 = self.RGB(205, 102, 29).hex_format()
        self.CHOCOLATE4 = self.RGB(139, 69, 19).hex_format()
        self.COBALT = self.RGB(61, 89, 171).hex_format()
        self.COBALTGREEN = self.RGB(61, 145, 64).hex_format()
        self.COLDGREY = self.RGB(128, 138, 135).hex_format()
        self.CORAL = self.RGB(255, 127, 80).hex_format()
        self.CORAL1 = self.RGB(255, 114, 86).hex_format()
        self.CORAL2 = self.RGB(238, 106, 80).hex_format()
        self.CORAL3 = self.RGB(205, 91, 69).hex_format()
        self.CORAL4 = self.RGB(139, 62, 47).hex_format()
        self.CORNFLOWERBLUE = self.RGB(100, 149, 237).hex_format()
        self.CORNSILK1 = self.RGB(255, 248, 220).hex_format()
        self.CORNSILK2 = self.RGB(238, 232, 205).hex_format()
        self.CORNSILK3 = self.RGB(205, 200, 177).hex_format()
        self.CORNSILK4 = self.RGB(139, 136, 120).hex_format()
        self.CRIMSON = self.RGB(220, 20, 60).hex_format()
        self.CYAN2 = self.RGB(0, 238, 238).hex_format()
        self.CYAN3 = self.RGB(0, 205, 205).hex_format()
        self.CYAN4 = self.RGB(0, 139, 139).hex_format()
        self.DARKGOLDENROD = self.RGB(184, 134, 11).hex_format()
        self.DARKGOLDENROD1 = self.RGB(255, 185, 15).hex_format()
        self.DARKGOLDENROD2 = self.RGB(238, 173, 14).hex_format()
        self.DARKGOLDENROD3 = self.RGB(205, 149, 12).hex_format()
        self.DARKGOLDENROD4 = self.RGB(139, 101, 8).hex_format()
        self.DARKGRAY = self.RGB(169, 169, 169).hex_format()
        self.DARKGREEN = self.RGB(0, 100, 0).hex_format()
        self.DARKKHAKI = self.RGB(189, 183, 107).hex_format()
        self.DARKOLIVEGREEN = self.RGB(85, 107, 47).hex_format()
        self.DARKOLIVEGREEN1 = self.RGB(202, 255, 112).hex_format()
        self.DARKOLIVEGREEN2 = self.RGB(188, 238, 104).hex_format()
        self.DARKOLIVEGREEN3 = self.RGB(162, 205, 90).hex_format()
        self.DARKOLIVEGREEN4 = self.RGB(110, 139, 61).hex_format()
        self.DARKORANGE = self.RGB(255, 140, 0).hex_format()
        self.DARKORANGE1 = self.RGB(255, 127, 0).hex_format()
        self.DARKORANGE2 = self.RGB(238, 118, 0).hex_format()
        self.DARKORANGE3 = self.RGB(205, 102, 0).hex_format()
        self.DARKORANGE4 = self.RGB(139, 69, 0).hex_format()
        self.DARKORCHID = self.RGB(153, 50, 204).hex_format()
        self.DARKORCHID1 = self.RGB(191, 62, 255).hex_format()
        self.DARKORCHID2 = self.RGB(178, 58, 238).hex_format()
        self.DARKORCHID3 = self.RGB(154, 50, 205).hex_format()
        self.DARKORCHID4 = self.RGB(104, 34, 139).hex_format()
        self.DARKSALMON = self.RGB(233, 150, 122).hex_format()
        self.DARKSEAGREEN = self.RGB(143, 188, 143).hex_format()
        self.DARKSEAGREEN1 = self.RGB(193, 255, 193).hex_format()
        self.DARKSEAGREEN2 = self.RGB(180, 238, 180).hex_format()
        self.DARKSEAGREEN3 = self.RGB(155, 205, 155).hex_format()
        self.DARKSEAGREEN4 = self.RGB(105, 139, 105).hex_format()
        self.DARKSLATEBLUE = self.RGB(72, 61, 139).hex_format()
        self.DARKSLATEGRAY = self.RGB(47, 79, 79).hex_format()
        self.DARKSLATEGRAY1 = self.RGB(151, 255, 255).hex_format()
        self.DARKSLATEGRAY2 = self.RGB(141, 238, 238).hex_format()
        self.DARKSLATEGRAY3 = self.RGB(121, 205, 205).hex_format()
        self.DARKSLATEGRAY4 = self.RGB(82, 139, 139).hex_format()
        self.DARKTURQUOISE = self.RGB(0, 206, 209).hex_format()
        self.DARKVIOLET = self.RGB(148, 0, 211).hex_format()
        self.DEEPPINK1 = self.RGB(255, 20, 147).hex_format()
        self.DEEPPINK2 = self.RGB(238, 18, 137).hex_format()
        self.DEEPPINK3 = self.RGB(205, 16, 118).hex_format()
        self.DEEPPINK4 = self.RGB(139, 10, 80).hex_format()
        self.DEEPSKYBLUE1 = self.RGB(0, 191, 255).hex_format()
        self.DEEPSKYBLUE2 = self.RGB(0, 178, 238).hex_format()
        self.DEEPSKYBLUE3 = self.RGB(0, 154, 205).hex_format()
        self.DEEPSKYBLUE4 = self.RGB(0, 104, 139).hex_format()
        self.DIMGRAY = self.RGB(105, 105, 105).hex_format()
        self.DIMGRAY = self.RGB(105, 105, 105).hex_format()
        self.DODGERBLUE1 = self.RGB(30, 144, 255).hex_format()
        self.DODGERBLUE2 = self.RGB(28, 134, 238).hex_format()
        self.DODGERBLUE3 = self.RGB(24, 116, 205).hex_format()
        self.DODGERBLUE4 = self.RGB(16, 78, 139).hex_format()
        self.EGGSHELL = self.RGB(252, 230, 201).hex_format()
        self.EMERALDGREEN = self.RGB(0, 201, 87).hex_format()
        self.FIREBRICK = self.RGB(178, 34, 34).hex_format()
        self.FIREBRICK1 = self.RGB(255, 48, 48).hex_format()
        self.FIREBRICK2 = self.RGB(238, 44, 44).hex_format()
        self.FIREBRICK3 = self.RGB(205, 38, 38).hex_format()
        self.FIREBRICK4 = self.RGB(139, 26, 26).hex_format()
        self.FLESH = self.RGB(255, 125, 64).hex_format()
        self.FLORALWHITE = self.RGB(255, 250, 240).hex_format()
        self.FORESTGREEN = self.RGB(34, 139, 34).hex_format()
        self.GAINSBORO = self.RGB(220, 220, 220).hex_format()
        self.GHOSTWHITE = self.RGB(248, 248, 255).hex_format()
        self.GOLD1 = self.RGB(255, 215, 0).hex_format()
        self.GOLD2 = self.RGB(238, 201, 0).hex_format()
        self.GOLD3 = self.RGB(205, 173, 0).hex_format()
        self.GOLD4 = self.RGB(139, 117, 0).hex_format()
        self.GOLDENROD = self.RGB(218, 165, 32).hex_format()
        self.GOLDENROD1 = self.RGB(255, 193, 37).hex_format()
        self.GOLDENROD2 = self.RGB(238, 180, 34).hex_format()
        self.GOLDENROD3 = self.RGB(205, 155, 29).hex_format()
        self.GOLDENROD4 = self.RGB(139, 105, 20).hex_format()
        self.GRAY = self.RGB(128, 128, 128).hex_format()
        self.GRAY1 = self.RGB(3, 3, 3).hex_format()
        self.GRAY10 = self.RGB(26, 26, 26).hex_format()
        self.GRAY11 = self.RGB(28, 28, 28).hex_format()
        self.GRAY12 = self.RGB(31, 31, 31).hex_format()
        self.GRAY13 = self.RGB(33, 33, 33).hex_format()
        self.GRAY14 = self.RGB(36, 36, 36).hex_format()
        self.GRAY15 = self.RGB(38, 38, 38).hex_format()
        self.GRAY16 = self.RGB(41, 41, 41).hex_format()
        self.GRAY17 = self.RGB(43, 43, 43).hex_format()
        self.GRAY18 = self.RGB(46, 46, 46).hex_format()
        self.GRAY19 = self.RGB(48, 48, 48).hex_format()
        self.GRAY2 = self.RGB(5, 5, 5).hex_format()
        self.GRAY20 = self.RGB(51, 51, 51).hex_format()
        self.GRAY21 = self.RGB(54, 54, 54).hex_format()
        self.GRAY22 = self.RGB(56, 56, 56).hex_format()
        self.GRAY23 = self.RGB(59, 59, 59).hex_format()
        self.GRAY24 = self.RGB(61, 61, 61).hex_format()
        self.GRAY25 = self.RGB(64, 64, 64).hex_format()
        self.GRAY26 = self.RGB(66, 66, 66).hex_format()
        self.GRAY27 = self.RGB(69, 69, 69).hex_format()
        self.GRAY28 = self.RGB(71, 71, 71).hex_format()
        self.GRAY29 = self.RGB(74, 74, 74).hex_format()
        self.GRAY3 = self.RGB(8, 8, 8).hex_format()
        self.GRAY30 = self.RGB(77, 77, 77).hex_format()
        self.GRAY31 = self.RGB(79, 79, 79).hex_format()
        self.GRAY32 = self.RGB(82, 82, 82).hex_format()
        self.GRAY33 = self.RGB(84, 84, 84).hex_format()
        self.GRAY34 = self.RGB(87, 87, 87).hex_format()
        self.GRAY35 = self.RGB(89, 89, 89).hex_format()
        self.GRAY36 = self.RGB(92, 92, 92).hex_format()
        self.GRAY37 = self.RGB(94, 94, 94).hex_format()
        self.GRAY38 = self.RGB(97, 97, 97).hex_format()
        self.GRAY39 = self.RGB(99, 99, 99).hex_format()
        self.GRAY4 = self.RGB(10, 10, 10).hex_format()
        self.GRAY40 = self.RGB(102, 102, 102).hex_format()
        self.GRAY42 = self.RGB(107, 107, 107).hex_format()
        self.GRAY43 = self.RGB(110, 110, 110).hex_format()
        self.GRAY44 = self.RGB(112, 112, 112).hex_format()
        self.GRAY45 = self.RGB(115, 115, 115).hex_format()
        self.GRAY46 = self.RGB(117, 117, 117).hex_format()
        self.GRAY47 = self.RGB(120, 120, 120).hex_format()
        self.GRAY48 = self.RGB(122, 122, 122).hex_format()
        self.GRAY49 = self.RGB(125, 125, 125).hex_format()
        self.GRAY5 = self.RGB(13, 13, 13).hex_format()
        self.GRAY50 = self.RGB(127, 127, 127).hex_format()
        self.GRAY51 = self.RGB(130, 130, 130).hex_format()
        self.GRAY52 = self.RGB(133, 133, 133).hex_format()
        self.GRAY53 = self.RGB(135, 135, 135).hex_format()
        self.GRAY54 = self.RGB(138, 138, 138).hex_format()
        self.GRAY55 = self.RGB(140, 140, 140).hex_format()
        self.GRAY56 = self.RGB(143, 143, 143).hex_format()
        self.GRAY57 = self.RGB(145, 145, 145).hex_format()
        self.GRAY58 = self.RGB(148, 148, 148).hex_format()
        self.GRAY59 = self.RGB(150, 150, 150).hex_format()
        self.GRAY6 = self.RGB(15, 15, 15).hex_format()
        self.GRAY60 = self.RGB(153, 153, 153).hex_format()
        self.GRAY61 = self.RGB(156, 156, 156).hex_format()
        self.GRAY62 = self.RGB(158, 158, 158).hex_format()
        self.GRAY63 = self.RGB(161, 161, 161).hex_format()
        self.GRAY64 = self.RGB(163, 163, 163).hex_format()
        self.GRAY65 = self.RGB(166, 166, 166).hex_format()
        self.GRAY66 = self.RGB(168, 168, 168).hex_format()
        self.GRAY67 = self.RGB(171, 171, 171).hex_format()
        self.GRAY68 = self.RGB(173, 173, 173).hex_format()
        self.GRAY69 = self.RGB(176, 176, 176).hex_format()
        self.GRAY7 = self.RGB(18, 18, 18).hex_format()
        self.GRAY70 = self.RGB(179, 179, 179).hex_format()
        self.GRAY71 = self.RGB(181, 181, 181).hex_format()
        self.GRAY72 = self.RGB(184, 184, 184).hex_format()
        self.GRAY73 = self.RGB(186, 186, 186).hex_format()
        self.GRAY74 = self.RGB(189, 189, 189).hex_format()
        self.GRAY75 = self.RGB(191, 191, 191).hex_format()
        self.GRAY76 = self.RGB(194, 194, 194).hex_format()
        self.GRAY77 = self.RGB(196, 196, 196).hex_format()
        self.GRAY78 = self.RGB(199, 199, 199).hex_format()
        self.GRAY79 = self.RGB(201, 201, 201).hex_format()
        self.GRAY8 = self.RGB(20, 20, 20).hex_format()
        self.GRAY80 = self.RGB(204, 204, 204).hex_format()
        self.GRAY81 = self.RGB(207, 207, 207).hex_format()
        self.GRAY82 = self.RGB(209, 209, 209).hex_format()
        self.GRAY83 = self.RGB(212, 212, 212).hex_format()
        self.GRAY84 = self.RGB(214, 214, 214).hex_format()
        self.GRAY85 = self.RGB(217, 217, 217).hex_format()
        self.GRAY86 = self.RGB(219, 219, 219).hex_format()
        self.GRAY87 = self.RGB(222, 222, 222).hex_format()
        self.GRAY88 = self.RGB(224, 224, 224).hex_format()
        self.GRAY89 = self.RGB(227, 227, 227).hex_format()
        self.GRAY9 = self.RGB(23, 23, 23).hex_format()
        self.GRAY90 = self.RGB(229, 229, 229).hex_format()
        self.GRAY91 = self.RGB(232, 232, 232).hex_format()
        self.GRAY92 = self.RGB(235, 235, 235).hex_format()
        self.GRAY93 = self.RGB(237, 237, 237).hex_format()
        self.GRAY94 = self.RGB(240, 240, 240).hex_format()
        self.GRAY95 = self.RGB(242, 242, 242).hex_format()
        self.GRAY97 = self.RGB(247, 247, 247).hex_format()
        self.GRAY98 = self.RGB(250, 250, 250).hex_format()
        self.GRAY99 = self.RGB(252, 252, 252).hex_format()
        self.GREEN = self.RGB(0, 128, 0).hex_format()
        self.GREEN1 = self.RGB(0, 255, 0).hex_format()
        self.GREEN2 = self.RGB(0, 238, 0).hex_format()
        self.GREEN3 = self.RGB(0, 205, 0).hex_format()
        self.GREEN4 = self.RGB(0, 139, 0).hex_format()
        self.GREENYELLOW = self.RGB(173, 255, 47).hex_format()
        self.HONEYDEW1 = self.RGB(240, 255, 240).hex_format()
        self.HONEYDEW2 = self.RGB(224, 238, 224).hex_format()
        self.HONEYDEW3 = self.RGB(193, 205, 193).hex_format()
        self.HONEYDEW4 = self.RGB(131, 139, 131).hex_format()
        self.HOTPINK = self.RGB(255, 105, 180).hex_format()
        self.HOTPINK1 = self.RGB(255, 110, 180).hex_format()
        self.HOTPINK2 = self.RGB(238, 106, 167).hex_format()
        self.HOTPINK3 = self.RGB(205, 96, 144).hex_format()
        self.HOTPINK4 = self.RGB(139, 58, 98).hex_format()
        self.INDIANRED = self.RGB(176, 23, 31).hex_format()
        self.INDIANRED = self.RGB(205, 92, 92).hex_format()
        self.INDIANRED1 = self.RGB(255, 106, 106).hex_format()
        self.INDIANRED2 = self.RGB(238, 99, 99).hex_format()
        self.INDIANRED3 = self.RGB(205, 85, 85).hex_format()
        self.INDIANRED4 = self.RGB(139, 58, 58).hex_format()
        self.INDIGO = self.RGB(75, 0, 130).hex_format()
        self.IVORY1 = self.RGB(255, 255, 240).hex_format()
        self.IVORY2 = self.RGB(238, 238, 224).hex_format()
        self.IVORY3 = self.RGB(205, 205, 193).hex_format()
        self.IVORY4 = self.RGB(139, 139, 131).hex_format()
        self.IVORYBLACK = self.RGB(41, 36, 33).hex_format()
        self.KHAKI = self.RGB(240, 230, 140).hex_format()
        self.KHAKI1 = self.RGB(255, 246, 143).hex_format()
        self.KHAKI2 = self.RGB(238, 230, 133).hex_format()
        self.KHAKI3 = self.RGB(205, 198, 115).hex_format()
        self.KHAKI4 = self.RGB(139, 134, 78).hex_format()
        self.LAVENDER = self.RGB(230, 230, 250).hex_format()
        self.LAVENDERBLUSH1 = self.RGB(255, 240, 245).hex_format()
        self.LAVENDERBLUSH2 = self.RGB(238, 224, 229).hex_format()
        self.LAVENDERBLUSH3 = self.RGB(205, 193, 197).hex_format()
        self.LAVENDERBLUSH4 = self.RGB(139, 131, 134).hex_format()
        self.LAWNGREEN = self.RGB(124, 252, 0).hex_format()
        self.LEMONCHIFFON1 = self.RGB(255, 250, 205).hex_format()
        self.LEMONCHIFFON2 = self.RGB(238, 233, 191).hex_format()
        self.LEMONCHIFFON3 = self.RGB(205, 201, 165).hex_format()
        self.LEMONCHIFFON4 = self.RGB(139, 137, 112).hex_format()
        self.LIGHTBLUE = self.RGB(173, 216, 230).hex_format()
        self.LIGHTBLUE1 = self.RGB(191, 239, 255).hex_format()
        self.LIGHTBLUE2 = self.RGB(178, 223, 238).hex_format()
        self.LIGHTBLUE3 = self.RGB(154, 192, 205).hex_format()
        self.LIGHTBLUE4 = self.RGB(104, 131, 139).hex_format()
        self.LIGHTCORAL = self.RGB(240, 128, 128).hex_format()
        self.LIGHTCYAN1 = self.RGB(224, 255, 255).hex_format()
        self.LIGHTCYAN2 = self.RGB(209, 238, 238).hex_format()
        self.LIGHTCYAN3 = self.RGB(180, 205, 205).hex_format()
        self.LIGHTCYAN4 = self.RGB(122, 139, 139).hex_format()
        self.LIGHTGOLDENROD1 = self.RGB(255, 236, 139).hex_format()
        self.LIGHTGOLDENROD2 = self.RGB(238, 220, 130).hex_format()
        self.LIGHTGOLDENROD3 = self.RGB(205, 190, 112).hex_format()
        self.LIGHTGOLDENROD4 = self.RGB(139, 129, 76).hex_format()
        self.LIGHTGOLDENRODYELLOW = self.RGB(250, 250, 210).hex_format()
        self.LIGHTGREY = self.RGB(211, 211, 211).hex_format()
        self.LIGHTPINK = self.RGB(255, 182, 193).hex_format()
        self.LIGHTPINK1 = self.RGB(255, 174, 185).hex_format()
        self.LIGHTPINK2 = self.RGB(238, 162, 173).hex_format()
        self.LIGHTPINK3 = self.RGB(205, 140, 149).hex_format()
        self.LIGHTPINK4 = self.RGB(139, 95, 101).hex_format()
        self.LIGHTSALMON1 = self.RGB(255, 160, 122).hex_format()
        self.LIGHTSALMON2 = self.RGB(238, 149, 114).hex_format()
        self.LIGHTSALMON3 = self.RGB(205, 129, 98).hex_format()
        self.LIGHTSALMON4 = self.RGB(139, 87, 66).hex_format()
        self.LIGHTSEAGREEN = self.RGB(32, 178, 170).hex_format()
        self.LIGHTSKYBLUE = self.RGB(135, 206, 250).hex_format()
        self.LIGHTSKYBLUE1 = self.RGB(176, 226, 255).hex_format()
        self.LIGHTSKYBLUE2 = self.RGB(164, 211, 238).hex_format()
        self.LIGHTSKYBLUE3 = self.RGB(141, 182, 205).hex_format()
        self.LIGHTSKYBLUE4 = self.RGB(96, 123, 139).hex_format()
        self.LIGHTSLATEBLUE = self.RGB(132, 112, 255).hex_format()
        self.LIGHTSLATEGRAY = self.RGB(119, 136, 153).hex_format()
        self.LIGHTSTEELBLUE = self.RGB(176, 196, 222).hex_format()
        self.LIGHTSTEELBLUE1 = self.RGB(202, 225, 255).hex_format()
        self.LIGHTSTEELBLUE2 = self.RGB(188, 210, 238).hex_format()
        self.LIGHTSTEELBLUE3 = self.RGB(162, 181, 205).hex_format()
        self.LIGHTSTEELBLUE4 = self.RGB(110, 123, 139).hex_format()
        self.LIGHTYELLOW1 = self.RGB(255, 255, 224).hex_format()
        self.LIGHTYELLOW2 = self.RGB(238, 238, 209).hex_format()
        self.LIGHTYELLOW3 = self.RGB(205, 205, 180).hex_format()
        self.LIGHTYELLOW4 = self.RGB(139, 139, 122).hex_format()
        self.LIMEGREEN = self.RGB(50, 205, 50).hex_format()
        self.LINEN = self.RGB(250, 240, 230).hex_format()
        self.MAGENTA = self.RGB(255, 0, 255).hex_format()
        self.MAGENTA2 = self.RGB(238, 0, 238).hex_format()
        self.MAGENTA3 = self.RGB(205, 0, 205).hex_format()
        self.MAGENTA4 = self.RGB(139, 0, 139).hex_format()
        self.MANGANESEBLUE = self.RGB(3, 168, 158).hex_format()
        self.MAROON = self.RGB(128, 0, 0).hex_format()
        self.MAROON1 = self.RGB(255, 52, 179).hex_format()
        self.MAROON2 = self.RGB(238, 48, 167).hex_format()
        self.MAROON3 = self.RGB(205, 41, 144).hex_format()
        self.MAROON4 = self.RGB(139, 28, 98).hex_format()
        self.MEDIUMORCHID = self.RGB(186, 85, 211).hex_format()
        self.MEDIUMORCHID1 = self.RGB(224, 102, 255).hex_format()
        self.MEDIUMORCHID2 = self.RGB(209, 95, 238).hex_format()
        self.MEDIUMORCHID3 = self.RGB(180, 82, 205).hex_format()
        self.MEDIUMORCHID4 = self.RGB(122, 55, 139).hex_format()
        self.MEDIUMPURPLE = self.RGB(147, 112, 219).hex_format()
        self.MEDIUMPURPLE1 = self.RGB(171, 130, 255).hex_format()
        self.MEDIUMPURPLE2 = self.RGB(159, 121, 238).hex_format()
        self.MEDIUMPURPLE3 = self.RGB(137, 104, 205).hex_format()
        self.MEDIUMPURPLE4 = self.RGB(93, 71, 139).hex_format()
        self.MEDIUMSEAGREEN = self.RGB(60, 179, 113).hex_format()
        self.MEDIUMSLATEBLUE = self.RGB(123, 104, 238).hex_format()
        self.MEDIUMSPRINGGREEN = self.RGB(0, 250, 154).hex_format()
        self.MEDIUMTURQUOISE = self.RGB(72, 209, 204).hex_format()
        self.MEDIUMVIOLETRED = self.RGB(199, 21, 133).hex_format()
        self.MELON = self.RGB(227, 168, 105).hex_format()
        self.MIDNIGHTBLUE = self.RGB(25, 25, 112).hex_format()
        self.MINT = self.RGB(189, 252, 201).hex_format()
        self.MINTCREAM = self.RGB(245, 255, 250).hex_format()
        self.MISTYROSE1 = self.RGB(255, 228, 225).hex_format()
        self.MISTYROSE2 = self.RGB(238, 213, 210).hex_format()
        self.MISTYROSE3 = self.RGB(205, 183, 181).hex_format()
        self.MISTYROSE4 = self.RGB(139, 125, 123).hex_format()
        self.MOCCASIN = self.RGB(255, 228, 181).hex_format()
        self.NAVAJOWHITE1 = self.RGB(255, 222, 173).hex_format()
        self.NAVAJOWHITE2 = self.RGB(238, 207, 161).hex_format()
        self.NAVAJOWHITE3 = self.RGB(205, 179, 139).hex_format()
        self.NAVAJOWHITE4 = self.RGB(139, 121, 94).hex_format()
        self.NAVY = self.RGB(0, 0, 128).hex_format()
        self.OLDLACE = self.RGB(253, 245, 230).hex_format()
        self.OLIVE = self.RGB(128, 128, 0).hex_format()
        self.OLIVEDRAB = self.RGB(107, 142, 35).hex_format()
        self.OLIVEDRAB1 = self.RGB(192, 255, 62).hex_format()
        self.OLIVEDRAB2 = self.RGB(179, 238, 58).hex_format()
        self.OLIVEDRAB3 = self.RGB(154, 205, 50).hex_format()
        self.OLIVEDRAB4 = self.RGB(105, 139, 34).hex_format()
        self.ORANGE = self.RGB(255, 128, 0).hex_format()
        self.ORANGE1 = self.RGB(255, 165, 0).hex_format()
        self.ORANGE2 = self.RGB(238, 154, 0).hex_format()
        self.ORANGE3 = self.RGB(205, 133, 0).hex_format()
        self.ORANGE4 = self.RGB(139, 90, 0).hex_format()
        self.ORANGERED1 = self.RGB(255, 69, 0).hex_format()
        self.ORANGERED2 = self.RGB(238, 64, 0).hex_format()
        self.ORANGERED3 = self.RGB(205, 55, 0).hex_format()
        self.ORANGERED4 = self.RGB(139, 37, 0).hex_format()
        self.ORCHID = self.RGB(218, 112, 214).hex_format()
        self.ORCHID1 = self.RGB(255, 131, 250).hex_format()
        self.ORCHID2 = self.RGB(238, 122, 233).hex_format()
        self.ORCHID3 = self.RGB(205, 105, 201).hex_format()
        self.ORCHID4 = self.RGB(139, 71, 137).hex_format()
        self.PALEGOLDENROD = self.RGB(238, 232, 170).hex_format()
        self.PALEGREEN = self.RGB(152, 251, 152).hex_format()
        self.PALEGREEN1 = self.RGB(154, 255, 154).hex_format()
        self.PALEGREEN2 = self.RGB(144, 238, 144).hex_format()
        self.PALEGREEN3 = self.RGB(124, 205, 124).hex_format()
        self.PALEGREEN4 = self.RGB(84, 139, 84).hex_format()
        self.PALETURQUOISE1 = self.RGB(187, 255, 255).hex_format()
        self.PALETURQUOISE2 = self.RGB(174, 238, 238).hex_format()
        self.PALETURQUOISE3 = self.RGB(150, 205, 205).hex_format()
        self.PALETURQUOISE4 = self.RGB(102, 139, 139).hex_format()
        self.PALEVIOLETRED = self.RGB(219, 112, 147).hex_format()
        self.PALEVIOLETRED1 = self.RGB(255, 130, 171).hex_format()
        self.PALEVIOLETRED2 = self.RGB(238, 121, 159).hex_format()
        self.PALEVIOLETRED3 = self.RGB(205, 104, 137).hex_format()
        self.PALEVIOLETRED4 = self.RGB(139, 71, 93).hex_format()
        self.PAPAYAWHIP = self.RGB(255, 239, 213).hex_format()
        self.PEACHPUFF1 = self.RGB(255, 218, 185).hex_format()
        self.PEACHPUFF2 = self.RGB(238, 203, 173).hex_format()
        self.PEACHPUFF3 = self.RGB(205, 175, 149).hex_format()
        self.PEACHPUFF4 = self.RGB(139, 119, 101).hex_format()
        self.PEACOCK = self.RGB(51, 161, 201).hex_format()
        self.PINK = self.RGB(255, 192, 203).hex_format()
        self.PINK1 = self.RGB(255, 181, 197).hex_format()
        self.PINK2 = self.RGB(238, 169, 184).hex_format()
        self.PINK3 = self.RGB(205, 145, 158).hex_format()
        self.PINK4 = self.RGB(139, 99, 108).hex_format()
        self.PLUM = self.RGB(221, 160, 221).hex_format()
        self.PLUM1 = self.RGB(255, 187, 255).hex_format()
        self.PLUM2 = self.RGB(238, 174, 238).hex_format()
        self.PLUM3 = self.RGB(205, 150, 205).hex_format()
        self.PLUM4 = self.RGB(139, 102, 139).hex_format()
        self.POWDERBLUE = self.RGB(176, 224, 230).hex_format()
        self.PURPLE = self.RGB(128, 0, 128).hex_format()
        self.PURPLE1 = self.RGB(155, 48, 255).hex_format()
        self.PURPLE2 = self.RGB(145, 44, 238).hex_format()
        self.PURPLE3 = self.RGB(125, 38, 205).hex_format()
        self.PURPLE4 = self.RGB(85, 26, 139).hex_format()
        self.RASPBERRY = self.RGB(135, 38, 87).hex_format()
        self.RAWSIENNA = self.RGB(199, 97, 20).hex_format()
        self.RED1 = self.RGB(255, 0, 0).hex_format()
        self.RED2 = self.RGB(238, 0, 0).hex_format()
        self.RED3 = self.RGB(205, 0, 0).hex_format()
        self.RED4 = self.RGB(139, 0, 0).hex_format()
        self.ROSYBROWN = self.RGB(188, 143, 143).hex_format()
        self.ROSYBROWN1 = self.RGB(255, 193, 193).hex_format()
        self.ROSYBROWN2 = self.RGB(238, 180, 180).hex_format()
        self.ROSYBROWN3 = self.RGB(205, 155, 155).hex_format()
        self.ROSYBROWN4 = self.RGB(139, 105, 105).hex_format()
        self.ROYALBLUE = self.RGB(65, 105, 225).hex_format()
        self.ROYALBLUE1 = self.RGB(72, 118, 255).hex_format()
        self.ROYALBLUE2 = self.RGB(67, 110, 238).hex_format()
        self.ROYALBLUE3 = self.RGB(58, 95, 205).hex_format()
        self.ROYALBLUE4 = self.RGB(39, 64, 139).hex_format()
        self.SALMON = self.RGB(250, 128, 114).hex_format()
        self.SALMON1 = self.RGB(255, 140, 105).hex_format()
        self.SALMON2 = self.RGB(238, 130, 98).hex_format()
        self.SALMON3 = self.RGB(205, 112, 84).hex_format()
        self.SALMON4 = self.RGB(139, 76, 57).hex_format()
        self.SANDYBROWN = self.RGB(244, 164, 96).hex_format()
        self.SAPGREEN = self.RGB(48, 128, 20).hex_format()
        self.SEAGREEN1 = self.RGB(84, 255, 159).hex_format()
        self.SEAGREEN2 = self.RGB(78, 238, 148).hex_format()
        self.SEAGREEN3 = self.RGB(67, 205, 128).hex_format()
        self.SEAGREEN4 = self.RGB(46, 139, 87).hex_format()
        self.SEASHELL1 = self.RGB(255, 245, 238).hex_format()
        self.SEASHELL2 = self.RGB(238, 229, 222).hex_format()
        self.SEASHELL3 = self.RGB(205, 197, 191).hex_format()
        self.SEASHELL4 = self.RGB(139, 134, 130).hex_format()
        self.SEPIA = self.RGB(94, 38, 18).hex_format()
        self.SGIBEET = self.RGB(142, 56, 142).hex_format()
        self.SGIBRIGHTGRAY = self.RGB(197, 193, 170).hex_format()
        self.SGICHARTREUSE = self.RGB(113, 198, 113).hex_format()
        self.SGIDARKGRAY = self.RGB(85, 85, 85).hex_format()
        self.SGIGRAY12 = self.RGB(30, 30, 30).hex_format()
        self.SGIGRAY16 = self.RGB(40, 40, 40).hex_format()
        self.SGIGRAY32 = self.RGB(81, 81, 81).hex_format()
        self.SGIGRAY36 = self.RGB(91, 91, 91).hex_format()
        self.SGIGRAY52 = self.RGB(132, 132, 132).hex_format()
        self.SGIGRAY56 = self.RGB(142, 142, 142).hex_format()
        self.SGIGRAY72 = self.RGB(183, 183, 183).hex_format()
        self.SGIGRAY76 = self.RGB(193, 193, 193).hex_format()
        self.SGIGRAY92 = self.RGB(234, 234, 234).hex_format()
        self.SGIGRAY96 = self.RGB(244, 244, 244).hex_format()
        self.SGILIGHTBLUE = self.RGB(125, 158, 192).hex_format()
        self.SGILIGHTGRAY = self.RGB(170, 170, 170).hex_format()
        self.SGIOLIVEDRAB = self.RGB(142, 142, 56).hex_format()
        self.SGISALMON = self.RGB(198, 113, 113).hex_format()
        self.SGISLATEBLUE = self.RGB(113, 113, 198).hex_format()
        self.SGITEAL = self.RGB(56, 142, 142).hex_format()
        self.SIENNA = self.RGB(160, 82, 45).hex_format()
        self.SIENNA1 = self.RGB(255, 130, 71).hex_format()
        self.SIENNA2 = self.RGB(238, 121, 66).hex_format()
        self.SIENNA3 = self.RGB(205, 104, 57).hex_format()
        self.SIENNA4 = self.RGB(139, 71, 38).hex_format()
        self.SILVER = self.RGB(192, 192, 192).hex_format()
        self.SKYBLUE = self.RGB(135, 206, 235).hex_format()
        self.SKYBLUE1 = self.RGB(135, 206, 255).hex_format()
        self.SKYBLUE2 = self.RGB(126, 192, 238).hex_format()
        self.SKYBLUE3 = self.RGB(108, 166, 205).hex_format()
        self.SKYBLUE4 = self.RGB(74, 112, 139).hex_format()
        self.SLATEBLUE = self.RGB(106, 90, 205).hex_format()
        self.SLATEBLUE1 = self.RGB(131, 111, 255).hex_format()
        self.SLATEBLUE2 = self.RGB(122, 103, 238).hex_format()
        self.SLATEBLUE3 = self.RGB(105, 89, 205).hex_format()
        self.SLATEBLUE4 = self.RGB(71, 60, 139).hex_format()
        self.SLATEGRAY = self.RGB(112, 128, 144).hex_format()
        self.SLATEGRAY1 = self.RGB(198, 226, 255).hex_format()
        self.SLATEGRAY2 = self.RGB(185, 211, 238).hex_format()
        self.SLATEGRAY3 = self.RGB(159, 182, 205).hex_format()
        self.SLATEGRAY4 = self.RGB(108, 123, 139).hex_format()
        self.SNOW1 = self.RGB(255, 250, 250).hex_format()
        self.SNOW2 = self.RGB(238, 233, 233).hex_format()
        self.SNOW3 = self.RGB(205, 201, 201).hex_format()
        self.SNOW4 = self.RGB(139, 137, 137).hex_format()
        self.SPRINGGREEN = self.RGB(0, 255, 127).hex_format()
        self.SPRINGGREEN1 = self.RGB(0, 238, 118).hex_format()
        self.SPRINGGREEN2 = self.RGB(0, 205, 102).hex_format()
        self.SPRINGGREEN3 = self.RGB(0, 139, 69).hex_format()
        self.STEELBLUE = self.RGB(70, 130, 180).hex_format()
        self.STEELBLUE1 = self.RGB(99, 184, 255).hex_format()
        self.STEELBLUE2 = self.RGB(92, 172, 238).hex_format()
        self.STEELBLUE3 = self.RGB(79, 148, 205).hex_format()
        self.STEELBLUE4 = self.RGB(54, 100, 139).hex_format()
        self.TAN = self.RGB(210, 180, 140).hex_format()
        self.TAN1 = self.RGB(255, 165, 79).hex_format()
        self.TAN2 = self.RGB(238, 154, 73).hex_format()
        self.TAN3 = self.RGB(205, 133, 63).hex_format()
        self.TAN4 = self.RGB(139, 90, 43).hex_format()
        self.TEAL = self.RGB(0, 128, 128).hex_format()
        self.THISTLE = self.RGB(216, 191, 216).hex_format()
        self.THISTLE1 = self.RGB(255, 225, 255).hex_format()
        self.THISTLE2 = self.RGB(238, 210, 238).hex_format()
        self.THISTLE3 = self.RGB(205, 181, 205).hex_format()
        self.THISTLE4 = self.RGB(139, 123, 139).hex_format()
        self.TOMATO1 = self.RGB(255, 99, 71).hex_format()
        self.TOMATO2 = self.RGB(238, 92, 66).hex_format()
        self.TOMATO3 = self.RGB(205, 79, 57).hex_format()
        self.TOMATO4 = self.RGB(139, 54, 38).hex_format()
        self.TURQUOISE = self.RGB(64, 224, 208).hex_format()
        self.TURQUOISE1 = self.RGB(0, 245, 255).hex_format()
        self.TURQUOISE2 = self.RGB(0, 229, 238).hex_format()
        self.TURQUOISE3 = self.RGB(0, 197, 205).hex_format()
        self.TURQUOISE4 = self.RGB(0, 134, 139).hex_format()
        self.TURQUOISEBLUE = self.RGB(0, 199, 140).hex_format()
        self.VIOLET = self.RGB(238, 130, 238).hex_format()
        self.VIOLETRED = self.RGB(208, 32, 144).hex_format()
        self.VIOLETRED1 = self.RGB(255, 62, 150).hex_format()
        self.VIOLETRED2 = self.RGB(238, 58, 140).hex_format()
        self.VIOLETRED3 = self.RGB(205, 50, 120).hex_format()
        self.VIOLETRED4 = self.RGB(139, 34, 82).hex_format()
        self.WARMGREY = self.RGB(128, 128, 105).hex_format()
        self.WHEAT = self.RGB(245, 222, 179).hex_format()
        self.WHEAT1 = self.RGB(255, 231, 186).hex_format()
        self.WHEAT2 = self.RGB(238, 216, 174).hex_format()
        self.WHEAT3 = self.RGB(205, 186, 150).hex_format()
        self.WHEAT4 = self.RGB(139, 126, 102).hex_format()
        self.WHITE = self.RGB(255, 255, 255).hex_format()
        self.WHITESMOKE = self.RGB(245, 245, 245).hex_format()
        self.WHITESMOKE = self.RGB(245, 245, 245).hex_format()
        self.YELLOW1 = self.RGB(255, 255, 0).hex_format()
        self.YELLOW2 = self.RGB(238, 238, 0).hex_format()
        self.YELLOW3 = self.RGB(205, 205, 0).hex_format()
        self.YELLOW4 = self.RGB(139, 139, 0).hex_format()

        return self # <= NOTE return all variables.

    def keys_rgb(self) -> tuple: # DESC => Color in RGB keys
        """ Return of color constants variables in RGB format.
        
        Returns:
            tuple[str, str, str]: variables keys.

        Example:
        ```python
            colors = ColorsConstants()
            rgb_keys = colors.keys_rgb().ALICEBLUE
            print(rgb_keys)  # Output: (240, 248, 255)
        ```
        """
        self.ALICEBLUE = self.RGB(240, 248, 255).rgb_format()
        self.ANTIQUEWHITE = self.RGB(250, 235, 215).rgb_format()
        self.ANTIQUEWHITE1 = self.RGB(255, 239, 219).rgb_format()
        self.ANTIQUEWHITE2 = self.RGB(238, 223, 204).rgb_format()
        self.ANTIQUEWHITE3 = self.RGB(205, 192, 176).rgb_format()
        self.ANTIQUEWHITE4 = self.RGB(139, 131, 120).rgb_format()
        self.AQUA = self.RGB(0, 255, 255).rgb_format()
        self.AQUAMARINE1 = self.RGB(127, 255, 212).rgb_format()
        self.AQUAMARINE2 = self.RGB(118, 238, 198).rgb_format()
        self.AQUAMARINE3 = self.RGB(102, 205, 170).rgb_format()
        self.AQUAMARINE4 = self.RGB(69, 139, 116).rgb_format()
        self.AZURE1 = self.RGB(240, 255, 255).rgb_format()
        self.AZURE2 = self.RGB(224, 238, 238).rgb_format()
        self.AZURE3 = self.RGB(193, 205, 205).rgb_format()
        self.AZURE4 = self.RGB(131, 139, 139).rgb_format()
        self.BANANA = self.RGB(227, 207, 87).rgb_format()
        self.BEIGE = self.RGB(245, 245, 220).rgb_format()
        self.BISQUE1 = self.RGB(255, 228, 196).rgb_format()
        self.BISQUE2 = self.RGB(238, 213, 183).rgb_format()
        self.BISQUE3 = self.RGB(205, 183, 158).rgb_format()
        self.BISQUE4 = self.RGB(139, 125, 107).rgb_format()
        self.BLACK = self.RGB(0, 0, 0).rgb_format()
        self.BLANCHEDALMOND = self.RGB(255, 235, 205).rgb_format()
        self.BLUE = self.RGB(0, 0, 255).rgb_format()
        self.BLUE2 = self.RGB(0, 0, 238).rgb_format()
        self.BLUE3 = self.RGB(0, 0, 205).rgb_format()
        self.BLUE4 = self.RGB(0, 0, 139).rgb_format()
        self.BLUEVIOLET = self.RGB(138, 43, 226).rgb_format()
        self.BRICK = self.RGB(156, 102, 31).rgb_format()
        self.BROWN = self.RGB(165, 42, 42).rgb_format()
        self.BROWN1 = self.RGB(255, 64, 64).rgb_format()
        self.BROWN2 = self.RGB(238, 59, 59).rgb_format()
        self.BROWN3 = self.RGB(205, 51, 51).rgb_format()
        self.BROWN4 = self.RGB(139, 35, 35).rgb_format()
        self.BURLYWOOD = self.RGB(222, 184, 135).rgb_format()
        self.BURLYWOOD1 = self.RGB(255, 211, 155).rgb_format()
        self.BURLYWOOD2 = self.RGB(238, 197, 145).rgb_format()
        self.BURLYWOOD3 = self.RGB(205, 170, 125).rgb_format()
        self.BURLYWOOD4 = self.RGB(139, 115, 85).rgb_format()
        self.BURNTSIENNA = self.RGB(138, 54, 15).rgb_format()
        self.BURNTUMBER = self.RGB(138, 51, 36).rgb_format()
        self.CADETBLUE = self.RGB(95, 158, 160).rgb_format()
        self.CADETBLUE1 = self.RGB(152, 245, 255).rgb_format()
        self.CADETBLUE2 = self.RGB(142, 229, 238).rgb_format()
        self.CADETBLUE3 = self.RGB(122, 197, 205).rgb_format()
        self.CADETBLUE4 = self.RGB(83, 134, 139).rgb_format()
        self.CADMIUMORANGE = self.RGB(255, 97, 3).rgb_format()
        self.CADMIUMYELLOW = self.RGB(255, 153, 18).rgb_format()
        self.CARROT = self.RGB(237, 145, 33).rgb_format()
        self.CHARTREUSE1 = self.RGB(127, 255, 0).rgb_format()
        self.CHARTREUSE2 = self.RGB(118, 238, 0).rgb_format()
        self.CHARTREUSE3 = self.RGB(102, 205, 0).rgb_format()
        self.CHARTREUSE4 = self.RGB(69, 139, 0).rgb_format()
        self.CHOCOLATE = self.RGB(210, 105, 30).rgb_format()
        self.CHOCOLATE1 = self.RGB(255, 127, 36).rgb_format()
        self.CHOCOLATE2 = self.RGB(238, 118, 33).rgb_format()
        self.CHOCOLATE3 = self.RGB(205, 102, 29).rgb_format()
        self.CHOCOLATE4 = self.RGB(139, 69, 19).rgb_format()
        self.COBALT = self.RGB(61, 89, 171).rgb_format()
        self.COBALTGREEN = self.RGB(61, 145, 64).rgb_format()
        self.COLDGREY = self.RGB(128, 138, 135).rgb_format()
        self.CORAL = self.RGB(255, 127, 80).rgb_format()
        self.CORAL1 = self.RGB(255, 114, 86).rgb_format()
        self.CORAL2 = self.RGB(238, 106, 80).rgb_format()
        self.CORAL3 = self.RGB(205, 91, 69).rgb_format()
        self.CORAL4 = self.RGB(139, 62, 47).rgb_format()
        self.CORNFLOWERBLUE = self.RGB(100, 149, 237).rgb_format()
        self.CORNSILK1 = self.RGB(255, 248, 220).rgb_format()
        self.CORNSILK2 = self.RGB(238, 232, 205).rgb_format()
        self.CORNSILK3 = self.RGB(205, 200, 177).rgb_format()
        self.CORNSILK4 = self.RGB(139, 136, 120).rgb_format()
        self.CRIMSON = self.RGB(220, 20, 60).rgb_format()
        self.CYAN2 = self.RGB(0, 238, 238).rgb_format()
        self.CYAN3 = self.RGB(0, 205, 205).rgb_format()
        self.CYAN4 = self.RGB(0, 139, 139).rgb_format()
        self.DARKGOLDENROD = self.RGB(184, 134, 11).rgb_format()
        self.DARKGOLDENROD1 = self.RGB(255, 185, 15).rgb_format()
        self.DARKGOLDENROD2 = self.RGB(238, 173, 14).rgb_format()
        self.DARKGOLDENROD3 = self.RGB(205, 149, 12).rgb_format()
        self.DARKGOLDENROD4 = self.RGB(139, 101, 8).rgb_format()
        self.DARKGRAY = self.RGB(169, 169, 169).rgb_format()
        self.DARKGREEN = self.RGB(0, 100, 0).rgb_format()
        self.DARKKHAKI = self.RGB(189, 183, 107).rgb_format()
        self.DARKOLIVEGREEN = self.RGB(85, 107, 47).rgb_format()
        self.DARKOLIVEGREEN1 = self.RGB(202, 255, 112).rgb_format()
        self.DARKOLIVEGREEN2 = self.RGB(188, 238, 104).rgb_format()
        self.DARKOLIVEGREEN3 = self.RGB(162, 205, 90).rgb_format()
        self.DARKOLIVEGREEN4 = self.RGB(110, 139, 61).rgb_format()
        self.DARKORANGE = self.RGB(255, 140, 0).rgb_format()
        self.DARKORANGE1 = self.RGB(255, 127, 0).rgb_format()
        self.DARKORANGE2 = self.RGB(238, 118, 0).rgb_format()
        self.DARKORANGE3 = self.RGB(205, 102, 0).rgb_format()
        self.DARKORANGE4 = self.RGB(139, 69, 0).rgb_format()
        self.DARKORCHID = self.RGB(153, 50, 204).rgb_format()
        self.DARKORCHID1 = self.RGB(191, 62, 255).rgb_format()
        self.DARKORCHID2 = self.RGB(178, 58, 238).rgb_format()
        self.DARKORCHID3 = self.RGB(154, 50, 205).rgb_format()
        self.DARKORCHID4 = self.RGB(104, 34, 139).rgb_format()
        self.DARKSALMON = self.RGB(233, 150, 122).rgb_format()
        self.DARKSEAGREEN = self.RGB(143, 188, 143).rgb_format()
        self.DARKSEAGREEN1 = self.RGB(193, 255, 193).rgb_format()
        self.DARKSEAGREEN2 = self.RGB(180, 238, 180).rgb_format()
        self.DARKSEAGREEN3 = self.RGB(155, 205, 155).rgb_format()
        self.DARKSEAGREEN4 = self.RGB(105, 139, 105).rgb_format()
        self.DARKSLATEBLUE = self.RGB(72, 61, 139).rgb_format()
        self.DARKSLATEGRAY = self.RGB(47, 79, 79).rgb_format()
        self.DARKSLATEGRAY1 = self.RGB(151, 255, 255).rgb_format()
        self.DARKSLATEGRAY2 = self.RGB(141, 238, 238).rgb_format()
        self.DARKSLATEGRAY3 = self.RGB(121, 205, 205).rgb_format()
        self.DARKSLATEGRAY4 = self.RGB(82, 139, 139).rgb_format()
        self.DARKTURQUOISE = self.RGB(0, 206, 209).rgb_format()
        self.DARKVIOLET = self.RGB(148, 0, 211).rgb_format()
        self.DEEPPINK1 = self.RGB(255, 20, 147).rgb_format()
        self.DEEPPINK2 = self.RGB(238, 18, 137).rgb_format()
        self.DEEPPINK3 = self.RGB(205, 16, 118).rgb_format()
        self.DEEPPINK4 = self.RGB(139, 10, 80).rgb_format()
        self.DEEPSKYBLUE1 = self.RGB(0, 191, 255).rgb_format()
        self.DEEPSKYBLUE2 = self.RGB(0, 178, 238).rgb_format()
        self.DEEPSKYBLUE3 = self.RGB(0, 154, 205).rgb_format()
        self.DEEPSKYBLUE4 = self.RGB(0, 104, 139).rgb_format()
        self.DIMGRAY = self.RGB(105, 105, 105).rgb_format()
        self.DIMGRAY = self.RGB(105, 105, 105).rgb_format()
        self.DODGERBLUE1 = self.RGB(30, 144, 255).rgb_format()
        self.DODGERBLUE2 = self.RGB(28, 134, 238).rgb_format()
        self.DODGERBLUE3 = self.RGB(24, 116, 205).rgb_format()
        self.DODGERBLUE4 = self.RGB(16, 78, 139).rgb_format()
        self.EGGSHELL = self.RGB(252, 230, 201).rgb_format()
        self.EMERALDGREEN = self.RGB(0, 201, 87).rgb_format()
        self.FIREBRICK = self.RGB(178, 34, 34).rgb_format()
        self.FIREBRICK1 = self.RGB(255, 48, 48).rgb_format()
        self.FIREBRICK2 = self.RGB(238, 44, 44).rgb_format()
        self.FIREBRICK3 = self.RGB(205, 38, 38).rgb_format()
        self.FIREBRICK4 = self.RGB(139, 26, 26).rgb_format()
        self.FLESH = self.RGB(255, 125, 64).rgb_format()
        self.FLORALWHITE = self.RGB(255, 250, 240).rgb_format()
        self.FORESTGREEN = self.RGB(34, 139, 34).rgb_format()
        self.GAINSBORO = self.RGB(220, 220, 220).rgb_format()
        self.GHOSTWHITE = self.RGB(248, 248, 255).rgb_format()
        self.GOLD1 = self.RGB(255, 215, 0).rgb_format()
        self.GOLD2 = self.RGB(238, 201, 0).rgb_format()
        self.GOLD3 = self.RGB(205, 173, 0).rgb_format()
        self.GOLD4 = self.RGB(139, 117, 0).rgb_format()
        self.GOLDENROD = self.RGB(218, 165, 32).rgb_format()
        self.GOLDENROD1 = self.RGB(255, 193, 37).rgb_format()
        self.GOLDENROD2 = self.RGB(238, 180, 34).rgb_format()
        self.GOLDENROD3 = self.RGB(205, 155, 29).rgb_format()
        self.GOLDENROD4 = self.RGB(139, 105, 20).rgb_format()
        self.GRAY = self.RGB(128, 128, 128).rgb_format()
        self.GRAY1 = self.RGB(3, 3, 3).rgb_format()
        self.GRAY10 = self.RGB(26, 26, 26).rgb_format()
        self.GRAY11 = self.RGB(28, 28, 28).rgb_format()
        self.GRAY12 = self.RGB(31, 31, 31).rgb_format()
        self.GRAY13 = self.RGB(33, 33, 33).rgb_format()
        self.GRAY14 = self.RGB(36, 36, 36).rgb_format()
        self.GRAY15 = self.RGB(38, 38, 38).rgb_format()
        self.GRAY16 = self.RGB(41, 41, 41).rgb_format()
        self.GRAY17 = self.RGB(43, 43, 43).rgb_format()
        self.GRAY18 = self.RGB(46, 46, 46).rgb_format()
        self.GRAY19 = self.RGB(48, 48, 48).rgb_format()
        self.GRAY2 = self.RGB(5, 5, 5).rgb_format()
        self.GRAY20 = self.RGB(51, 51, 51).rgb_format()
        self.GRAY21 = self.RGB(54, 54, 54).rgb_format()
        self.GRAY22 = self.RGB(56, 56, 56).rgb_format()
        self.GRAY23 = self.RGB(59, 59, 59).rgb_format()
        self.GRAY24 = self.RGB(61, 61, 61).rgb_format()
        self.GRAY25 = self.RGB(64, 64, 64).rgb_format()
        self.GRAY26 = self.RGB(66, 66, 66).rgb_format()
        self.GRAY27 = self.RGB(69, 69, 69).rgb_format()
        self.GRAY28 = self.RGB(71, 71, 71).rgb_format()
        self.GRAY29 = self.RGB(74, 74, 74).rgb_format()
        self.GRAY3 = self.RGB(8, 8, 8).rgb_format()
        self.GRAY30 = self.RGB(77, 77, 77).rgb_format()
        self.GRAY31 = self.RGB(79, 79, 79).rgb_format()
        self.GRAY32 = self.RGB(82, 82, 82).rgb_format()
        self.GRAY33 = self.RGB(84, 84, 84).rgb_format()
        self.GRAY34 = self.RGB(87, 87, 87).rgb_format()
        self.GRAY35 = self.RGB(89, 89, 89).rgb_format()
        self.GRAY36 = self.RGB(92, 92, 92).rgb_format()
        self.GRAY37 = self.RGB(94, 94, 94).rgb_format()
        self.GRAY38 = self.RGB(97, 97, 97).rgb_format()
        self.GRAY39 = self.RGB(99, 99, 99).rgb_format()
        self.GRAY4 = self.RGB(10, 10, 10).rgb_format()
        self.GRAY40 = self.RGB(102, 102, 102).rgb_format()
        self.GRAY42 = self.RGB(107, 107, 107).rgb_format()
        self.GRAY43 = self.RGB(110, 110, 110).rgb_format()
        self.GRAY44 = self.RGB(112, 112, 112).rgb_format()
        self.GRAY45 = self.RGB(115, 115, 115).rgb_format()
        self.GRAY46 = self.RGB(117, 117, 117).rgb_format()
        self.GRAY47 = self.RGB(120, 120, 120).rgb_format()
        self.GRAY48 = self.RGB(122, 122, 122).rgb_format()
        self.GRAY49 = self.RGB(125, 125, 125).rgb_format()
        self.GRAY5 = self.RGB(13, 13, 13).rgb_format()
        self.GRAY50 = self.RGB(127, 127, 127).rgb_format()
        self.GRAY51 = self.RGB(130, 130, 130).rgb_format()
        self.GRAY52 = self.RGB(133, 133, 133).rgb_format()
        self.GRAY53 = self.RGB(135, 135, 135).rgb_format()
        self.GRAY54 = self.RGB(138, 138, 138).rgb_format()
        self.GRAY55 = self.RGB(140, 140, 140).rgb_format()
        self.GRAY56 = self.RGB(143, 143, 143).rgb_format()
        self.GRAY57 = self.RGB(145, 145, 145).rgb_format()
        self.GRAY58 = self.RGB(148, 148, 148).rgb_format()
        self.GRAY59 = self.RGB(150, 150, 150).rgb_format()
        self.GRAY6 = self.RGB(15, 15, 15).rgb_format()
        self.GRAY60 = self.RGB(153, 153, 153).rgb_format()
        self.GRAY61 = self.RGB(156, 156, 156).rgb_format()
        self.GRAY62 = self.RGB(158, 158, 158).rgb_format()
        self.GRAY63 = self.RGB(161, 161, 161).rgb_format()
        self.GRAY64 = self.RGB(163, 163, 163).rgb_format()
        self.GRAY65 = self.RGB(166, 166, 166).rgb_format()
        self.GRAY66 = self.RGB(168, 168, 168).rgb_format()
        self.GRAY67 = self.RGB(171, 171, 171).rgb_format()
        self.GRAY68 = self.RGB(173, 173, 173).rgb_format()
        self.GRAY69 = self.RGB(176, 176, 176).rgb_format()
        self.GRAY7 = self.RGB(18, 18, 18).rgb_format()
        self.GRAY70 = self.RGB(179, 179, 179).rgb_format()
        self.GRAY71 = self.RGB(181, 181, 181).rgb_format()
        self.GRAY72 = self.RGB(184, 184, 184).rgb_format()
        self.GRAY73 = self.RGB(186, 186, 186).rgb_format()
        self.GRAY74 = self.RGB(189, 189, 189).rgb_format()
        self.GRAY75 = self.RGB(191, 191, 191).rgb_format()
        self.GRAY76 = self.RGB(194, 194, 194).rgb_format()
        self.GRAY77 = self.RGB(196, 196, 196).rgb_format()
        self.GRAY78 = self.RGB(199, 199, 199).rgb_format()
        self.GRAY79 = self.RGB(201, 201, 201).rgb_format()
        self.GRAY8 = self.RGB(20, 20, 20).rgb_format()
        self.GRAY80 = self.RGB(204, 204, 204).rgb_format()
        self.GRAY81 = self.RGB(207, 207, 207).rgb_format()
        self.GRAY82 = self.RGB(209, 209, 209).rgb_format()
        self.GRAY83 = self.RGB(212, 212, 212).rgb_format()
        self.GRAY84 = self.RGB(214, 214, 214).rgb_format()
        self.GRAY85 = self.RGB(217, 217, 217).rgb_format()
        self.GRAY86 = self.RGB(219, 219, 219).rgb_format()
        self.GRAY87 = self.RGB(222, 222, 222).rgb_format()
        self.GRAY88 = self.RGB(224, 224, 224).rgb_format()
        self.GRAY89 = self.RGB(227, 227, 227).rgb_format()
        self.GRAY9 = self.RGB(23, 23, 23).rgb_format()
        self.GRAY90 = self.RGB(229, 229, 229).rgb_format()
        self.GRAY91 = self.RGB(232, 232, 232).rgb_format()
        self.GRAY92 = self.RGB(235, 235, 235).rgb_format()
        self.GRAY93 = self.RGB(237, 237, 237).rgb_format()
        self.GRAY94 = self.RGB(240, 240, 240).rgb_format()
        self.GRAY95 = self.RGB(242, 242, 242).rgb_format()
        self.GRAY97 = self.RGB(247, 247, 247).rgb_format()
        self.GRAY98 = self.RGB(250, 250, 250).rgb_format()
        self.GRAY99 = self.RGB(252, 252, 252).rgb_format()
        self.GREEN = self.RGB(0, 128, 0).rgb_format()
        self.GREEN1 = self.RGB(0, 255, 0).rgb_format()
        self.GREEN2 = self.RGB(0, 238, 0).rgb_format()
        self.GREEN3 = self.RGB(0, 205, 0).rgb_format()
        self.GREEN4 = self.RGB(0, 139, 0).rgb_format()
        self.GREENYELLOW = self.RGB(173, 255, 47).rgb_format()
        self.HONEYDEW1 = self.RGB(240, 255, 240).rgb_format()
        self.HONEYDEW2 = self.RGB(224, 238, 224).rgb_format()
        self.HONEYDEW3 = self.RGB(193, 205, 193).rgb_format()
        self.HONEYDEW4 = self.RGB(131, 139, 131).rgb_format()
        self.HOTPINK = self.RGB(255, 105, 180).rgb_format()
        self.HOTPINK1 = self.RGB(255, 110, 180).rgb_format()
        self.HOTPINK2 = self.RGB(238, 106, 167).rgb_format()
        self.HOTPINK3 = self.RGB(205, 96, 144).rgb_format()
        self.HOTPINK4 = self.RGB(139, 58, 98).rgb_format()
        self.INDIANRED = self.RGB(176, 23, 31).rgb_format()
        self.INDIANRED = self.RGB(205, 92, 92).rgb_format()
        self.INDIANRED1 = self.RGB(255, 106, 106).rgb_format()
        self.INDIANRED2 = self.RGB(238, 99, 99).rgb_format()
        self.INDIANRED3 = self.RGB(205, 85, 85).rgb_format()
        self.INDIANRED4 = self.RGB(139, 58, 58).rgb_format()
        self.INDIGO = self.RGB(75, 0, 130).rgb_format()
        self.IVORY1 = self.RGB(255, 255, 240).rgb_format()
        self.IVORY2 = self.RGB(238, 238, 224).rgb_format()
        self.IVORY3 = self.RGB(205, 205, 193).rgb_format()
        self.IVORY4 = self.RGB(139, 139, 131).rgb_format()
        self.IVORYBLACK = self.RGB(41, 36, 33).rgb_format()
        self.KHAKI = self.RGB(240, 230, 140).rgb_format()
        self.KHAKI1 = self.RGB(255, 246, 143).rgb_format()
        self.KHAKI2 = self.RGB(238, 230, 133).rgb_format()
        self.KHAKI3 = self.RGB(205, 198, 115).rgb_format()
        self.KHAKI4 = self.RGB(139, 134, 78).rgb_format()
        self.LAVENDER = self.RGB(230, 230, 250).rgb_format()
        self.LAVENDERBLUSH1 = self.RGB(255, 240, 245).rgb_format()
        self.LAVENDERBLUSH2 = self.RGB(238, 224, 229).rgb_format()
        self.LAVENDERBLUSH3 = self.RGB(205, 193, 197).rgb_format()
        self.LAVENDERBLUSH4 = self.RGB(139, 131, 134).rgb_format()
        self.LAWNGREEN = self.RGB(124, 252, 0).rgb_format()
        self.LEMONCHIFFON1 = self.RGB(255, 250, 205).rgb_format()
        self.LEMONCHIFFON2 = self.RGB(238, 233, 191).rgb_format()
        self.LEMONCHIFFON3 = self.RGB(205, 201, 165).rgb_format()
        self.LEMONCHIFFON4 = self.RGB(139, 137, 112).rgb_format()
        self.LIGHTBLUE = self.RGB(173, 216, 230).rgb_format()
        self.LIGHTBLUE1 = self.RGB(191, 239, 255).rgb_format()
        self.LIGHTBLUE2 = self.RGB(178, 223, 238).rgb_format()
        self.LIGHTBLUE3 = self.RGB(154, 192, 205).rgb_format()
        self.LIGHTBLUE4 = self.RGB(104, 131, 139).rgb_format()
        self.LIGHTCORAL = self.RGB(240, 128, 128).rgb_format()
        self.LIGHTCYAN1 = self.RGB(224, 255, 255).rgb_format()
        self.LIGHTCYAN2 = self.RGB(209, 238, 238).rgb_format()
        self.LIGHTCYAN3 = self.RGB(180, 205, 205).rgb_format()
        self.LIGHTCYAN4 = self.RGB(122, 139, 139).rgb_format()
        self.LIGHTGOLDENROD1 = self.RGB(255, 236, 139).rgb_format()
        self.LIGHTGOLDENROD2 = self.RGB(238, 220, 130).rgb_format()
        self.LIGHTGOLDENROD3 = self.RGB(205, 190, 112).rgb_format()
        self.LIGHTGOLDENROD4 = self.RGB(139, 129, 76).rgb_format()
        self.LIGHTGOLDENRODYELLOW = self.RGB(250, 250, 210).rgb_format()
        self.LIGHTGREY = self.RGB(211, 211, 211).rgb_format()
        self.LIGHTPINK = self.RGB(255, 182, 193).rgb_format()
        self.LIGHTPINK1 = self.RGB(255, 174, 185).rgb_format()
        self.LIGHTPINK2 = self.RGB(238, 162, 173).rgb_format()
        self.LIGHTPINK3 = self.RGB(205, 140, 149).rgb_format()
        self.LIGHTPINK4 = self.RGB(139, 95, 101).rgb_format()
        self.LIGHTSALMON1 = self.RGB(255, 160, 122).rgb_format()
        self.LIGHTSALMON2 = self.RGB(238, 149, 114).rgb_format()
        self.LIGHTSALMON3 = self.RGB(205, 129, 98).rgb_format()
        self.LIGHTSALMON4 = self.RGB(139, 87, 66).rgb_format()
        self.LIGHTSEAGREEN = self.RGB(32, 178, 170).rgb_format()
        self.LIGHTSKYBLUE = self.RGB(135, 206, 250).rgb_format()
        self.LIGHTSKYBLUE1 = self.RGB(176, 226, 255).rgb_format()
        self.LIGHTSKYBLUE2 = self.RGB(164, 211, 238).rgb_format()
        self.LIGHTSKYBLUE3 = self.RGB(141, 182, 205).rgb_format()
        self.LIGHTSKYBLUE4 = self.RGB(96, 123, 139).rgb_format()
        self.LIGHTSLATEBLUE = self.RGB(132, 112, 255).rgb_format()
        self.LIGHTSLATEGRAY = self.RGB(119, 136, 153).rgb_format()
        self.LIGHTSTEELBLUE = self.RGB(176, 196, 222).rgb_format()
        self.LIGHTSTEELBLUE1 = self.RGB(202, 225, 255).rgb_format()
        self.LIGHTSTEELBLUE2 = self.RGB(188, 210, 238).rgb_format()
        self.LIGHTSTEELBLUE3 = self.RGB(162, 181, 205).rgb_format()
        self.LIGHTSTEELBLUE4 = self.RGB(110, 123, 139).rgb_format()
        self.LIGHTYELLOW1 = self.RGB(255, 255, 224).rgb_format()
        self.LIGHTYELLOW2 = self.RGB(238, 238, 209).rgb_format()
        self.LIGHTYELLOW3 = self.RGB(205, 205, 180).rgb_format()
        self.LIGHTYELLOW4 = self.RGB(139, 139, 122).rgb_format()
        self.LIMEGREEN = self.RGB(50, 205, 50).rgb_format()
        self.LINEN = self.RGB(250, 240, 230).rgb_format()
        self.MAGENTA = self.RGB(255, 0, 255).rgb_format()
        self.MAGENTA2 = self.RGB(238, 0, 238).rgb_format()
        self.MAGENTA3 = self.RGB(205, 0, 205).rgb_format()
        self.MAGENTA4 = self.RGB(139, 0, 139).rgb_format()
        self.MANGANESEBLUE = self.RGB(3, 168, 158).rgb_format()
        self.MAROON = self.RGB(128, 0, 0).rgb_format()
        self.MAROON1 = self.RGB(255, 52, 179).rgb_format()
        self.MAROON2 = self.RGB(238, 48, 167).rgb_format()
        self.MAROON3 = self.RGB(205, 41, 144).rgb_format()
        self.MAROON4 = self.RGB(139, 28, 98).rgb_format()
        self.MEDIUMORCHID = self.RGB(186, 85, 211).rgb_format()
        self.MEDIUMORCHID1 = self.RGB(224, 102, 255).rgb_format()
        self.MEDIUMORCHID2 = self.RGB(209, 95, 238).rgb_format()
        self.MEDIUMORCHID3 = self.RGB(180, 82, 205).rgb_format()
        self.MEDIUMORCHID4 = self.RGB(122, 55, 139).rgb_format()
        self.MEDIUMPURPLE = self.RGB(147, 112, 219).rgb_format()
        self.MEDIUMPURPLE1 = self.RGB(171, 130, 255).rgb_format()
        self.MEDIUMPURPLE2 = self.RGB(159, 121, 238).rgb_format()
        self.MEDIUMPURPLE3 = self.RGB(137, 104, 205).rgb_format()
        self.MEDIUMPURPLE4 = self.RGB(93, 71, 139).rgb_format()
        self.MEDIUMSEAGREEN = self.RGB(60, 179, 113).rgb_format()
        self.MEDIUMSLATEBLUE = self.RGB(123, 104, 238).rgb_format()
        self.MEDIUMSPRINGGREEN = self.RGB(0, 250, 154).rgb_format()
        self.MEDIUMTURQUOISE = self.RGB(72, 209, 204).rgb_format()
        self.MEDIUMVIOLETRED = self.RGB(199, 21, 133).rgb_format()
        self.MELON = self.RGB(227, 168, 105).rgb_format()
        self.MIDNIGHTBLUE = self.RGB(25, 25, 112).rgb_format()
        self.MINT = self.RGB(189, 252, 201).rgb_format()
        self.MINTCREAM = self.RGB(245, 255, 250).rgb_format()
        self.MISTYROSE1 = self.RGB(255, 228, 225).rgb_format()
        self.MISTYROSE2 = self.RGB(238, 213, 210).rgb_format()
        self.MISTYROSE3 = self.RGB(205, 183, 181).rgb_format()
        self.MISTYROSE4 = self.RGB(139, 125, 123).rgb_format()
        self.MOCCASIN = self.RGB(255, 228, 181).rgb_format()
        self.NAVAJOWHITE1 = self.RGB(255, 222, 173).rgb_format()
        self.NAVAJOWHITE2 = self.RGB(238, 207, 161).rgb_format()
        self.NAVAJOWHITE3 = self.RGB(205, 179, 139).rgb_format()
        self.NAVAJOWHITE4 = self.RGB(139, 121, 94).rgb_format()
        self.NAVY = self.RGB(0, 0, 128).rgb_format()
        self.OLDLACE = self.RGB(253, 245, 230).rgb_format()
        self.OLIVE = self.RGB(128, 128, 0).rgb_format()
        self.OLIVEDRAB = self.RGB(107, 142, 35).rgb_format()
        self.OLIVEDRAB1 = self.RGB(192, 255, 62).rgb_format()
        self.OLIVEDRAB2 = self.RGB(179, 238, 58).rgb_format()
        self.OLIVEDRAB3 = self.RGB(154, 205, 50).rgb_format()
        self.OLIVEDRAB4 = self.RGB(105, 139, 34).rgb_format()
        self.ORANGE = self.RGB(255, 128, 0).rgb_format()
        self.ORANGE1 = self.RGB(255, 165, 0).rgb_format()
        self.ORANGE2 = self.RGB(238, 154, 0).rgb_format()
        self.ORANGE3 = self.RGB(205, 133, 0).rgb_format()
        self.ORANGE4 = self.RGB(139, 90, 0).rgb_format()
        self.ORANGERED1 = self.RGB(255, 69, 0).rgb_format()
        self.ORANGERED2 = self.RGB(238, 64, 0).rgb_format()
        self.ORANGERED3 = self.RGB(205, 55, 0).rgb_format()
        self.ORANGERED4 = self.RGB(139, 37, 0).rgb_format()
        self.ORCHID = self.RGB(218, 112, 214).rgb_format()
        self.ORCHID1 = self.RGB(255, 131, 250).rgb_format()
        self.ORCHID2 = self.RGB(238, 122, 233).rgb_format()
        self.ORCHID3 = self.RGB(205, 105, 201).rgb_format()
        self.ORCHID4 = self.RGB(139, 71, 137).rgb_format()
        self.PALEGOLDENROD = self.RGB(238, 232, 170).rgb_format()
        self.PALEGREEN = self.RGB(152, 251, 152).rgb_format()
        self.PALEGREEN1 = self.RGB(154, 255, 154).rgb_format()
        self.PALEGREEN2 = self.RGB(144, 238, 144).rgb_format()
        self.PALEGREEN3 = self.RGB(124, 205, 124).rgb_format()
        self.PALEGREEN4 = self.RGB(84, 139, 84).rgb_format()
        self.PALETURQUOISE1 = self.RGB(187, 255, 255).rgb_format()
        self.PALETURQUOISE2 = self.RGB(174, 238, 238).rgb_format()
        self.PALETURQUOISE3 = self.RGB(150, 205, 205).rgb_format()
        self.PALETURQUOISE4 = self.RGB(102, 139, 139).rgb_format()
        self.PALEVIOLETRED = self.RGB(219, 112, 147).rgb_format()
        self.PALEVIOLETRED1 = self.RGB(255, 130, 171).rgb_format()
        self.PALEVIOLETRED2 = self.RGB(238, 121, 159).rgb_format()
        self.PALEVIOLETRED3 = self.RGB(205, 104, 137).rgb_format()
        self.PALEVIOLETRED4 = self.RGB(139, 71, 93).rgb_format()
        self.PAPAYAWHIP = self.RGB(255, 239, 213).rgb_format()
        self.PEACHPUFF1 = self.RGB(255, 218, 185).rgb_format()
        self.PEACHPUFF2 = self.RGB(238, 203, 173).rgb_format()
        self.PEACHPUFF3 = self.RGB(205, 175, 149).rgb_format()
        self.PEACHPUFF4 = self.RGB(139, 119, 101).rgb_format()
        self.PEACOCK = self.RGB(51, 161, 201).rgb_format()
        self.PINK = self.RGB(255, 192, 203).rgb_format()
        self.PINK1 = self.RGB(255, 181, 197).rgb_format()
        self.PINK2 = self.RGB(238, 169, 184).rgb_format()
        self.PINK3 = self.RGB(205, 145, 158).rgb_format()
        self.PINK4 = self.RGB(139, 99, 108).rgb_format()
        self.PLUM = self.RGB(221, 160, 221).rgb_format()
        self.PLUM1 = self.RGB(255, 187, 255).rgb_format()
        self.PLUM2 = self.RGB(238, 174, 238).rgb_format()
        self.PLUM3 = self.RGB(205, 150, 205).rgb_format()
        self.PLUM4 = self.RGB(139, 102, 139).rgb_format()
        self.POWDERBLUE = self.RGB(176, 224, 230).rgb_format()
        self.PURPLE = self.RGB(128, 0, 128).rgb_format()
        self.PURPLE1 = self.RGB(155, 48, 255).rgb_format()
        self.PURPLE2 = self.RGB(145, 44, 238).rgb_format()
        self.PURPLE3 = self.RGB(125, 38, 205).rgb_format()
        self.PURPLE4 = self.RGB(85, 26, 139).rgb_format()
        self.RASPBERRY = self.RGB(135, 38, 87).rgb_format()
        self.RAWSIENNA = self.RGB(199, 97, 20).rgb_format()
        self.RED1 = self.RGB(255, 0, 0).rgb_format()
        self.RED2 = self.RGB(238, 0, 0).rgb_format()
        self.RED3 = self.RGB(205, 0, 0).rgb_format()
        self.RED4 = self.RGB(139, 0, 0).rgb_format()
        self.ROSYBROWN = self.RGB(188, 143, 143).rgb_format()
        self.ROSYBROWN1 = self.RGB(255, 193, 193).rgb_format()
        self.ROSYBROWN2 = self.RGB(238, 180, 180).rgb_format()
        self.ROSYBROWN3 = self.RGB(205, 155, 155).rgb_format()
        self.ROSYBROWN4 = self.RGB(139, 105, 105).rgb_format()
        self.ROYALBLUE = self.RGB(65, 105, 225).rgb_format()
        self.ROYALBLUE1 = self.RGB(72, 118, 255).rgb_format()
        self.ROYALBLUE2 = self.RGB(67, 110, 238).rgb_format()
        self.ROYALBLUE3 = self.RGB(58, 95, 205).rgb_format()
        self.ROYALBLUE4 = self.RGB(39, 64, 139).rgb_format()
        self.SALMON = self.RGB(250, 128, 114).rgb_format()
        self.SALMON1 = self.RGB(255, 140, 105).rgb_format()
        self.SALMON2 = self.RGB(238, 130, 98).rgb_format()
        self.SALMON3 = self.RGB(205, 112, 84).rgb_format()
        self.SALMON4 = self.RGB(139, 76, 57).rgb_format()
        self.SANDYBROWN = self.RGB(244, 164, 96).rgb_format()
        self.SAPGREEN = self.RGB(48, 128, 20).rgb_format()
        self.SEAGREEN1 = self.RGB(84, 255, 159).rgb_format()
        self.SEAGREEN2 = self.RGB(78, 238, 148).rgb_format()
        self.SEAGREEN3 = self.RGB(67, 205, 128).rgb_format()
        self.SEAGREEN4 = self.RGB(46, 139, 87).rgb_format()
        self.SEASHELL1 = self.RGB(255, 245, 238).rgb_format()
        self.SEASHELL2 = self.RGB(238, 229, 222).rgb_format()
        self.SEASHELL3 = self.RGB(205, 197, 191).rgb_format()
        self.SEASHELL4 = self.RGB(139, 134, 130).rgb_format()
        self.SEPIA = self.RGB(94, 38, 18).rgb_format()
        self.SGIBEET = self.RGB(142, 56, 142).rgb_format()
        self.SGIBRIGHTGRAY = self.RGB(197, 193, 170).rgb_format()
        self.SGICHARTREUSE = self.RGB(113, 198, 113).rgb_format()
        self.SGIDARKGRAY = self.RGB(85, 85, 85).rgb_format()
        self.SGIGRAY12 = self.RGB(30, 30, 30).rgb_format()
        self.SGIGRAY16 = self.RGB(40, 40, 40).rgb_format()
        self.SGIGRAY32 = self.RGB(81, 81, 81).rgb_format()
        self.SGIGRAY36 = self.RGB(91, 91, 91).rgb_format()
        self.SGIGRAY52 = self.RGB(132, 132, 132).rgb_format()
        self.SGIGRAY56 = self.RGB(142, 142, 142).rgb_format()
        self.SGIGRAY72 = self.RGB(183, 183, 183).rgb_format()
        self.SGIGRAY76 = self.RGB(193, 193, 193).rgb_format()
        self.SGIGRAY92 = self.RGB(234, 234, 234).rgb_format()
        self.SGIGRAY96 = self.RGB(244, 244, 244).rgb_format()
        self.SGILIGHTBLUE = self.RGB(125, 158, 192).rgb_format()
        self.SGILIGHTGRAY = self.RGB(170, 170, 170).rgb_format()
        self.SGIOLIVEDRAB = self.RGB(142, 142, 56).rgb_format()
        self.SGISALMON = self.RGB(198, 113, 113).rgb_format()
        self.SGISLATEBLUE = self.RGB(113, 113, 198).rgb_format()
        self.SGITEAL = self.RGB(56, 142, 142).rgb_format()
        self.SIENNA = self.RGB(160, 82, 45).rgb_format()
        self.SIENNA1 = self.RGB(255, 130, 71).rgb_format()
        self.SIENNA2 = self.RGB(238, 121, 66).rgb_format()
        self.SIENNA3 = self.RGB(205, 104, 57).rgb_format()
        self.SIENNA4 = self.RGB(139, 71, 38).rgb_format()
        self.SILVER = self.RGB(192, 192, 192).rgb_format()
        self.SKYBLUE = self.RGB(135, 206, 235).rgb_format()
        self.SKYBLUE1 = self.RGB(135, 206, 255).rgb_format()
        self.SKYBLUE2 = self.RGB(126, 192, 238).rgb_format()
        self.SKYBLUE3 = self.RGB(108, 166, 205).rgb_format()
        self.SKYBLUE4 = self.RGB(74, 112, 139).rgb_format()
        self.SLATEBLUE = self.RGB(106, 90, 205).rgb_format()
        self.SLATEBLUE1 = self.RGB(131, 111, 255).rgb_format()
        self.SLATEBLUE2 = self.RGB(122, 103, 238).rgb_format()
        self.SLATEBLUE3 = self.RGB(105, 89, 205).rgb_format()
        self.SLATEBLUE4 = self.RGB(71, 60, 139).rgb_format()
        self.SLATEGRAY = self.RGB(112, 128, 144).rgb_format()
        self.SLATEGRAY1 = self.RGB(198, 226, 255).rgb_format()
        self.SLATEGRAY2 = self.RGB(185, 211, 238).rgb_format()
        self.SLATEGRAY3 = self.RGB(159, 182, 205).rgb_format()
        self.SLATEGRAY4 = self.RGB(108, 123, 139).rgb_format()
        self.SNOW1 = self.RGB(255, 250, 250).rgb_format()
        self.SNOW2 = self.RGB(238, 233, 233).rgb_format()
        self.SNOW3 = self.RGB(205, 201, 201).rgb_format()
        self.SNOW4 = self.RGB(139, 137, 137).rgb_format()
        self.SPRINGGREEN = self.RGB(0, 255, 127).rgb_format()
        self.SPRINGGREEN1 = self.RGB(0, 238, 118).rgb_format()
        self.SPRINGGREEN2 = self.RGB(0, 205, 102).rgb_format()
        self.SPRINGGREEN3 = self.RGB(0, 139, 69).rgb_format()
        self.STEELBLUE = self.RGB(70, 130, 180).rgb_format()
        self.STEELBLUE1 = self.RGB(99, 184, 255).rgb_format()
        self.STEELBLUE2 = self.RGB(92, 172, 238).rgb_format()
        self.STEELBLUE3 = self.RGB(79, 148, 205).rgb_format()
        self.STEELBLUE4 = self.RGB(54, 100, 139).rgb_format()
        self.TAN = self.RGB(210, 180, 140).rgb_format()
        self.TAN1 = self.RGB(255, 165, 79).rgb_format()
        self.TAN2 = self.RGB(238, 154, 73).rgb_format()
        self.TAN3 = self.RGB(205, 133, 63).rgb_format()
        self.TAN4 = self.RGB(139, 90, 43).rgb_format()
        self.TEAL = self.RGB(0, 128, 128).rgb_format()
        self.THISTLE = self.RGB(216, 191, 216).rgb_format()
        self.THISTLE1 = self.RGB(255, 225, 255).rgb_format()
        self.THISTLE2 = self.RGB(238, 210, 238).rgb_format()
        self.THISTLE3 = self.RGB(205, 181, 205).rgb_format()
        self.THISTLE4 = self.RGB(139, 123, 139).rgb_format()
        self.TOMATO1 = self.RGB(255, 99, 71).rgb_format()
        self.TOMATO2 = self.RGB(238, 92, 66).rgb_format()
        self.TOMATO3 = self.RGB(205, 79, 57).rgb_format()
        self.TOMATO4 = self.RGB(139, 54, 38).rgb_format()
        self.TURQUOISE = self.RGB(64, 224, 208).rgb_format()
        self.TURQUOISE1 = self.RGB(0, 245, 255).rgb_format()
        self.TURQUOISE2 = self.RGB(0, 229, 238).rgb_format()
        self.TURQUOISE3 = self.RGB(0, 197, 205).rgb_format()
        self.TURQUOISE4 = self.RGB(0, 134, 139).rgb_format()
        self.TURQUOISEBLUE = self.RGB(0, 199, 140).rgb_format()
        self.VIOLET = self.RGB(238, 130, 238).rgb_format()
        self.VIOLETRED = self.RGB(208, 32, 144).rgb_format()
        self.VIOLETRED1 = self.RGB(255, 62, 150).rgb_format()
        self.VIOLETRED2 = self.RGB(238, 58, 140).rgb_format()
        self.VIOLETRED3 = self.RGB(205, 50, 120).rgb_format()
        self.VIOLETRED4 = self.RGB(139, 34, 82).rgb_format()
        self.WARMGREY = self.RGB(128, 128, 105).rgb_format()
        self.WHEAT = self.RGB(245, 222, 179).rgb_format()
        self.WHEAT1 = self.RGB(255, 231, 186).rgb_format()
        self.WHEAT2 = self.RGB(238, 216, 174).rgb_format()
        self.WHEAT3 = self.RGB(205, 186, 150).rgb_format()
        self.WHEAT4 = self.RGB(139, 126, 102).rgb_format()
        self.WHITE = self.RGB(255, 255, 255).rgb_format()
        self.WHITESMOKE = self.RGB(245, 245, 245).rgb_format()
        self.WHITESMOKE = self.RGB(245, 245, 245).rgb_format()
        self.YELLOW1 = self.RGB(255, 255, 0).rgb_format()
        self.YELLOW2 = self.RGB(238, 238, 0).rgb_format()
        self.YELLOW3 = self.RGB(205, 205, 0).rgb_format()
        self.YELLOW4 = self.RGB(139, 139, 0).rgb_format()

        return self # <= NOTE return all variables

    def colors_hex(self) -> dict: # DESC => Color in HEX format contants
        """ Return a dictionary of color variables in hexadecimal format.
        
        Returns:
            dict{str: str}: A dictionary containing color variables in hexadecimal format.

        Example:
        ```python
            colors = ColorsConstants()
            hex_colors = colors.colors_hex()
            print(hex_colors)  # Output: {'ALICEBLUE': '#F0F8FF', ...}
        ```
        """
        ALICEBLUE = self.RGB(240, 248, 255).hex_format()
        ANTIQUEWHITE = self.RGB(250, 235, 215).hex_format()
        ANTIQUEWHITE1 = self.RGB(255, 239, 219).hex_format()
        ANTIQUEWHITE2 = self.RGB(238, 223, 204).hex_format()
        ANTIQUEWHITE3 = self.RGB(205, 192, 176).hex_format()
        ANTIQUEWHITE4 = self.RGB(139, 131, 120).hex_format()
        AQUA = self.RGB(0, 255, 255).hex_format()
        AQUAMARINE1 = self.RGB(127, 255, 212).hex_format()
        AQUAMARINE2 = self.RGB(118, 238, 198).hex_format()
        AQUAMARINE3 = self.RGB(102, 205, 170).hex_format()
        AQUAMARINE4 = self.RGB(69, 139, 116).hex_format()
        AZURE1 = self.RGB(240, 255, 255).hex_format()
        AZURE2 = self.RGB(224, 238, 238).hex_format()
        AZURE3 = self.RGB(193, 205, 205).hex_format()
        AZURE4 = self.RGB(131, 139, 139).hex_format()
        BANANA = self.RGB(227, 207, 87).hex_format()
        BEIGE = self.RGB(245, 245, 220).hex_format()
        BISQUE1 = self.RGB(255, 228, 196).hex_format()
        BISQUE2 = self.RGB(238, 213, 183).hex_format()
        BISQUE3 = self.RGB(205, 183, 158).hex_format()
        BISQUE4 = self.RGB(139, 125, 107).hex_format()
        BLACK = self.RGB(0, 0, 0).hex_format()
        BLANCHEDALMOND = self.RGB(255, 235, 205).hex_format()
        BLUE = self.RGB(0, 0, 255).hex_format()
        BLUE2 = self.RGB(0, 0, 238).hex_format()
        BLUE3 = self.RGB(0, 0, 205).hex_format()
        BLUE4 = self.RGB(0, 0, 139).hex_format()
        BLUEVIOLET = self.RGB(138, 43, 226).hex_format()
        BRICK = self.RGB(156, 102, 31).hex_format()
        BROWN = self.RGB(165, 42, 42).hex_format()
        BROWN1 = self.RGB(255, 64, 64).hex_format()
        BROWN2 = self.RGB(238, 59, 59).hex_format()
        BROWN3 = self.RGB(205, 51, 51).hex_format()
        BROWN4 = self.RGB(139, 35, 35).hex_format()
        BURLYWOOD = self.RGB(222, 184, 135).hex_format()
        BURLYWOOD1 = self.RGB(255, 211, 155).hex_format()
        BURLYWOOD2 = self.RGB(238, 197, 145).hex_format()
        BURLYWOOD3 = self.RGB(205, 170, 125).hex_format()
        BURLYWOOD4 = self.RGB(139, 115, 85).hex_format()
        BURNTSIENNA = self.RGB(138, 54, 15).hex_format()
        BURNTUMBER = self.RGB(138, 51, 36).hex_format()
        CADETBLUE = self.RGB(95, 158, 160).hex_format()
        CADETBLUE1 = self.RGB(152, 245, 255).hex_format()
        CADETBLUE2 = self.RGB(142, 229, 238).hex_format()
        CADETBLUE3 = self.RGB(122, 197, 205).hex_format()
        CADETBLUE4 = self.RGB(83, 134, 139).hex_format()
        CADMIUMORANGE = self.RGB(255, 97, 3).hex_format()
        CADMIUMYELLOW = self.RGB(255, 153, 18).hex_format()
        CARROT = self.RGB(237, 145, 33).hex_format()
        CHARTREUSE1 = self.RGB(127, 255, 0).hex_format()
        CHARTREUSE2 = self.RGB(118, 238, 0).hex_format()
        CHARTREUSE3 = self.RGB(102, 205, 0).hex_format()
        CHARTREUSE4 = self.RGB(69, 139, 0).hex_format()
        CHOCOLATE = self.RGB(210, 105, 30).hex_format()
        CHOCOLATE1 = self.RGB(255, 127, 36).hex_format()
        CHOCOLATE2 = self.RGB(238, 118, 33).hex_format()
        CHOCOLATE3 = self.RGB(205, 102, 29).hex_format()
        CHOCOLATE4 = self.RGB(139, 69, 19).hex_format()
        COBALT = self.RGB(61, 89, 171).hex_format()
        COBALTGREEN = self.RGB(61, 145, 64).hex_format()
        COLDGREY = self.RGB(128, 138, 135).hex_format()
        CORAL = self.RGB(255, 127, 80).hex_format()
        CORAL1 = self.RGB(255, 114, 86).hex_format()
        CORAL2 = self.RGB(238, 106, 80).hex_format()
        CORAL3 = self.RGB(205, 91, 69).hex_format()
        CORAL4 = self.RGB(139, 62, 47).hex_format()
        CORNFLOWERBLUE = self.RGB(100, 149, 237).hex_format()
        CORNSILK1 = self.RGB(255, 248, 220).hex_format()
        CORNSILK2 = self.RGB(238, 232, 205).hex_format()
        CORNSILK3 = self.RGB(205, 200, 177).hex_format()
        CORNSILK4 = self.RGB(139, 136, 120).hex_format()
        CRIMSON = self.RGB(220, 20, 60).hex_format()
        CYAN2 = self.RGB(0, 238, 238).hex_format()
        CYAN3 = self.RGB(0, 205, 205).hex_format()
        CYAN4 = self.RGB(0, 139, 139).hex_format()
        DARKGOLDENROD = self.RGB(184, 134, 11).hex_format()
        DARKGOLDENROD1 = self.RGB(255, 185, 15).hex_format()
        DARKGOLDENROD2 = self.RGB(238, 173, 14).hex_format()
        DARKGOLDENROD3 = self.RGB(205, 149, 12).hex_format()
        DARKGOLDENROD4 = self.RGB(139, 101, 8).hex_format()
        DARKGRAY = self.RGB(169, 169, 169).hex_format()
        DARKGREEN = self.RGB(0, 100, 0).hex_format()
        DARKKHAKI = self.RGB(189, 183, 107).hex_format()
        DARKOLIVEGREEN = self.RGB(85, 107, 47).hex_format()
        DARKOLIVEGREEN1 = self.RGB(202, 255, 112).hex_format()
        DARKOLIVEGREEN2 = self.RGB(188, 238, 104).hex_format()
        DARKOLIVEGREEN3 = self.RGB(162, 205, 90).hex_format()
        DARKOLIVEGREEN4 = self.RGB(110, 139, 61).hex_format()
        DARKORANGE = self.RGB(255, 140, 0).hex_format()
        DARKORANGE1 = self.RGB(255, 127, 0).hex_format()
        DARKORANGE2 = self.RGB(238, 118, 0).hex_format()
        DARKORANGE3 = self.RGB(205, 102, 0).hex_format()
        DARKORANGE4 = self.RGB(139, 69, 0).hex_format()
        DARKORCHID = self.RGB(153, 50, 204).hex_format()
        DARKORCHID1 = self.RGB(191, 62, 255).hex_format()
        DARKORCHID2 = self.RGB(178, 58, 238).hex_format()
        DARKORCHID3 = self.RGB(154, 50, 205).hex_format()
        DARKORCHID4 = self.RGB(104, 34, 139).hex_format()
        DARKSALMON = self.RGB(233, 150, 122).hex_format()
        DARKSEAGREEN = self.RGB(143, 188, 143).hex_format()
        DARKSEAGREEN1 = self.RGB(193, 255, 193).hex_format()
        DARKSEAGREEN2 = self.RGB(180, 238, 180).hex_format()
        DARKSEAGREEN3 = self.RGB(155, 205, 155).hex_format()
        DARKSEAGREEN4 = self.RGB(105, 139, 105).hex_format()
        DARKSLATEBLUE = self.RGB(72, 61, 139).hex_format()
        DARKSLATEGRAY = self.RGB(47, 79, 79).hex_format()
        DARKSLATEGRAY1 = self.RGB(151, 255, 255).hex_format()
        DARKSLATEGRAY2 = self.RGB(141, 238, 238).hex_format()
        DARKSLATEGRAY3 = self.RGB(121, 205, 205).hex_format()
        DARKSLATEGRAY4 = self.RGB(82, 139, 139).hex_format()
        DARKTURQUOISE = self.RGB(0, 206, 209).hex_format()
        DARKVIOLET = self.RGB(148, 0, 211).hex_format()
        DEEPPINK1 = self.RGB(255, 20, 147).hex_format()
        DEEPPINK2 = self.RGB(238, 18, 137).hex_format()
        DEEPPINK3 = self.RGB(205, 16, 118).hex_format()
        DEEPPINK4 = self.RGB(139, 10, 80).hex_format()
        DEEPSKYBLUE1 = self.RGB(0, 191, 255).hex_format()
        DEEPSKYBLUE2 = self.RGB(0, 178, 238).hex_format()
        DEEPSKYBLUE3 = self.RGB(0, 154, 205).hex_format()
        DEEPSKYBLUE4 = self.RGB(0, 104, 139).hex_format()
        DIMGRAY = self.RGB(105, 105, 105).hex_format()
        DIMGRAY = self.RGB(105, 105, 105).hex_format()
        DODGERBLUE1 = self.RGB(30, 144, 255).hex_format()
        DODGERBLUE2 = self.RGB(28, 134, 238).hex_format()
        DODGERBLUE3 = self.RGB(24, 116, 205).hex_format()
        DODGERBLUE4 = self.RGB(16, 78, 139).hex_format()
        EGGSHELL = self.RGB(252, 230, 201).hex_format()
        EMERALDGREEN = self.RGB(0, 201, 87).hex_format()
        FIREBRICK = self.RGB(178, 34, 34).hex_format()
        FIREBRICK1 = self.RGB(255, 48, 48).hex_format()
        FIREBRICK2 = self.RGB(238, 44, 44).hex_format()
        FIREBRICK3 = self.RGB(205, 38, 38).hex_format()
        FIREBRICK4 = self.RGB(139, 26, 26).hex_format()
        FLESH = self.RGB(255, 125, 64).hex_format()
        FLORALWHITE = self.RGB(255, 250, 240).hex_format()
        FORESTGREEN = self.RGB(34, 139, 34).hex_format()
        GAINSBORO = self.RGB(220, 220, 220).hex_format()
        GHOSTWHITE = self.RGB(248, 248, 255).hex_format()
        GOLD1 = self.RGB(255, 215, 0).hex_format()
        GOLD2 = self.RGB(238, 201, 0).hex_format()
        GOLD3 = self.RGB(205, 173, 0).hex_format()
        GOLD4 = self.RGB(139, 117, 0).hex_format()
        GOLDENROD = self.RGB(218, 165, 32).hex_format()
        GOLDENROD1 = self.RGB(255, 193, 37).hex_format()
        GOLDENROD2 = self.RGB(238, 180, 34).hex_format()
        GOLDENROD3 = self.RGB(205, 155, 29).hex_format()
        GOLDENROD4 = self.RGB(139, 105, 20).hex_format()
        GRAY = self.RGB(128, 128, 128).hex_format()
        GRAY1 = self.RGB(3, 3, 3).hex_format()
        GRAY10 = self.RGB(26, 26, 26).hex_format()
        GRAY11 = self.RGB(28, 28, 28).hex_format()
        GRAY12 = self.RGB(31, 31, 31).hex_format()
        GRAY13 = self.RGB(33, 33, 33).hex_format()
        GRAY14 = self.RGB(36, 36, 36).hex_format()
        GRAY15 = self.RGB(38, 38, 38).hex_format()
        GRAY16 = self.RGB(41, 41, 41).hex_format()
        GRAY17 = self.RGB(43, 43, 43).hex_format()
        GRAY18 = self.RGB(46, 46, 46).hex_format()
        GRAY19 = self.RGB(48, 48, 48).hex_format()
        GRAY2 = self.RGB(5, 5, 5).hex_format()
        GRAY20 = self.RGB(51, 51, 51).hex_format()
        GRAY21 = self.RGB(54, 54, 54).hex_format()
        GRAY22 = self.RGB(56, 56, 56).hex_format()
        GRAY23 = self.RGB(59, 59, 59).hex_format()
        GRAY24 = self.RGB(61, 61, 61).hex_format()
        GRAY25 = self.RGB(64, 64, 64).hex_format()
        GRAY26 = self.RGB(66, 66, 66).hex_format()
        GRAY27 = self.RGB(69, 69, 69).hex_format()
        GRAY28 = self.RGB(71, 71, 71).hex_format()
        GRAY29 = self.RGB(74, 74, 74).hex_format()
        GRAY3 = self.RGB(8, 8, 8).hex_format()
        GRAY30 = self.RGB(77, 77, 77).hex_format()
        GRAY31 = self.RGB(79, 79, 79).hex_format()
        GRAY32 = self.RGB(82, 82, 82).hex_format()
        GRAY33 = self.RGB(84, 84, 84).hex_format()
        GRAY34 = self.RGB(87, 87, 87).hex_format()
        GRAY35 = self.RGB(89, 89, 89).hex_format()
        GRAY36 = self.RGB(92, 92, 92).hex_format()
        GRAY37 = self.RGB(94, 94, 94).hex_format()
        GRAY38 = self.RGB(97, 97, 97).hex_format()
        GRAY39 = self.RGB(99, 99, 99).hex_format()
        GRAY4 = self.RGB(10, 10, 10).hex_format()
        GRAY40 = self.RGB(102, 102, 102).hex_format()
        GRAY42 = self.RGB(107, 107, 107).hex_format()
        GRAY43 = self.RGB(110, 110, 110).hex_format()
        GRAY44 = self.RGB(112, 112, 112).hex_format()
        GRAY45 = self.RGB(115, 115, 115).hex_format()
        GRAY46 = self.RGB(117, 117, 117).hex_format()
        GRAY47 = self.RGB(120, 120, 120).hex_format()
        GRAY48 = self.RGB(122, 122, 122).hex_format()
        GRAY49 = self.RGB(125, 125, 125).hex_format()
        GRAY5 = self.RGB(13, 13, 13).hex_format()
        GRAY50 = self.RGB(127, 127, 127).hex_format()
        GRAY51 = self.RGB(130, 130, 130).hex_format()
        GRAY52 = self.RGB(133, 133, 133).hex_format()
        GRAY53 = self.RGB(135, 135, 135).hex_format()
        GRAY54 = self.RGB(138, 138, 138).hex_format()
        GRAY55 = self.RGB(140, 140, 140).hex_format()
        GRAY56 = self.RGB(143, 143, 143).hex_format()
        GRAY57 = self.RGB(145, 145, 145).hex_format()
        GRAY58 = self.RGB(148, 148, 148).hex_format()
        GRAY59 = self.RGB(150, 150, 150).hex_format()
        GRAY6 = self.RGB(15, 15, 15).hex_format()
        GRAY60 = self.RGB(153, 153, 153).hex_format()
        GRAY61 = self.RGB(156, 156, 156).hex_format()
        GRAY62 = self.RGB(158, 158, 158).hex_format()
        GRAY63 = self.RGB(161, 161, 161).hex_format()
        GRAY64 = self.RGB(163, 163, 163).hex_format()
        GRAY65 = self.RGB(166, 166, 166).hex_format()
        GRAY66 = self.RGB(168, 168, 168).hex_format()
        GRAY67 = self.RGB(171, 171, 171).hex_format()
        GRAY68 = self.RGB(173, 173, 173).hex_format()
        GRAY69 = self.RGB(176, 176, 176).hex_format()
        GRAY7 = self.RGB(18, 18, 18).hex_format()
        GRAY70 = self.RGB(179, 179, 179).hex_format()
        GRAY71 = self.RGB(181, 181, 181).hex_format()
        GRAY72 = self.RGB(184, 184, 184).hex_format()
        GRAY73 = self.RGB(186, 186, 186).hex_format()
        GRAY74 = self.RGB(189, 189, 189).hex_format()
        GRAY75 = self.RGB(191, 191, 191).hex_format()
        GRAY76 = self.RGB(194, 194, 194).hex_format()
        GRAY77 = self.RGB(196, 196, 196).hex_format()
        GRAY78 = self.RGB(199, 199, 199).hex_format()
        GRAY79 = self.RGB(201, 201, 201).hex_format()
        GRAY8 = self.RGB(20, 20, 20).hex_format()
        GRAY80 = self.RGB(204, 204, 204).hex_format()
        GRAY81 = self.RGB(207, 207, 207).hex_format()
        GRAY82 = self.RGB(209, 209, 209).hex_format()
        GRAY83 = self.RGB(212, 212, 212).hex_format()
        GRAY84 = self.RGB(214, 214, 214).hex_format()
        GRAY85 = self.RGB(217, 217, 217).hex_format()
        GRAY86 = self.RGB(219, 219, 219).hex_format()
        GRAY87 = self.RGB(222, 222, 222).hex_format()
        GRAY88 = self.RGB(224, 224, 224).hex_format()
        GRAY89 = self.RGB(227, 227, 227).hex_format()
        GRAY9 = self.RGB(23, 23, 23).hex_format()
        GRAY90 = self.RGB(229, 229, 229).hex_format()
        GRAY91 = self.RGB(232, 232, 232).hex_format()
        GRAY92 = self.RGB(235, 235, 235).hex_format()
        GRAY93 = self.RGB(237, 237, 237).hex_format()
        GRAY94 = self.RGB(240, 240, 240).hex_format()
        GRAY95 = self.RGB(242, 242, 242).hex_format()
        GRAY97 = self.RGB(247, 247, 247).hex_format()
        GRAY98 = self.RGB(250, 250, 250).hex_format()
        GRAY99 = self.RGB(252, 252, 252).hex_format()
        GREEN = self.RGB(0, 128, 0).hex_format()
        GREEN1 = self.RGB(0, 255, 0).hex_format()
        GREEN2 = self.RGB(0, 238, 0).hex_format()
        GREEN3 = self.RGB(0, 205, 0).hex_format()
        GREEN4 = self.RGB(0, 139, 0).hex_format()
        GREENYELLOW = self.RGB(173, 255, 47).hex_format()
        HONEYDEW1 = self.RGB(240, 255, 240).hex_format()
        HONEYDEW2 = self.RGB(224, 238, 224).hex_format()
        HONEYDEW3 = self.RGB(193, 205, 193).hex_format()
        HONEYDEW4 = self.RGB(131, 139, 131).hex_format()
        HOTPINK = self.RGB(255, 105, 180).hex_format()
        HOTPINK1 = self.RGB(255, 110, 180).hex_format()
        HOTPINK2 = self.RGB(238, 106, 167).hex_format()
        HOTPINK3 = self.RGB(205, 96, 144).hex_format()
        HOTPINK4 = self.RGB(139, 58, 98).hex_format()
        INDIANRED = self.RGB(176, 23, 31).hex_format()
        INDIANRED = self.RGB(205, 92, 92).hex_format()
        INDIANRED1 = self.RGB(255, 106, 106).hex_format()
        INDIANRED2 = self.RGB(238, 99, 99).hex_format()
        INDIANRED3 = self.RGB(205, 85, 85).hex_format()
        INDIANRED4 = self.RGB(139, 58, 58).hex_format()
        INDIGO = self.RGB(75, 0, 130).hex_format()
        IVORY1 = self.RGB(255, 255, 240).hex_format()
        IVORY2 = self.RGB(238, 238, 224).hex_format()
        IVORY3 = self.RGB(205, 205, 193).hex_format()
        IVORY4 = self.RGB(139, 139, 131).hex_format()
        IVORYBLACK = self.RGB(41, 36, 33).hex_format()
        KHAKI = self.RGB(240, 230, 140).hex_format()
        KHAKI1 = self.RGB(255, 246, 143).hex_format()
        KHAKI2 = self.RGB(238, 230, 133).hex_format()
        KHAKI3 = self.RGB(205, 198, 115).hex_format()
        KHAKI4 = self.RGB(139, 134, 78).hex_format()
        LAVENDER = self.RGB(230, 230, 250).hex_format()
        LAVENDERBLUSH1 = self.RGB(255, 240, 245).hex_format()
        LAVENDERBLUSH2 = self.RGB(238, 224, 229).hex_format()
        LAVENDERBLUSH3 = self.RGB(205, 193, 197).hex_format()
        LAVENDERBLUSH4 = self.RGB(139, 131, 134).hex_format()
        LAWNGREEN = self.RGB(124, 252, 0).hex_format()
        LEMONCHIFFON1 = self.RGB(255, 250, 205).hex_format()
        LEMONCHIFFON2 = self.RGB(238, 233, 191).hex_format()
        LEMONCHIFFON3 = self.RGB(205, 201, 165).hex_format()
        LEMONCHIFFON4 = self.RGB(139, 137, 112).hex_format()
        LIGHTBLUE = self.RGB(173, 216, 230).hex_format()
        LIGHTBLUE1 = self.RGB(191, 239, 255).hex_format()
        LIGHTBLUE2 = self.RGB(178, 223, 238).hex_format()
        LIGHTBLUE3 = self.RGB(154, 192, 205).hex_format()
        LIGHTBLUE4 = self.RGB(104, 131, 139).hex_format()
        LIGHTCORAL = self.RGB(240, 128, 128).hex_format()
        LIGHTCYAN1 = self.RGB(224, 255, 255).hex_format()
        LIGHTCYAN2 = self.RGB(209, 238, 238).hex_format()
        LIGHTCYAN3 = self.RGB(180, 205, 205).hex_format()
        LIGHTCYAN4 = self.RGB(122, 139, 139).hex_format()
        LIGHTGOLDENROD1 = self.RGB(255, 236, 139).hex_format()
        LIGHTGOLDENROD2 = self.RGB(238, 220, 130).hex_format()
        LIGHTGOLDENROD3 = self.RGB(205, 190, 112).hex_format()
        LIGHTGOLDENROD4 = self.RGB(139, 129, 76).hex_format()
        LIGHTGOLDENRODYELLOW = self.RGB(250, 250, 210).hex_format()
        LIGHTGREY = self.RGB(211, 211, 211).hex_format()
        LIGHTPINK = self.RGB(255, 182, 193).hex_format()
        LIGHTPINK1 = self.RGB(255, 174, 185).hex_format()
        LIGHTPINK2 = self.RGB(238, 162, 173).hex_format()
        LIGHTPINK3 = self.RGB(205, 140, 149).hex_format()
        LIGHTPINK4 = self.RGB(139, 95, 101).hex_format()
        LIGHTSALMON1 = self.RGB(255, 160, 122).hex_format()
        LIGHTSALMON2 = self.RGB(238, 149, 114).hex_format()
        LIGHTSALMON3 = self.RGB(205, 129, 98).hex_format()
        LIGHTSALMON4 = self.RGB(139, 87, 66).hex_format()
        LIGHTSEAGREEN = self.RGB(32, 178, 170).hex_format()
        LIGHTSKYBLUE = self.RGB(135, 206, 250).hex_format()
        LIGHTSKYBLUE1 = self.RGB(176, 226, 255).hex_format()
        LIGHTSKYBLUE2 = self.RGB(164, 211, 238).hex_format()
        LIGHTSKYBLUE3 = self.RGB(141, 182, 205).hex_format()
        LIGHTSKYBLUE4 = self.RGB(96, 123, 139).hex_format()
        LIGHTSLATEBLUE = self.RGB(132, 112, 255).hex_format()
        LIGHTSLATEGRAY = self.RGB(119, 136, 153).hex_format()
        LIGHTSTEELBLUE = self.RGB(176, 196, 222).hex_format()
        LIGHTSTEELBLUE1 = self.RGB(202, 225, 255).hex_format()
        LIGHTSTEELBLUE2 = self.RGB(188, 210, 238).hex_format()
        LIGHTSTEELBLUE3 = self.RGB(162, 181, 205).hex_format()
        LIGHTSTEELBLUE4 = self.RGB(110, 123, 139).hex_format()
        LIGHTYELLOW1 = self.RGB(255, 255, 224).hex_format()
        LIGHTYELLOW2 = self.RGB(238, 238, 209).hex_format()
        LIGHTYELLOW3 = self.RGB(205, 205, 180).hex_format()
        LIGHTYELLOW4 = self.RGB(139, 139, 122).hex_format()
        LIMEGREEN = self.RGB(50, 205, 50).hex_format()
        LINEN = self.RGB(250, 240, 230).hex_format()
        MAGENTA = self.RGB(255, 0, 255).hex_format()
        MAGENTA2 = self.RGB(238, 0, 238).hex_format()
        MAGENTA3 = self.RGB(205, 0, 205).hex_format()
        MAGENTA4 = self.RGB(139, 0, 139).hex_format()
        MANGANESEBLUE = self.RGB(3, 168, 158).hex_format()
        MAROON = self.RGB(128, 0, 0).hex_format()
        MAROON1 = self.RGB(255, 52, 179).hex_format()
        MAROON2 = self.RGB(238, 48, 167).hex_format()
        MAROON3 = self.RGB(205, 41, 144).hex_format()
        MAROON4 = self.RGB(139, 28, 98).hex_format()
        MEDIUMORCHID = self.RGB(186, 85, 211).hex_format()
        MEDIUMORCHID1 = self.RGB(224, 102, 255).hex_format()
        MEDIUMORCHID2 = self.RGB(209, 95, 238).hex_format()
        MEDIUMORCHID3 = self.RGB(180, 82, 205).hex_format()
        MEDIUMORCHID4 = self.RGB(122, 55, 139).hex_format()
        MEDIUMPURPLE = self.RGB(147, 112, 219).hex_format()
        MEDIUMPURPLE1 = self.RGB(171, 130, 255).hex_format()
        MEDIUMPURPLE2 = self.RGB(159, 121, 238).hex_format()
        MEDIUMPURPLE3 = self.RGB(137, 104, 205).hex_format()
        MEDIUMPURPLE4 = self.RGB(93, 71, 139).hex_format()
        MEDIUMSEAGREEN = self.RGB(60, 179, 113).hex_format()
        MEDIUMSLATEBLUE = self.RGB(123, 104, 238).hex_format()
        MEDIUMSPRINGGREEN = self.RGB(0, 250, 154).hex_format()
        MEDIUMTURQUOISE = self.RGB(72, 209, 204).hex_format()
        MEDIUMVIOLETRED = self.RGB(199, 21, 133).hex_format()
        MELON = self.RGB(227, 168, 105).hex_format()
        MIDNIGHTBLUE = self.RGB(25, 25, 112).hex_format()
        MINT = self.RGB(189, 252, 201).hex_format()
        MINTCREAM = self.RGB(245, 255, 250).hex_format()
        MISTYROSE1 = self.RGB(255, 228, 225).hex_format()
        MISTYROSE2 = self.RGB(238, 213, 210).hex_format()
        MISTYROSE3 = self.RGB(205, 183, 181).hex_format()
        MISTYROSE4 = self.RGB(139, 125, 123).hex_format()
        MOCCASIN = self.RGB(255, 228, 181).hex_format()
        NAVAJOWHITE1 = self.RGB(255, 222, 173).hex_format()
        NAVAJOWHITE2 = self.RGB(238, 207, 161).hex_format()
        NAVAJOWHITE3 = self.RGB(205, 179, 139).hex_format()
        NAVAJOWHITE4 = self.RGB(139, 121, 94).hex_format()
        NAVY = self.RGB(0, 0, 128).hex_format()
        OLDLACE = self.RGB(253, 245, 230).hex_format()
        OLIVE = self.RGB(128, 128, 0).hex_format()
        OLIVEDRAB = self.RGB(107, 142, 35).hex_format()
        OLIVEDRAB1 = self.RGB(192, 255, 62).hex_format()
        OLIVEDRAB2 = self.RGB(179, 238, 58).hex_format()
        OLIVEDRAB3 = self.RGB(154, 205, 50).hex_format()
        OLIVEDRAB4 = self.RGB(105, 139, 34).hex_format()
        ORANGE = self.RGB(255, 128, 0).hex_format()
        ORANGE1 = self.RGB(255, 165, 0).hex_format()
        ORANGE2 = self.RGB(238, 154, 0).hex_format()
        ORANGE3 = self.RGB(205, 133, 0).hex_format()
        ORANGE4 = self.RGB(139, 90, 0).hex_format()
        ORANGERED1 = self.RGB(255, 69, 0).hex_format()
        ORANGERED2 = self.RGB(238, 64, 0).hex_format()
        ORANGERED3 = self.RGB(205, 55, 0).hex_format()
        ORANGERED4 = self.RGB(139, 37, 0).hex_format()
        ORCHID = self.RGB(218, 112, 214).hex_format()
        ORCHID1 = self.RGB(255, 131, 250).hex_format()
        ORCHID2 = self.RGB(238, 122, 233).hex_format()
        ORCHID3 = self.RGB(205, 105, 201).hex_format()
        ORCHID4 = self.RGB(139, 71, 137).hex_format()
        PALEGOLDENROD = self.RGB(238, 232, 170).hex_format()
        PALEGREEN = self.RGB(152, 251, 152).hex_format()
        PALEGREEN1 = self.RGB(154, 255, 154).hex_format()
        PALEGREEN2 = self.RGB(144, 238, 144).hex_format()
        PALEGREEN3 = self.RGB(124, 205, 124).hex_format()
        PALEGREEN4 = self.RGB(84, 139, 84).hex_format()
        PALETURQUOISE1 = self.RGB(187, 255, 255).hex_format()
        PALETURQUOISE2 = self.RGB(174, 238, 238).hex_format()
        PALETURQUOISE3 = self.RGB(150, 205, 205).hex_format()
        PALETURQUOISE4 = self.RGB(102, 139, 139).hex_format()
        PALEVIOLETRED = self.RGB(219, 112, 147).hex_format()
        PALEVIOLETRED1 = self.RGB(255, 130, 171).hex_format()
        PALEVIOLETRED2 = self.RGB(238, 121, 159).hex_format()
        PALEVIOLETRED3 = self.RGB(205, 104, 137).hex_format()
        PALEVIOLETRED4 = self.RGB(139, 71, 93).hex_format()
        PAPAYAWHIP = self.RGB(255, 239, 213).hex_format()
        PEACHPUFF1 = self.RGB(255, 218, 185).hex_format()
        PEACHPUFF2 = self.RGB(238, 203, 173).hex_format()
        PEACHPUFF3 = self.RGB(205, 175, 149).hex_format()
        PEACHPUFF4 = self.RGB(139, 119, 101).hex_format()
        PEACOCK = self.RGB(51, 161, 201).hex_format()
        PINK = self.RGB(255, 192, 203).hex_format()
        PINK1 = self.RGB(255, 181, 197).hex_format()
        PINK2 = self.RGB(238, 169, 184).hex_format()
        PINK3 = self.RGB(205, 145, 158).hex_format()
        PINK4 = self.RGB(139, 99, 108).hex_format()
        PLUM = self.RGB(221, 160, 221).hex_format()
        PLUM1 = self.RGB(255, 187, 255).hex_format()
        PLUM2 = self.RGB(238, 174, 238).hex_format()
        PLUM3 = self.RGB(205, 150, 205).hex_format()
        PLUM4 = self.RGB(139, 102, 139).hex_format()
        POWDERBLUE = self.RGB(176, 224, 230).hex_format()
        PURPLE = self.RGB(128, 0, 128).hex_format()
        PURPLE1 = self.RGB(155, 48, 255).hex_format()
        PURPLE2 = self.RGB(145, 44, 238).hex_format()
        PURPLE3 = self.RGB(125, 38, 205).hex_format()
        PURPLE4 = self.RGB(85, 26, 139).hex_format()
        RASPBERRY = self.RGB(135, 38, 87).hex_format()
        RAWSIENNA = self.RGB(199, 97, 20).hex_format()
        RED1 = self.RGB(255, 0, 0).hex_format()
        RED2 = self.RGB(238, 0, 0).hex_format()
        RED3 = self.RGB(205, 0, 0).hex_format()
        RED4 = self.RGB(139, 0, 0).hex_format()
        ROSYBROWN = self.RGB(188, 143, 143).hex_format()
        ROSYBROWN1 = self.RGB(255, 193, 193).hex_format()
        ROSYBROWN2 = self.RGB(238, 180, 180).hex_format()
        ROSYBROWN3 = self.RGB(205, 155, 155).hex_format()
        ROSYBROWN4 = self.RGB(139, 105, 105).hex_format()
        ROYALBLUE = self.RGB(65, 105, 225).hex_format()
        ROYALBLUE1 = self.RGB(72, 118, 255).hex_format()
        ROYALBLUE2 = self.RGB(67, 110, 238).hex_format()
        ROYALBLUE3 = self.RGB(58, 95, 205).hex_format()
        ROYALBLUE4 = self.RGB(39, 64, 139).hex_format()
        SALMON = self.RGB(250, 128, 114).hex_format()
        SALMON1 = self.RGB(255, 140, 105).hex_format()
        SALMON2 = self.RGB(238, 130, 98).hex_format()
        SALMON3 = self.RGB(205, 112, 84).hex_format()
        SALMON4 = self.RGB(139, 76, 57).hex_format()
        SANDYBROWN = self.RGB(244, 164, 96).hex_format()
        SAPGREEN = self.RGB(48, 128, 20).hex_format()
        SEAGREEN1 = self.RGB(84, 255, 159).hex_format()
        SEAGREEN2 = self.RGB(78, 238, 148).hex_format()
        SEAGREEN3 = self.RGB(67, 205, 128).hex_format()
        SEAGREEN4 = self.RGB(46, 139, 87).hex_format()
        SEASHELL1 = self.RGB(255, 245, 238).hex_format()
        SEASHELL2 = self.RGB(238, 229, 222).hex_format()
        SEASHELL3 = self.RGB(205, 197, 191).hex_format()
        SEASHELL4 = self.RGB(139, 134, 130).hex_format()
        SEPIA = self.RGB(94, 38, 18).hex_format()
        SGIBEET = self.RGB(142, 56, 142).hex_format()
        SGIBRIGHTGRAY = self.RGB(197, 193, 170).hex_format()
        SGICHARTREUSE = self.RGB(113, 198, 113).hex_format()
        SGIDARKGRAY = self.RGB(85, 85, 85).hex_format()
        SGIGRAY12 = self.RGB(30, 30, 30).hex_format()
        SGIGRAY16 = self.RGB(40, 40, 40).hex_format()
        SGIGRAY32 = self.RGB(81, 81, 81).hex_format()
        SGIGRAY36 = self.RGB(91, 91, 91).hex_format()
        SGIGRAY52 = self.RGB(132, 132, 132).hex_format()
        SGIGRAY56 = self.RGB(142, 142, 142).hex_format()
        SGIGRAY72 = self.RGB(183, 183, 183).hex_format()
        SGIGRAY76 = self.RGB(193, 193, 193).hex_format()
        SGIGRAY92 = self.RGB(234, 234, 234).hex_format()
        SGIGRAY96 = self.RGB(244, 244, 244).hex_format()
        SGILIGHTBLUE = self.RGB(125, 158, 192).hex_format()
        SGILIGHTGRAY = self.RGB(170, 170, 170).hex_format()
        SGIOLIVEDRAB = self.RGB(142, 142, 56).hex_format()
        SGISALMON = self.RGB(198, 113, 113).hex_format()
        SGISLATEBLUE = self.RGB(113, 113, 198).hex_format()
        SGITEAL = self.RGB(56, 142, 142).hex_format()
        SIENNA = self.RGB(160, 82, 45).hex_format()
        SIENNA1 = self.RGB(255, 130, 71).hex_format()
        SIENNA2 = self.RGB(238, 121, 66).hex_format()
        SIENNA3 = self.RGB(205, 104, 57).hex_format()
        SIENNA4 = self.RGB(139, 71, 38).hex_format()
        SILVER = self.RGB(192, 192, 192).hex_format()
        SKYBLUE = self.RGB(135, 206, 235).hex_format()
        SKYBLUE1 = self.RGB(135, 206, 255).hex_format()
        SKYBLUE2 = self.RGB(126, 192, 238).hex_format()
        SKYBLUE3 = self.RGB(108, 166, 205).hex_format()
        SKYBLUE4 = self.RGB(74, 112, 139).hex_format()
        SLATEBLUE = self.RGB(106, 90, 205).hex_format()
        SLATEBLUE1 = self.RGB(131, 111, 255).hex_format()
        SLATEBLUE2 = self.RGB(122, 103, 238).hex_format()
        SLATEBLUE3 = self.RGB(105, 89, 205).hex_format()
        SLATEBLUE4 = self.RGB(71, 60, 139).hex_format()
        SLATEGRAY = self.RGB(112, 128, 144).hex_format()
        SLATEGRAY1 = self.RGB(198, 226, 255).hex_format()
        SLATEGRAY2 = self.RGB(185, 211, 238).hex_format()
        SLATEGRAY3 = self.RGB(159, 182, 205).hex_format()
        SLATEGRAY4 = self.RGB(108, 123, 139).hex_format()
        SNOW1 = self.RGB(255, 250, 250).hex_format()
        SNOW2 = self.RGB(238, 233, 233).hex_format()
        SNOW3 = self.RGB(205, 201, 201).hex_format()
        SNOW4 = self.RGB(139, 137, 137).hex_format()
        SPRINGGREEN = self.RGB(0, 255, 127).hex_format()
        SPRINGGREEN1 = self.RGB(0, 238, 118).hex_format()
        SPRINGGREEN2 = self.RGB(0, 205, 102).hex_format()
        SPRINGGREEN3 = self.RGB(0, 139, 69).hex_format()
        STEELBLUE = self.RGB(70, 130, 180).hex_format()
        STEELBLUE1 = self.RGB(99, 184, 255).hex_format()
        STEELBLUE2 = self.RGB(92, 172, 238).hex_format()
        STEELBLUE3 = self.RGB(79, 148, 205).hex_format()
        STEELBLUE4 = self.RGB(54, 100, 139).hex_format()
        TAN = self.RGB(210, 180, 140).hex_format()
        TAN1 = self.RGB(255, 165, 79).hex_format()
        TAN2 = self.RGB(238, 154, 73).hex_format()
        TAN3 = self.RGB(205, 133, 63).hex_format()
        TAN4 = self.RGB(139, 90, 43).hex_format()
        TEAL = self.RGB(0, 128, 128).hex_format()
        THISTLE = self.RGB(216, 191, 216).hex_format()
        THISTLE1 = self.RGB(255, 225, 255).hex_format()
        THISTLE2 = self.RGB(238, 210, 238).hex_format()
        THISTLE3 = self.RGB(205, 181, 205).hex_format()
        THISTLE4 = self.RGB(139, 123, 139).hex_format()
        TOMATO1 = self.RGB(255, 99, 71).hex_format()
        TOMATO2 = self.RGB(238, 92, 66).hex_format()
        TOMATO3 = self.RGB(205, 79, 57).hex_format()
        TOMATO4 = self.RGB(139, 54, 38).hex_format()
        TURQUOISE = self.RGB(64, 224, 208).hex_format()
        TURQUOISE1 = self.RGB(0, 245, 255).hex_format()
        TURQUOISE2 = self.RGB(0, 229, 238).hex_format()
        TURQUOISE3 = self.RGB(0, 197, 205).hex_format()
        TURQUOISE4 = self.RGB(0, 134, 139).hex_format()
        TURQUOISEBLUE = self.RGB(0, 199, 140).hex_format()
        VIOLET = self.RGB(238, 130, 238).hex_format()
        VIOLETRED = self.RGB(208, 32, 144).hex_format()
        VIOLETRED1 = self.RGB(255, 62, 150).hex_format()
        VIOLETRED2 = self.RGB(238, 58, 140).hex_format()
        VIOLETRED3 = self.RGB(205, 50, 120).hex_format()
        VIOLETRED4 = self.RGB(139, 34, 82).hex_format()
        WARMGREY = self.RGB(128, 128, 105).hex_format()
        WHEAT = self.RGB(245, 222, 179).hex_format()
        WHEAT1 = self.RGB(255, 231, 186).hex_format()
        WHEAT2 = self.RGB(238, 216, 174).hex_format()
        WHEAT3 = self.RGB(205, 186, 150).hex_format()
        WHEAT4 = self.RGB(139, 126, 102).hex_format()
        WHITE = self.RGB(255, 255, 255).hex_format()
        WHITESMOKE = self.RGB(245, 245, 245).hex_format()
        WHITESMOKE = self.RGB(245, 245, 245).hex_format()
        YELLOW1 = self.RGB(255, 255, 0).hex_format()
        YELLOW2 = self.RGB(238, 238, 0).hex_format()
        YELLOW3 = self.RGB(205, 205, 0).hex_format()
        YELLOW4 = self.RGB(139, 139, 0).hex_format()

        dict_containing_variables = locals()
        del dict_containing_variables['self']

        return dict_containing_variables # <= NOTE Return a dictionary containing the current scope's local variables.

    def colors_rgb(self) -> dict: # DESC => Color RGB contants
        """ Return a dictionary of color variables in RGB format.
        
        Returns:
            dict{str: tuple}: A dictionary containing color variables in RGB format.

        Example:
        ```python
            colors = ColorsConstants()
            rgb_colors = colors.colors_rgb()
            print(rgb_colors)  # Output: {'ALICEBLUE': (240, 248, 255), ...}
        ```
        """
        ALICEBLUE = self.RGB(240, 248, 255).rgb_format()
        ANTIQUEWHITE = self.RGB(250, 235, 215).rgb_format()
        ANTIQUEWHITE1 = self.RGB(255, 239, 219).rgb_format()
        ANTIQUEWHITE2 = self.RGB(238, 223, 204).rgb_format()
        ANTIQUEWHITE3 = self.RGB(205, 192, 176).rgb_format()
        ANTIQUEWHITE4 = self.RGB(139, 131, 120).rgb_format()
        AQUA = self.RGB(0, 255, 255).rgb_format()
        AQUAMARINE1 = self.RGB(127, 255, 212).rgb_format()
        AQUAMARINE2 = self.RGB(118, 238, 198).rgb_format()
        AQUAMARINE3 = self.RGB(102, 205, 170).rgb_format()
        AQUAMARINE4 = self.RGB(69, 139, 116).rgb_format()
        AZURE1 = self.RGB(240, 255, 255).rgb_format()
        AZURE2 = self.RGB(224, 238, 238).rgb_format()
        AZURE3 = self.RGB(193, 205, 205).rgb_format()
        AZURE4 = self.RGB(131, 139, 139).rgb_format()
        BANANA = self.RGB(227, 207, 87).rgb_format()
        BEIGE = self.RGB(245, 245, 220).rgb_format()
        BISQUE1 = self.RGB(255, 228, 196).rgb_format()
        BISQUE2 = self.RGB(238, 213, 183).rgb_format()
        BISQUE3 = self.RGB(205, 183, 158).rgb_format()
        BISQUE4 = self.RGB(139, 125, 107).rgb_format()
        BLACK = self.RGB(0, 0, 0).rgb_format()
        BLANCHEDALMOND = self.RGB(255, 235, 205).rgb_format()
        BLUE = self.RGB(0, 0, 255).rgb_format()
        BLUE2 = self.RGB(0, 0, 238).rgb_format()
        BLUE3 = self.RGB(0, 0, 205).rgb_format()
        BLUE4 = self.RGB(0, 0, 139).rgb_format()
        BLUEVIOLET = self.RGB(138, 43, 226).rgb_format()
        BRICK = self.RGB(156, 102, 31).rgb_format()
        BROWN = self.RGB(165, 42, 42).rgb_format()
        BROWN1 = self.RGB(255, 64, 64).rgb_format()
        BROWN2 = self.RGB(238, 59, 59).rgb_format()
        BROWN3 = self.RGB(205, 51, 51).rgb_format()
        BROWN4 = self.RGB(139, 35, 35).rgb_format()
        BURLYWOOD = self.RGB(222, 184, 135).rgb_format()
        BURLYWOOD1 = self.RGB(255, 211, 155).rgb_format()
        BURLYWOOD2 = self.RGB(238, 197, 145).rgb_format()
        BURLYWOOD3 = self.RGB(205, 170, 125).rgb_format()
        BURLYWOOD4 = self.RGB(139, 115, 85).rgb_format()
        BURNTSIENNA = self.RGB(138, 54, 15).rgb_format()
        BURNTUMBER = self.RGB(138, 51, 36).rgb_format()
        CADETBLUE = self.RGB(95, 158, 160).rgb_format()
        CADETBLUE1 = self.RGB(152, 245, 255).rgb_format()
        CADETBLUE2 = self.RGB(142, 229, 238).rgb_format()
        CADETBLUE3 = self.RGB(122, 197, 205).rgb_format()
        CADETBLUE4 = self.RGB(83, 134, 139).rgb_format()
        CADMIUMORANGE = self.RGB(255, 97, 3).rgb_format()
        CADMIUMYELLOW = self.RGB(255, 153, 18).rgb_format()
        CARROT = self.RGB(237, 145, 33).rgb_format()
        CHARTREUSE1 = self.RGB(127, 255, 0).rgb_format()
        CHARTREUSE2 = self.RGB(118, 238, 0).rgb_format()
        CHARTREUSE3 = self.RGB(102, 205, 0).rgb_format()
        CHARTREUSE4 = self.RGB(69, 139, 0).rgb_format()
        CHOCOLATE = self.RGB(210, 105, 30).rgb_format()
        CHOCOLATE1 = self.RGB(255, 127, 36).rgb_format()
        CHOCOLATE2 = self.RGB(238, 118, 33).rgb_format()
        CHOCOLATE3 = self.RGB(205, 102, 29).rgb_format()
        CHOCOLATE4 = self.RGB(139, 69, 19).rgb_format()
        COBALT = self.RGB(61, 89, 171).rgb_format()
        COBALTGREEN = self.RGB(61, 145, 64).rgb_format()
        COLDGREY = self.RGB(128, 138, 135).rgb_format()
        CORAL = self.RGB(255, 127, 80).rgb_format()
        CORAL1 = self.RGB(255, 114, 86).rgb_format()
        CORAL2 = self.RGB(238, 106, 80).rgb_format()
        CORAL3 = self.RGB(205, 91, 69).rgb_format()
        CORAL4 = self.RGB(139, 62, 47).rgb_format()
        CORNFLOWERBLUE = self.RGB(100, 149, 237).rgb_format()
        CORNSILK1 = self.RGB(255, 248, 220).rgb_format()
        CORNSILK2 = self.RGB(238, 232, 205).rgb_format()
        CORNSILK3 = self.RGB(205, 200, 177).rgb_format()
        CORNSILK4 = self.RGB(139, 136, 120).rgb_format()
        CRIMSON = self.RGB(220, 20, 60).rgb_format()
        CYAN2 = self.RGB(0, 238, 238).rgb_format()
        CYAN3 = self.RGB(0, 205, 205).rgb_format()
        CYAN4 = self.RGB(0, 139, 139).rgb_format()
        DARKGOLDENROD = self.RGB(184, 134, 11).rgb_format()
        DARKGOLDENROD1 = self.RGB(255, 185, 15).rgb_format()
        DARKGOLDENROD2 = self.RGB(238, 173, 14).rgb_format()
        DARKGOLDENROD3 = self.RGB(205, 149, 12).rgb_format()
        DARKGOLDENROD4 = self.RGB(139, 101, 8).rgb_format()
        DARKGRAY = self.RGB(169, 169, 169).rgb_format()
        DARKGREEN = self.RGB(0, 100, 0).rgb_format()
        DARKKHAKI = self.RGB(189, 183, 107).rgb_format()
        DARKOLIVEGREEN = self.RGB(85, 107, 47).rgb_format()
        DARKOLIVEGREEN1 = self.RGB(202, 255, 112).rgb_format()
        DARKOLIVEGREEN2 = self.RGB(188, 238, 104).rgb_format()
        DARKOLIVEGREEN3 = self.RGB(162, 205, 90).rgb_format()
        DARKOLIVEGREEN4 = self.RGB(110, 139, 61).rgb_format()
        DARKORANGE = self.RGB(255, 140, 0).rgb_format()
        DARKORANGE1 = self.RGB(255, 127, 0).rgb_format()
        DARKORANGE2 = self.RGB(238, 118, 0).rgb_format()
        DARKORANGE3 = self.RGB(205, 102, 0).rgb_format()
        DARKORANGE4 = self.RGB(139, 69, 0).rgb_format()
        DARKORCHID = self.RGB(153, 50, 204).rgb_format()
        DARKORCHID1 = self.RGB(191, 62, 255).rgb_format()
        DARKORCHID2 = self.RGB(178, 58, 238).rgb_format()
        DARKORCHID3 = self.RGB(154, 50, 205).rgb_format()
        DARKORCHID4 = self.RGB(104, 34, 139).rgb_format()
        DARKSALMON = self.RGB(233, 150, 122).rgb_format()
        DARKSEAGREEN = self.RGB(143, 188, 143).rgb_format()
        DARKSEAGREEN1 = self.RGB(193, 255, 193).rgb_format()
        DARKSEAGREEN2 = self.RGB(180, 238, 180).rgb_format()
        DARKSEAGREEN3 = self.RGB(155, 205, 155).rgb_format()
        DARKSEAGREEN4 = self.RGB(105, 139, 105).rgb_format()
        DARKSLATEBLUE = self.RGB(72, 61, 139).rgb_format()
        DARKSLATEGRAY = self.RGB(47, 79, 79).rgb_format()
        DARKSLATEGRAY1 = self.RGB(151, 255, 255).rgb_format()
        DARKSLATEGRAY2 = self.RGB(141, 238, 238).rgb_format()
        DARKSLATEGRAY3 = self.RGB(121, 205, 205).rgb_format()
        DARKSLATEGRAY4 = self.RGB(82, 139, 139).rgb_format()
        DARKTURQUOISE = self.RGB(0, 206, 209).rgb_format()
        DARKVIOLET = self.RGB(148, 0, 211).rgb_format()
        DEEPPINK1 = self.RGB(255, 20, 147).rgb_format()
        DEEPPINK2 = self.RGB(238, 18, 137).rgb_format()
        DEEPPINK3 = self.RGB(205, 16, 118).rgb_format()
        DEEPPINK4 = self.RGB(139, 10, 80).rgb_format()
        DEEPSKYBLUE1 = self.RGB(0, 191, 255).rgb_format()
        DEEPSKYBLUE2 = self.RGB(0, 178, 238).rgb_format()
        DEEPSKYBLUE3 = self.RGB(0, 154, 205).rgb_format()
        DEEPSKYBLUE4 = self.RGB(0, 104, 139).rgb_format()
        DIMGRAY = self.RGB(105, 105, 105).rgb_format()
        DIMGRAY = self.RGB(105, 105, 105).rgb_format()
        DODGERBLUE1 = self.RGB(30, 144, 255).rgb_format()
        DODGERBLUE2 = self.RGB(28, 134, 238).rgb_format()
        DODGERBLUE3 = self.RGB(24, 116, 205).rgb_format()
        DODGERBLUE4 = self.RGB(16, 78, 139).rgb_format()
        EGGSHELL = self.RGB(252, 230, 201).rgb_format()
        EMERALDGREEN = self.RGB(0, 201, 87).rgb_format()
        FIREBRICK = self.RGB(178, 34, 34).rgb_format()
        FIREBRICK1 = self.RGB(255, 48, 48).rgb_format()
        FIREBRICK2 = self.RGB(238, 44, 44).rgb_format()
        FIREBRICK3 = self.RGB(205, 38, 38).rgb_format()
        FIREBRICK4 = self.RGB(139, 26, 26).rgb_format()
        FLESH = self.RGB(255, 125, 64).rgb_format()
        FLORALWHITE = self.RGB(255, 250, 240).rgb_format()
        FORESTGREEN = self.RGB(34, 139, 34).rgb_format()
        GAINSBORO = self.RGB(220, 220, 220).rgb_format()
        GHOSTWHITE = self.RGB(248, 248, 255).rgb_format()
        GOLD1 = self.RGB(255, 215, 0).rgb_format()
        GOLD2 = self.RGB(238, 201, 0).rgb_format()
        GOLD3 = self.RGB(205, 173, 0).rgb_format()
        GOLD4 = self.RGB(139, 117, 0).rgb_format()
        GOLDENROD = self.RGB(218, 165, 32).rgb_format()
        GOLDENROD1 = self.RGB(255, 193, 37).rgb_format()
        GOLDENROD2 = self.RGB(238, 180, 34).rgb_format()
        GOLDENROD3 = self.RGB(205, 155, 29).rgb_format()
        GOLDENROD4 = self.RGB(139, 105, 20).rgb_format()
        GRAY = self.RGB(128, 128, 128).rgb_format()
        GRAY1 = self.RGB(3, 3, 3).rgb_format()
        GRAY10 = self.RGB(26, 26, 26).rgb_format()
        GRAY11 = self.RGB(28, 28, 28).rgb_format()
        GRAY12 = self.RGB(31, 31, 31).rgb_format()
        GRAY13 = self.RGB(33, 33, 33).rgb_format()
        GRAY14 = self.RGB(36, 36, 36).rgb_format()
        GRAY15 = self.RGB(38, 38, 38).rgb_format()
        GRAY16 = self.RGB(41, 41, 41).rgb_format()
        GRAY17 = self.RGB(43, 43, 43).rgb_format()
        GRAY18 = self.RGB(46, 46, 46).rgb_format()
        GRAY19 = self.RGB(48, 48, 48).rgb_format()
        GRAY2 = self.RGB(5, 5, 5).rgb_format()
        GRAY20 = self.RGB(51, 51, 51).rgb_format()
        GRAY21 = self.RGB(54, 54, 54).rgb_format()
        GRAY22 = self.RGB(56, 56, 56).rgb_format()
        GRAY23 = self.RGB(59, 59, 59).rgb_format()
        GRAY24 = self.RGB(61, 61, 61).rgb_format()
        GRAY25 = self.RGB(64, 64, 64).rgb_format()
        GRAY26 = self.RGB(66, 66, 66).rgb_format()
        GRAY27 = self.RGB(69, 69, 69).rgb_format()
        GRAY28 = self.RGB(71, 71, 71).rgb_format()
        GRAY29 = self.RGB(74, 74, 74).rgb_format()
        GRAY3 = self.RGB(8, 8, 8).rgb_format()
        GRAY30 = self.RGB(77, 77, 77).rgb_format()
        GRAY31 = self.RGB(79, 79, 79).rgb_format()
        GRAY32 = self.RGB(82, 82, 82).rgb_format()
        GRAY33 = self.RGB(84, 84, 84).rgb_format()
        GRAY34 = self.RGB(87, 87, 87).rgb_format()
        GRAY35 = self.RGB(89, 89, 89).rgb_format()
        GRAY36 = self.RGB(92, 92, 92).rgb_format()
        GRAY37 = self.RGB(94, 94, 94).rgb_format()
        GRAY38 = self.RGB(97, 97, 97).rgb_format()
        GRAY39 = self.RGB(99, 99, 99).rgb_format()
        GRAY4 = self.RGB(10, 10, 10).rgb_format()
        GRAY40 = self.RGB(102, 102, 102).rgb_format()
        GRAY42 = self.RGB(107, 107, 107).rgb_format()
        GRAY43 = self.RGB(110, 110, 110).rgb_format()
        GRAY44 = self.RGB(112, 112, 112).rgb_format()
        GRAY45 = self.RGB(115, 115, 115).rgb_format()
        GRAY46 = self.RGB(117, 117, 117).rgb_format()
        GRAY47 = self.RGB(120, 120, 120).rgb_format()
        GRAY48 = self.RGB(122, 122, 122).rgb_format()
        GRAY49 = self.RGB(125, 125, 125).rgb_format()
        GRAY5 = self.RGB(13, 13, 13).rgb_format()
        GRAY50 = self.RGB(127, 127, 127).rgb_format()
        GRAY51 = self.RGB(130, 130, 130).rgb_format()
        GRAY52 = self.RGB(133, 133, 133).rgb_format()
        GRAY53 = self.RGB(135, 135, 135).rgb_format()
        GRAY54 = self.RGB(138, 138, 138).rgb_format()
        GRAY55 = self.RGB(140, 140, 140).rgb_format()
        GRAY56 = self.RGB(143, 143, 143).rgb_format()
        GRAY57 = self.RGB(145, 145, 145).rgb_format()
        GRAY58 = self.RGB(148, 148, 148).rgb_format()
        GRAY59 = self.RGB(150, 150, 150).rgb_format()
        GRAY6 = self.RGB(15, 15, 15).rgb_format()
        GRAY60 = self.RGB(153, 153, 153).rgb_format()
        GRAY61 = self.RGB(156, 156, 156).rgb_format()
        GRAY62 = self.RGB(158, 158, 158).rgb_format()
        GRAY63 = self.RGB(161, 161, 161).rgb_format()
        GRAY64 = self.RGB(163, 163, 163).rgb_format()
        GRAY65 = self.RGB(166, 166, 166).rgb_format()
        GRAY66 = self.RGB(168, 168, 168).rgb_format()
        GRAY67 = self.RGB(171, 171, 171).rgb_format()
        GRAY68 = self.RGB(173, 173, 173).rgb_format()
        GRAY69 = self.RGB(176, 176, 176).rgb_format()
        GRAY7 = self.RGB(18, 18, 18).rgb_format()
        GRAY70 = self.RGB(179, 179, 179).rgb_format()
        GRAY71 = self.RGB(181, 181, 181).rgb_format()
        GRAY72 = self.RGB(184, 184, 184).rgb_format()
        GRAY73 = self.RGB(186, 186, 186).rgb_format()
        GRAY74 = self.RGB(189, 189, 189).rgb_format()
        GRAY75 = self.RGB(191, 191, 191).rgb_format()
        GRAY76 = self.RGB(194, 194, 194).rgb_format()
        GRAY77 = self.RGB(196, 196, 196).rgb_format()
        GRAY78 = self.RGB(199, 199, 199).rgb_format()
        GRAY79 = self.RGB(201, 201, 201).rgb_format()
        GRAY8 = self.RGB(20, 20, 20).rgb_format()
        GRAY80 = self.RGB(204, 204, 204).rgb_format()
        GRAY81 = self.RGB(207, 207, 207).rgb_format()
        GRAY82 = self.RGB(209, 209, 209).rgb_format()
        GRAY83 = self.RGB(212, 212, 212).rgb_format()
        GRAY84 = self.RGB(214, 214, 214).rgb_format()
        GRAY85 = self.RGB(217, 217, 217).rgb_format()
        GRAY86 = self.RGB(219, 219, 219).rgb_format()
        GRAY87 = self.RGB(222, 222, 222).rgb_format()
        GRAY88 = self.RGB(224, 224, 224).rgb_format()
        GRAY89 = self.RGB(227, 227, 227).rgb_format()
        GRAY9 = self.RGB(23, 23, 23).rgb_format()
        GRAY90 = self.RGB(229, 229, 229).rgb_format()
        GRAY91 = self.RGB(232, 232, 232).rgb_format()
        GRAY92 = self.RGB(235, 235, 235).rgb_format()
        GRAY93 = self.RGB(237, 237, 237).rgb_format()
        GRAY94 = self.RGB(240, 240, 240).rgb_format()
        GRAY95 = self.RGB(242, 242, 242).rgb_format()
        GRAY97 = self.RGB(247, 247, 247).rgb_format()
        GRAY98 = self.RGB(250, 250, 250).rgb_format()
        GRAY99 = self.RGB(252, 252, 252).rgb_format()
        GREEN = self.RGB(0, 128, 0).rgb_format()
        GREEN1 = self.RGB(0, 255, 0).rgb_format()
        GREEN2 = self.RGB(0, 238, 0).rgb_format()
        GREEN3 = self.RGB(0, 205, 0).rgb_format()
        GREEN4 = self.RGB(0, 139, 0).rgb_format()
        GREENYELLOW = self.RGB(173, 255, 47).rgb_format()
        HONEYDEW1 = self.RGB(240, 255, 240).rgb_format()
        HONEYDEW2 = self.RGB(224, 238, 224).rgb_format()
        HONEYDEW3 = self.RGB(193, 205, 193).rgb_format()
        HONEYDEW4 = self.RGB(131, 139, 131).rgb_format()
        HOTPINK = self.RGB(255, 105, 180).rgb_format()
        HOTPINK1 = self.RGB(255, 110, 180).rgb_format()
        HOTPINK2 = self.RGB(238, 106, 167).rgb_format()
        HOTPINK3 = self.RGB(205, 96, 144).rgb_format()
        HOTPINK4 = self.RGB(139, 58, 98).rgb_format()
        INDIANRED = self.RGB(176, 23, 31).rgb_format()
        INDIANRED = self.RGB(205, 92, 92).rgb_format()
        INDIANRED1 = self.RGB(255, 106, 106).rgb_format()
        INDIANRED2 = self.RGB(238, 99, 99).rgb_format()
        INDIANRED3 = self.RGB(205, 85, 85).rgb_format()
        INDIANRED4 = self.RGB(139, 58, 58).rgb_format()
        INDIGO = self.RGB(75, 0, 130).rgb_format()
        IVORY1 = self.RGB(255, 255, 240).rgb_format()
        IVORY2 = self.RGB(238, 238, 224).rgb_format()
        IVORY3 = self.RGB(205, 205, 193).rgb_format()
        IVORY4 = self.RGB(139, 139, 131).rgb_format()
        IVORYBLACK = self.RGB(41, 36, 33).rgb_format()
        KHAKI = self.RGB(240, 230, 140).rgb_format()
        KHAKI1 = self.RGB(255, 246, 143).rgb_format()
        KHAKI2 = self.RGB(238, 230, 133).rgb_format()
        KHAKI3 = self.RGB(205, 198, 115).rgb_format()
        KHAKI4 = self.RGB(139, 134, 78).rgb_format()
        LAVENDER = self.RGB(230, 230, 250).rgb_format()
        LAVENDERBLUSH1 = self.RGB(255, 240, 245).rgb_format()
        LAVENDERBLUSH2 = self.RGB(238, 224, 229).rgb_format()
        LAVENDERBLUSH3 = self.RGB(205, 193, 197).rgb_format()
        LAVENDERBLUSH4 = self.RGB(139, 131, 134).rgb_format()
        LAWNGREEN = self.RGB(124, 252, 0).rgb_format()
        LEMONCHIFFON1 = self.RGB(255, 250, 205).rgb_format()
        LEMONCHIFFON2 = self.RGB(238, 233, 191).rgb_format()
        LEMONCHIFFON3 = self.RGB(205, 201, 165).rgb_format()
        LEMONCHIFFON4 = self.RGB(139, 137, 112).rgb_format()
        LIGHTBLUE = self.RGB(173, 216, 230).rgb_format()
        LIGHTBLUE1 = self.RGB(191, 239, 255).rgb_format()
        LIGHTBLUE2 = self.RGB(178, 223, 238).rgb_format()
        LIGHTBLUE3 = self.RGB(154, 192, 205).rgb_format()
        LIGHTBLUE4 = self.RGB(104, 131, 139).rgb_format()
        LIGHTCORAL = self.RGB(240, 128, 128).rgb_format()
        LIGHTCYAN1 = self.RGB(224, 255, 255).rgb_format()
        LIGHTCYAN2 = self.RGB(209, 238, 238).rgb_format()
        LIGHTCYAN3 = self.RGB(180, 205, 205).rgb_format()
        LIGHTCYAN4 = self.RGB(122, 139, 139).rgb_format()
        LIGHTGOLDENROD1 = self.RGB(255, 236, 139).rgb_format()
        LIGHTGOLDENROD2 = self.RGB(238, 220, 130).rgb_format()
        LIGHTGOLDENROD3 = self.RGB(205, 190, 112).rgb_format()
        LIGHTGOLDENROD4 = self.RGB(139, 129, 76).rgb_format()
        LIGHTGOLDENRODYELLOW = self.RGB(250, 250, 210).rgb_format()
        LIGHTGREY = self.RGB(211, 211, 211).rgb_format()
        LIGHTPINK = self.RGB(255, 182, 193).rgb_format()
        LIGHTPINK1 = self.RGB(255, 174, 185).rgb_format()
        LIGHTPINK2 = self.RGB(238, 162, 173).rgb_format()
        LIGHTPINK3 = self.RGB(205, 140, 149).rgb_format()
        LIGHTPINK4 = self.RGB(139, 95, 101).rgb_format()
        LIGHTSALMON1 = self.RGB(255, 160, 122).rgb_format()
        LIGHTSALMON2 = self.RGB(238, 149, 114).rgb_format()
        LIGHTSALMON3 = self.RGB(205, 129, 98).rgb_format()
        LIGHTSALMON4 = self.RGB(139, 87, 66).rgb_format()
        LIGHTSEAGREEN = self.RGB(32, 178, 170).rgb_format()
        LIGHTSKYBLUE = self.RGB(135, 206, 250).rgb_format()
        LIGHTSKYBLUE1 = self.RGB(176, 226, 255).rgb_format()
        LIGHTSKYBLUE2 = self.RGB(164, 211, 238).rgb_format()
        LIGHTSKYBLUE3 = self.RGB(141, 182, 205).rgb_format()
        LIGHTSKYBLUE4 = self.RGB(96, 123, 139).rgb_format()
        LIGHTSLATEBLUE = self.RGB(132, 112, 255).rgb_format()
        LIGHTSLATEGRAY = self.RGB(119, 136, 153).rgb_format()
        LIGHTSTEELBLUE = self.RGB(176, 196, 222).rgb_format()
        LIGHTSTEELBLUE1 = self.RGB(202, 225, 255).rgb_format()
        LIGHTSTEELBLUE2 = self.RGB(188, 210, 238).rgb_format()
        LIGHTSTEELBLUE3 = self.RGB(162, 181, 205).rgb_format()
        LIGHTSTEELBLUE4 = self.RGB(110, 123, 139).rgb_format()
        LIGHTYELLOW1 = self.RGB(255, 255, 224).rgb_format()
        LIGHTYELLOW2 = self.RGB(238, 238, 209).rgb_format()
        LIGHTYELLOW3 = self.RGB(205, 205, 180).rgb_format()
        LIGHTYELLOW4 = self.RGB(139, 139, 122).rgb_format()
        LIMEGREEN = self.RGB(50, 205, 50).rgb_format()
        LINEN = self.RGB(250, 240, 230).rgb_format()
        MAGENTA = self.RGB(255, 0, 255).rgb_format()
        MAGENTA2 = self.RGB(238, 0, 238).rgb_format()
        MAGENTA3 = self.RGB(205, 0, 205).rgb_format()
        MAGENTA4 = self.RGB(139, 0, 139).rgb_format()
        MANGANESEBLUE = self.RGB(3, 168, 158).rgb_format()
        MAROON = self.RGB(128, 0, 0).rgb_format()
        MAROON1 = self.RGB(255, 52, 179).rgb_format()
        MAROON2 = self.RGB(238, 48, 167).rgb_format()
        MAROON3 = self.RGB(205, 41, 144).rgb_format()
        MAROON4 = self.RGB(139, 28, 98).rgb_format()
        MEDIUMORCHID = self.RGB(186, 85, 211).rgb_format()
        MEDIUMORCHID1 = self.RGB(224, 102, 255).rgb_format()
        MEDIUMORCHID2 = self.RGB(209, 95, 238).rgb_format()
        MEDIUMORCHID3 = self.RGB(180, 82, 205).rgb_format()
        MEDIUMORCHID4 = self.RGB(122, 55, 139).rgb_format()
        MEDIUMPURPLE = self.RGB(147, 112, 219).rgb_format()
        MEDIUMPURPLE1 = self.RGB(171, 130, 255).rgb_format()
        MEDIUMPURPLE2 = self.RGB(159, 121, 238).rgb_format()
        MEDIUMPURPLE3 = self.RGB(137, 104, 205).rgb_format()
        MEDIUMPURPLE4 = self.RGB(93, 71, 139).rgb_format()
        MEDIUMSEAGREEN = self.RGB(60, 179, 113).rgb_format()
        MEDIUMSLATEBLUE = self.RGB(123, 104, 238).rgb_format()
        MEDIUMSPRINGGREEN = self.RGB(0, 250, 154).rgb_format()
        MEDIUMTURQUOISE = self.RGB(72, 209, 204).rgb_format()
        MEDIUMVIOLETRED = self.RGB(199, 21, 133).rgb_format()
        MELON = self.RGB(227, 168, 105).rgb_format()
        MIDNIGHTBLUE = self.RGB(25, 25, 112).rgb_format()
        MINT = self.RGB(189, 252, 201).rgb_format()
        MINTCREAM = self.RGB(245, 255, 250).rgb_format()
        MISTYROSE1 = self.RGB(255, 228, 225).rgb_format()
        MISTYROSE2 = self.RGB(238, 213, 210).rgb_format()
        MISTYROSE3 = self.RGB(205, 183, 181).rgb_format()
        MISTYROSE4 = self.RGB(139, 125, 123).rgb_format()
        MOCCASIN = self.RGB(255, 228, 181).rgb_format()
        NAVAJOWHITE1 = self.RGB(255, 222, 173).rgb_format()
        NAVAJOWHITE2 = self.RGB(238, 207, 161).rgb_format()
        NAVAJOWHITE3 = self.RGB(205, 179, 139).rgb_format()
        NAVAJOWHITE4 = self.RGB(139, 121, 94).rgb_format()
        NAVY = self.RGB(0, 0, 128).rgb_format()
        OLDLACE = self.RGB(253, 245, 230).rgb_format()
        OLIVE = self.RGB(128, 128, 0).rgb_format()
        OLIVEDRAB = self.RGB(107, 142, 35).rgb_format()
        OLIVEDRAB1 = self.RGB(192, 255, 62).rgb_format()
        OLIVEDRAB2 = self.RGB(179, 238, 58).rgb_format()
        OLIVEDRAB3 = self.RGB(154, 205, 50).rgb_format()
        OLIVEDRAB4 = self.RGB(105, 139, 34).rgb_format()
        ORANGE = self.RGB(255, 128, 0).rgb_format()
        ORANGE1 = self.RGB(255, 165, 0).rgb_format()
        ORANGE2 = self.RGB(238, 154, 0).rgb_format()
        ORANGE3 = self.RGB(205, 133, 0).rgb_format()
        ORANGE4 = self.RGB(139, 90, 0).rgb_format()
        ORANGERED1 = self.RGB(255, 69, 0).rgb_format()
        ORANGERED2 = self.RGB(238, 64, 0).rgb_format()
        ORANGERED3 = self.RGB(205, 55, 0).rgb_format()
        ORANGERED4 = self.RGB(139, 37, 0).rgb_format()
        ORCHID = self.RGB(218, 112, 214).rgb_format()
        ORCHID1 = self.RGB(255, 131, 250).rgb_format()
        ORCHID2 = self.RGB(238, 122, 233).rgb_format()
        ORCHID3 = self.RGB(205, 105, 201).rgb_format()
        ORCHID4 = self.RGB(139, 71, 137).rgb_format()
        PALEGOLDENROD = self.RGB(238, 232, 170).rgb_format()
        PALEGREEN = self.RGB(152, 251, 152).rgb_format()
        PALEGREEN1 = self.RGB(154, 255, 154).rgb_format()
        PALEGREEN2 = self.RGB(144, 238, 144).rgb_format()
        PALEGREEN3 = self.RGB(124, 205, 124).rgb_format()
        PALEGREEN4 = self.RGB(84, 139, 84).rgb_format()
        PALETURQUOISE1 = self.RGB(187, 255, 255).rgb_format()
        PALETURQUOISE2 = self.RGB(174, 238, 238).rgb_format()
        PALETURQUOISE3 = self.RGB(150, 205, 205).rgb_format()
        PALETURQUOISE4 = self.RGB(102, 139, 139).rgb_format()
        PALEVIOLETRED = self.RGB(219, 112, 147).rgb_format()
        PALEVIOLETRED1 = self.RGB(255, 130, 171).rgb_format()
        PALEVIOLETRED2 = self.RGB(238, 121, 159).rgb_format()
        PALEVIOLETRED3 = self.RGB(205, 104, 137).rgb_format()
        PALEVIOLETRED4 = self.RGB(139, 71, 93).rgb_format()
        PAPAYAWHIP = self.RGB(255, 239, 213).rgb_format()
        PEACHPUFF1 = self.RGB(255, 218, 185).rgb_format()
        PEACHPUFF2 = self.RGB(238, 203, 173).rgb_format()
        PEACHPUFF3 = self.RGB(205, 175, 149).rgb_format()
        PEACHPUFF4 = self.RGB(139, 119, 101).rgb_format()
        PEACOCK = self.RGB(51, 161, 201).rgb_format()
        PINK = self.RGB(255, 192, 203).rgb_format()
        PINK1 = self.RGB(255, 181, 197).rgb_format()
        PINK2 = self.RGB(238, 169, 184).rgb_format()
        PINK3 = self.RGB(205, 145, 158).rgb_format()
        PINK4 = self.RGB(139, 99, 108).rgb_format()
        PLUM = self.RGB(221, 160, 221).rgb_format()
        PLUM1 = self.RGB(255, 187, 255).rgb_format()
        PLUM2 = self.RGB(238, 174, 238).rgb_format()
        PLUM3 = self.RGB(205, 150, 205).rgb_format()
        PLUM4 = self.RGB(139, 102, 139).rgb_format()
        POWDERBLUE = self.RGB(176, 224, 230).rgb_format()
        PURPLE = self.RGB(128, 0, 128).rgb_format()
        PURPLE1 = self.RGB(155, 48, 255).rgb_format()
        PURPLE2 = self.RGB(145, 44, 238).rgb_format()
        PURPLE3 = self.RGB(125, 38, 205).rgb_format()
        PURPLE4 = self.RGB(85, 26, 139).rgb_format()
        RASPBERRY = self.RGB(135, 38, 87).rgb_format()
        RAWSIENNA = self.RGB(199, 97, 20).rgb_format()
        RED1 = self.RGB(255, 0, 0).rgb_format()
        RED2 = self.RGB(238, 0, 0).rgb_format()
        RED3 = self.RGB(205, 0, 0).rgb_format()
        RED4 = self.RGB(139, 0, 0).rgb_format()
        ROSYBROWN = self.RGB(188, 143, 143).rgb_format()
        ROSYBROWN1 = self.RGB(255, 193, 193).rgb_format()
        ROSYBROWN2 = self.RGB(238, 180, 180).rgb_format()
        ROSYBROWN3 = self.RGB(205, 155, 155).rgb_format()
        ROSYBROWN4 = self.RGB(139, 105, 105).rgb_format()
        ROYALBLUE = self.RGB(65, 105, 225).rgb_format()
        ROYALBLUE1 = self.RGB(72, 118, 255).rgb_format()
        ROYALBLUE2 = self.RGB(67, 110, 238).rgb_format()
        ROYALBLUE3 = self.RGB(58, 95, 205).rgb_format()
        ROYALBLUE4 = self.RGB(39, 64, 139).rgb_format()
        SALMON = self.RGB(250, 128, 114).rgb_format()
        SALMON1 = self.RGB(255, 140, 105).rgb_format()
        SALMON2 = self.RGB(238, 130, 98).rgb_format()
        SALMON3 = self.RGB(205, 112, 84).rgb_format()
        SALMON4 = self.RGB(139, 76, 57).rgb_format()
        SANDYBROWN = self.RGB(244, 164, 96).rgb_format()
        SAPGREEN = self.RGB(48, 128, 20).rgb_format()
        SEAGREEN1 = self.RGB(84, 255, 159).rgb_format()
        SEAGREEN2 = self.RGB(78, 238, 148).rgb_format()
        SEAGREEN3 = self.RGB(67, 205, 128).rgb_format()
        SEAGREEN4 = self.RGB(46, 139, 87).rgb_format()
        SEASHELL1 = self.RGB(255, 245, 238).rgb_format()
        SEASHELL2 = self.RGB(238, 229, 222).rgb_format()
        SEASHELL3 = self.RGB(205, 197, 191).rgb_format()
        SEASHELL4 = self.RGB(139, 134, 130).rgb_format()
        SEPIA = self.RGB(94, 38, 18).rgb_format()
        SGIBEET = self.RGB(142, 56, 142).rgb_format()
        SGIBRIGHTGRAY = self.RGB(197, 193, 170).rgb_format()
        SGICHARTREUSE = self.RGB(113, 198, 113).rgb_format()
        SGIDARKGRAY = self.RGB(85, 85, 85).rgb_format()
        SGIGRAY12 = self.RGB(30, 30, 30).rgb_format()
        SGIGRAY16 = self.RGB(40, 40, 40).rgb_format()
        SGIGRAY32 = self.RGB(81, 81, 81).rgb_format()
        SGIGRAY36 = self.RGB(91, 91, 91).rgb_format()
        SGIGRAY52 = self.RGB(132, 132, 132).rgb_format()
        SGIGRAY56 = self.RGB(142, 142, 142).rgb_format()
        SGIGRAY72 = self.RGB(183, 183, 183).rgb_format()
        SGIGRAY76 = self.RGB(193, 193, 193).rgb_format()
        SGIGRAY92 = self.RGB(234, 234, 234).rgb_format()
        SGIGRAY96 = self.RGB(244, 244, 244).rgb_format()
        SGILIGHTBLUE = self.RGB(125, 158, 192).rgb_format()
        SGILIGHTGRAY = self.RGB(170, 170, 170).rgb_format()
        SGIOLIVEDRAB = self.RGB(142, 142, 56).rgb_format()
        SGISALMON = self.RGB(198, 113, 113).rgb_format()
        SGISLATEBLUE = self.RGB(113, 113, 198).rgb_format()
        SGITEAL = self.RGB(56, 142, 142).rgb_format()
        SIENNA = self.RGB(160, 82, 45).rgb_format()
        SIENNA1 = self.RGB(255, 130, 71).rgb_format()
        SIENNA2 = self.RGB(238, 121, 66).rgb_format()
        SIENNA3 = self.RGB(205, 104, 57).rgb_format()
        SIENNA4 = self.RGB(139, 71, 38).rgb_format()
        SILVER = self.RGB(192, 192, 192).rgb_format()
        SKYBLUE = self.RGB(135, 206, 235).rgb_format()
        SKYBLUE1 = self.RGB(135, 206, 255).rgb_format()
        SKYBLUE2 = self.RGB(126, 192, 238).rgb_format()
        SKYBLUE3 = self.RGB(108, 166, 205).rgb_format()
        SKYBLUE4 = self.RGB(74, 112, 139).rgb_format()
        SLATEBLUE = self.RGB(106, 90, 205).rgb_format()
        SLATEBLUE1 = self.RGB(131, 111, 255).rgb_format()
        SLATEBLUE2 = self.RGB(122, 103, 238).rgb_format()
        SLATEBLUE3 = self.RGB(105, 89, 205).rgb_format()
        SLATEBLUE4 = self.RGB(71, 60, 139).rgb_format()
        SLATEGRAY = self.RGB(112, 128, 144).rgb_format()
        SLATEGRAY1 = self.RGB(198, 226, 255).rgb_format()
        SLATEGRAY2 = self.RGB(185, 211, 238).rgb_format()
        SLATEGRAY3 = self.RGB(159, 182, 205).rgb_format()
        SLATEGRAY4 = self.RGB(108, 123, 139).rgb_format()
        SNOW1 = self.RGB(255, 250, 250).rgb_format()
        SNOW2 = self.RGB(238, 233, 233).rgb_format()
        SNOW3 = self.RGB(205, 201, 201).rgb_format()
        SNOW4 = self.RGB(139, 137, 137).rgb_format()
        SPRINGGREEN = self.RGB(0, 255, 127).rgb_format()
        SPRINGGREEN1 = self.RGB(0, 238, 118).rgb_format()
        SPRINGGREEN2 = self.RGB(0, 205, 102).rgb_format()
        SPRINGGREEN3 = self.RGB(0, 139, 69).rgb_format()
        STEELBLUE = self.RGB(70, 130, 180).rgb_format()
        STEELBLUE1 = self.RGB(99, 184, 255).rgb_format()
        STEELBLUE2 = self.RGB(92, 172, 238).rgb_format()
        STEELBLUE3 = self.RGB(79, 148, 205).rgb_format()
        STEELBLUE4 = self.RGB(54, 100, 139).rgb_format()
        TAN = self.RGB(210, 180, 140).rgb_format()
        TAN1 = self.RGB(255, 165, 79).rgb_format()
        TAN2 = self.RGB(238, 154, 73).rgb_format()
        TAN3 = self.RGB(205, 133, 63).rgb_format()
        TAN4 = self.RGB(139, 90, 43).rgb_format()
        TEAL = self.RGB(0, 128, 128).rgb_format()
        THISTLE = self.RGB(216, 191, 216).rgb_format()
        THISTLE1 = self.RGB(255, 225, 255).rgb_format()
        THISTLE2 = self.RGB(238, 210, 238).rgb_format()
        THISTLE3 = self.RGB(205, 181, 205).rgb_format()
        THISTLE4 = self.RGB(139, 123, 139).rgb_format()
        TOMATO1 = self.RGB(255, 99, 71).rgb_format()
        TOMATO2 = self.RGB(238, 92, 66).rgb_format()
        TOMATO3 = self.RGB(205, 79, 57).rgb_format()
        TOMATO4 = self.RGB(139, 54, 38).rgb_format()
        TURQUOISE = self.RGB(64, 224, 208).rgb_format()
        TURQUOISE1 = self.RGB(0, 245, 255).rgb_format()
        TURQUOISE2 = self.RGB(0, 229, 238).rgb_format()
        TURQUOISE3 = self.RGB(0, 197, 205).rgb_format()
        TURQUOISE4 = self.RGB(0, 134, 139).rgb_format()
        TURQUOISEBLUE = self.RGB(0, 199, 140).rgb_format()
        VIOLET = self.RGB(238, 130, 238).rgb_format()
        VIOLETRED = self.RGB(208, 32, 144).rgb_format()
        VIOLETRED1 = self.RGB(255, 62, 150).rgb_format()
        VIOLETRED2 = self.RGB(238, 58, 140).rgb_format()
        VIOLETRED3 = self.RGB(205, 50, 120).rgb_format()
        VIOLETRED4 = self.RGB(139, 34, 82).rgb_format()
        WARMGREY = self.RGB(128, 128, 105).rgb_format()
        WHEAT = self.RGB(245, 222, 179).rgb_format()
        WHEAT1 = self.RGB(255, 231, 186).rgb_format()
        WHEAT2 = self.RGB(238, 216, 174).rgb_format()
        WHEAT3 = self.RGB(205, 186, 150).rgb_format()
        WHEAT4 = self.RGB(139, 126, 102).rgb_format()
        WHITE = self.RGB(255, 255, 255).rgb_format()
        WHITESMOKE = self.RGB(245, 245, 245).rgb_format()
        WHITESMOKE = self.RGB(245, 245, 245).rgb_format()
        YELLOW1 = self.RGB(255, 255, 0).rgb_format()
        YELLOW2 = self.RGB(238, 238, 0).rgb_format()
        YELLOW3 = self.RGB(205, 205, 0).rgb_format()
        YELLOW4 = self.RGB(139, 139, 0).rgb_format()

        dict_containing_variables = locals()
        del dict_containing_variables['self']

        return dict_containing_variables # <= NOTE Return a dictionary containing the current scope's local variables.

    def colors_rgb_name(self) -> dict: # DESC => Color RGB contants
        """ Return a dictionary of color variables in RGB format with color names as keys.
        
        Returns:
            dict: A dictionary containing color variables in RGB format with color names as keys.

        Example:
        ```python
            colors = ColorsConstants()
            rgb_colors = colors.colors_rgb_name()
            print(rgb_colors)  # Output: {'ALICEBLUE': RGB(red=240, green=248, blue=255), ...}
        ```
        """
        ALICEBLUE = self.RGB(240, 248, 255)
        ANTIQUEWHITE = self.RGB(250, 235, 215)
        ANTIQUEWHITE1 = self.RGB(255, 239, 219)
        ANTIQUEWHITE2 = self.RGB(238, 223, 204)
        ANTIQUEWHITE3 = self.RGB(205, 192, 176)
        ANTIQUEWHITE4 = self.RGB(139, 131, 120)
        AQUA = self.RGB(0, 255, 255)
        AQUAMARINE1 = self.RGB(127, 255, 212)
        AQUAMARINE2 = self.RGB(118, 238, 198)
        AQUAMARINE3 = self.RGB(102, 205, 170)
        AQUAMARINE4 = self.RGB(69, 139, 116)
        AZURE1 = self.RGB(240, 255, 255)
        AZURE2 = self.RGB(224, 238, 238)
        AZURE3 = self.RGB(193, 205, 205)
        AZURE4 = self.RGB(131, 139, 139)
        BANANA = self.RGB(227, 207, 87)
        BEIGE = self.RGB(245, 245, 220)
        BISQUE1 = self.RGB(255, 228, 196)
        BISQUE2 = self.RGB(238, 213, 183)
        BISQUE3 = self.RGB(205, 183, 158)
        BISQUE4 = self.RGB(139, 125, 107)
        BLACK = self.RGB(0, 0, 0)
        BLANCHEDALMOND = self.RGB(255, 235, 205)
        BLUE = self.RGB(0, 0, 255)
        BLUE2 = self.RGB(0, 0, 238)
        BLUE3 = self.RGB(0, 0, 205)
        BLUE4 = self.RGB(0, 0, 139)
        BLUEVIOLET = self.RGB(138, 43, 226)
        BRICK = self.RGB(156, 102, 31)
        BROWN = self.RGB(165, 42, 42)
        BROWN1 = self.RGB(255, 64, 64)
        BROWN2 = self.RGB(238, 59, 59)
        BROWN3 = self.RGB(205, 51, 51)
        BROWN4 = self.RGB(139, 35, 35)
        BURLYWOOD = self.RGB(222, 184, 135)
        BURLYWOOD1 = self.RGB(255, 211, 155)
        BURLYWOOD2 = self.RGB(238, 197, 145)
        BURLYWOOD3 = self.RGB(205, 170, 125)
        BURLYWOOD4 = self.RGB(139, 115, 85)
        BURNTSIENNA = self.RGB(138, 54, 15)
        BURNTUMBER = self.RGB(138, 51, 36)
        CADETBLUE = self.RGB(95, 158, 160)
        CADETBLUE1 = self.RGB(152, 245, 255)
        CADETBLUE2 = self.RGB(142, 229, 238)
        CADETBLUE3 = self.RGB(122, 197, 205)
        CADETBLUE4 = self.RGB(83, 134, 139)
        CADMIUMORANGE = self.RGB(255, 97, 3)
        CADMIUMYELLOW = self.RGB(255, 153, 18)
        CARROT = self.RGB(237, 145, 33)
        CHARTREUSE1 = self.RGB(127, 255, 0)
        CHARTREUSE2 = self.RGB(118, 238, 0)
        CHARTREUSE3 = self.RGB(102, 205, 0)
        CHARTREUSE4 = self.RGB(69, 139, 0)
        CHOCOLATE = self.RGB(210, 105, 30)
        CHOCOLATE1 = self.RGB(255, 127, 36)
        CHOCOLATE2 = self.RGB(238, 118, 33)
        CHOCOLATE3 = self.RGB(205, 102, 29)
        CHOCOLATE4 = self.RGB(139, 69, 19)
        COBALT = self.RGB(61, 89, 171)
        COBALTGREEN = self.RGB(61, 145, 64)
        COLDGREY = self.RGB(128, 138, 135)
        CORAL = self.RGB(255, 127, 80)
        CORAL1 = self.RGB(255, 114, 86)
        CORAL2 = self.RGB(238, 106, 80)
        CORAL3 = self.RGB(205, 91, 69)
        CORAL4 = self.RGB(139, 62, 47)
        CORNFLOWERBLUE = self.RGB(100, 149, 237)
        CORNSILK1 = self.RGB(255, 248, 220)
        CORNSILK2 = self.RGB(238, 232, 205)
        CORNSILK3 = self.RGB(205, 200, 177)
        CORNSILK4 = self.RGB(139, 136, 120)
        CRIMSON = self.RGB(220, 20, 60)
        CYAN2 = self.RGB(0, 238, 238)
        CYAN3 = self.RGB(0, 205, 205)
        CYAN4 = self.RGB(0, 139, 139)
        DARKGOLDENROD = self.RGB(184, 134, 11)
        DARKGOLDENROD1 = self.RGB(255, 185, 15)
        DARKGOLDENROD2 = self.RGB(238, 173, 14)
        DARKGOLDENROD3 = self.RGB(205, 149, 12)
        DARKGOLDENROD4 = self.RGB(139, 101, 8)
        DARKGRAY = self.RGB(169, 169, 169)
        DARKGREEN = self.RGB(0, 100, 0)
        DARKKHAKI = self.RGB(189, 183, 107)
        DARKOLIVEGREEN = self.RGB(85, 107, 47)
        DARKOLIVEGREEN1 = self.RGB(202, 255, 112)
        DARKOLIVEGREEN2 = self.RGB(188, 238, 104)
        DARKOLIVEGREEN3 = self.RGB(162, 205, 90)
        DARKOLIVEGREEN4 = self.RGB(110, 139, 61)
        DARKORANGE = self.RGB(255, 140, 0)
        DARKORANGE1 = self.RGB(255, 127, 0)
        DARKORANGE2 = self.RGB(238, 118, 0)
        DARKORANGE3 = self.RGB(205, 102, 0)
        DARKORANGE4 = self.RGB(139, 69, 0)
        DARKORCHID = self.RGB(153, 50, 204)
        DARKORCHID1 = self.RGB(191, 62, 255)
        DARKORCHID2 = self.RGB(178, 58, 238)
        DARKORCHID3 = self.RGB(154, 50, 205)
        DARKORCHID4 = self.RGB(104, 34, 139)
        DARKSALMON = self.RGB(233, 150, 122)
        DARKSEAGREEN = self.RGB(143, 188, 143)
        DARKSEAGREEN1 = self.RGB(193, 255, 193)
        DARKSEAGREEN2 = self.RGB(180, 238, 180)
        DARKSEAGREEN3 = self.RGB(155, 205, 155)
        DARKSEAGREEN4 = self.RGB(105, 139, 105)
        DARKSLATEBLUE = self.RGB(72, 61, 139)
        DARKSLATEGRAY = self.RGB(47, 79, 79)
        DARKSLATEGRAY1 = self.RGB(151, 255, 255)
        DARKSLATEGRAY2 = self.RGB(141, 238, 238)
        DARKSLATEGRAY3 = self.RGB(121, 205, 205)
        DARKSLATEGRAY4 = self.RGB(82, 139, 139)
        DARKTURQUOISE = self.RGB(0, 206, 209)
        DARKVIOLET = self.RGB(148, 0, 211)
        DEEPPINK1 = self.RGB(255, 20, 147)
        DEEPPINK2 = self.RGB(238, 18, 137)
        DEEPPINK3 = self.RGB(205, 16, 118)
        DEEPPINK4 = self.RGB(139, 10, 80)
        DEEPSKYBLUE1 = self.RGB(0, 191, 255)
        DEEPSKYBLUE2 = self.RGB(0, 178, 238)
        DEEPSKYBLUE3 = self.RGB(0, 154, 205)
        DEEPSKYBLUE4 = self.RGB(0, 104, 139)
        DIMGRAY = self.RGB(105, 105, 105)
        DIMGRAY = self.RGB(105, 105, 105)
        DODGERBLUE1 = self.RGB(30, 144, 255)
        DODGERBLUE2 = self.RGB(28, 134, 238)
        DODGERBLUE3 = self.RGB(24, 116, 205)
        DODGERBLUE4 = self.RGB(16, 78, 139)
        EGGSHELL = self.RGB(252, 230, 201)
        EMERALDGREEN = self.RGB(0, 201, 87)
        FIREBRICK = self.RGB(178, 34, 34)
        FIREBRICK1 = self.RGB(255, 48, 48)
        FIREBRICK2 = self.RGB(238, 44, 44)
        FIREBRICK3 = self.RGB(205, 38, 38)
        FIREBRICK4 = self.RGB(139, 26, 26)
        FLESH = self.RGB(255, 125, 64)
        FLORALWHITE = self.RGB(255, 250, 240)
        FORESTGREEN = self.RGB(34, 139, 34)
        GAINSBORO = self.RGB(220, 220, 220)
        GHOSTWHITE = self.RGB(248, 248, 255)
        GOLD1 = self.RGB(255, 215, 0)
        GOLD2 = self.RGB(238, 201, 0)
        GOLD3 = self.RGB(205, 173, 0)
        GOLD4 = self.RGB(139, 117, 0)
        GOLDENROD = self.RGB(218, 165, 32)
        GOLDENROD1 = self.RGB(255, 193, 37)
        GOLDENROD2 = self.RGB(238, 180, 34)
        GOLDENROD3 = self.RGB(205, 155, 29)
        GOLDENROD4 = self.RGB(139, 105, 20)
        GRAY = self.RGB(128, 128, 128)
        GRAY1 = self.RGB(3, 3, 3)
        GRAY10 = self.RGB(26, 26, 26)
        GRAY11 = self.RGB(28, 28, 28)
        GRAY12 = self.RGB(31, 31, 31)
        GRAY13 = self.RGB(33, 33, 33)
        GRAY14 = self.RGB(36, 36, 36)
        GRAY15 = self.RGB(38, 38, 38)
        GRAY16 = self.RGB(41, 41, 41)
        GRAY17 = self.RGB(43, 43, 43)
        GRAY18 = self.RGB(46, 46, 46)
        GRAY19 = self.RGB(48, 48, 48)
        GRAY2 = self.RGB(5, 5, 5)
        GRAY20 = self.RGB(51, 51, 51)
        GRAY21 = self.RGB(54, 54, 54)
        GRAY22 = self.RGB(56, 56, 56)
        GRAY23 = self.RGB(59, 59, 59)
        GRAY24 = self.RGB(61, 61, 61)
        GRAY25 = self.RGB(64, 64, 64)
        GRAY26 = self.RGB(66, 66, 66)
        GRAY27 = self.RGB(69, 69, 69)
        GRAY28 = self.RGB(71, 71, 71)
        GRAY29 = self.RGB(74, 74, 74)
        GRAY3 = self.RGB(8, 8, 8)
        GRAY30 = self.RGB(77, 77, 77)
        GRAY31 = self.RGB(79, 79, 79)
        GRAY32 = self.RGB(82, 82, 82)
        GRAY33 = self.RGB(84, 84, 84)
        GRAY34 = self.RGB(87, 87, 87)
        GRAY35 = self.RGB(89, 89, 89)
        GRAY36 = self.RGB(92, 92, 92)
        GRAY37 = self.RGB(94, 94, 94)
        GRAY38 = self.RGB(97, 97, 97)
        GRAY39 = self.RGB(99, 99, 99)
        GRAY4 = self.RGB(10, 10, 10)
        GRAY40 = self.RGB(102, 102, 102)
        GRAY42 = self.RGB(107, 107, 107)
        GRAY43 = self.RGB(110, 110, 110)
        GRAY44 = self.RGB(112, 112, 112)
        GRAY45 = self.RGB(115, 115, 115)
        GRAY46 = self.RGB(117, 117, 117)
        GRAY47 = self.RGB(120, 120, 120)
        GRAY48 = self.RGB(122, 122, 122)
        GRAY49 = self.RGB(125, 125, 125)
        GRAY5 = self.RGB(13, 13, 13)
        GRAY50 = self.RGB(127, 127, 127)
        GRAY51 = self.RGB(130, 130, 130)
        GRAY52 = self.RGB(133, 133, 133)
        GRAY53 = self.RGB(135, 135, 135)
        GRAY54 = self.RGB(138, 138, 138)
        GRAY55 = self.RGB(140, 140, 140)
        GRAY56 = self.RGB(143, 143, 143)
        GRAY57 = self.RGB(145, 145, 145)
        GRAY58 = self.RGB(148, 148, 148)
        GRAY59 = self.RGB(150, 150, 150)
        GRAY6 = self.RGB(15, 15, 15)
        GRAY60 = self.RGB(153, 153, 153)
        GRAY61 = self.RGB(156, 156, 156)
        GRAY62 = self.RGB(158, 158, 158)
        GRAY63 = self.RGB(161, 161, 161)
        GRAY64 = self.RGB(163, 163, 163)
        GRAY65 = self.RGB(166, 166, 166)
        GRAY66 = self.RGB(168, 168, 168)
        GRAY67 = self.RGB(171, 171, 171)
        GRAY68 = self.RGB(173, 173, 173)
        GRAY69 = self.RGB(176, 176, 176)
        GRAY7 = self.RGB(18, 18, 18)
        GRAY70 = self.RGB(179, 179, 179)
        GRAY71 = self.RGB(181, 181, 181)
        GRAY72 = self.RGB(184, 184, 184)
        GRAY73 = self.RGB(186, 186, 186)
        GRAY74 = self.RGB(189, 189, 189)
        GRAY75 = self.RGB(191, 191, 191)
        GRAY76 = self.RGB(194, 194, 194)
        GRAY77 = self.RGB(196, 196, 196)
        GRAY78 = self.RGB(199, 199, 199)
        GRAY79 = self.RGB(201, 201, 201)
        GRAY8 = self.RGB(20, 20, 20)
        GRAY80 = self.RGB(204, 204, 204)
        GRAY81 = self.RGB(207, 207, 207)
        GRAY82 = self.RGB(209, 209, 209)
        GRAY83 = self.RGB(212, 212, 212)
        GRAY84 = self.RGB(214, 214, 214)
        GRAY85 = self.RGB(217, 217, 217)
        GRAY86 = self.RGB(219, 219, 219)
        GRAY87 = self.RGB(222, 222, 222)
        GRAY88 = self.RGB(224, 224, 224)
        GRAY89 = self.RGB(227, 227, 227)
        GRAY9 = self.RGB(23, 23, 23)
        GRAY90 = self.RGB(229, 229, 229)
        GRAY91 = self.RGB(232, 232, 232)
        GRAY92 = self.RGB(235, 235, 235)
        GRAY93 = self.RGB(237, 237, 237)
        GRAY94 = self.RGB(240, 240, 240)
        GRAY95 = self.RGB(242, 242, 242)
        GRAY97 = self.RGB(247, 247, 247)
        GRAY98 = self.RGB(250, 250, 250)
        GRAY99 = self.RGB(252, 252, 252)
        GREEN = self.RGB(0, 128, 0)
        GREEN1 = self.RGB(0, 255, 0)
        GREEN2 = self.RGB(0, 238, 0)
        GREEN3 = self.RGB(0, 205, 0)
        GREEN4 = self.RGB(0, 139, 0)
        GREENYELLOW = self.RGB(173, 255, 47)
        HONEYDEW1 = self.RGB(240, 255, 240)
        HONEYDEW2 = self.RGB(224, 238, 224)
        HONEYDEW3 = self.RGB(193, 205, 193)
        HONEYDEW4 = self.RGB(131, 139, 131)
        HOTPINK = self.RGB(255, 105, 180)
        HOTPINK1 = self.RGB(255, 110, 180)
        HOTPINK2 = self.RGB(238, 106, 167)
        HOTPINK3 = self.RGB(205, 96, 144)
        HOTPINK4 = self.RGB(139, 58, 98)
        INDIANRED = self.RGB(176, 23, 31)
        INDIANRED = self.RGB(205, 92, 92)
        INDIANRED1 = self.RGB(255, 106, 106)
        INDIANRED2 = self.RGB(238, 99, 99)
        INDIANRED3 = self.RGB(205, 85, 85)
        INDIANRED4 = self.RGB(139, 58, 58)
        INDIGO = self.RGB(75, 0, 130)
        IVORY1 = self.RGB(255, 255, 240)
        IVORY2 = self.RGB(238, 238, 224)
        IVORY3 = self.RGB(205, 205, 193)
        IVORY4 = self.RGB(139, 139, 131)
        IVORYBLACK = self.RGB(41, 36, 33)
        KHAKI = self.RGB(240, 230, 140)
        KHAKI1 = self.RGB(255, 246, 143)
        KHAKI2 = self.RGB(238, 230, 133)
        KHAKI3 = self.RGB(205, 198, 115)
        KHAKI4 = self.RGB(139, 134, 78)
        LAVENDER = self.RGB(230, 230, 250)
        LAVENDERBLUSH1 = self.RGB(255, 240, 245)
        LAVENDERBLUSH2 = self.RGB(238, 224, 229)
        LAVENDERBLUSH3 = self.RGB(205, 193, 197)
        LAVENDERBLUSH4 = self.RGB(139, 131, 134)
        LAWNGREEN = self.RGB(124, 252, 0)
        LEMONCHIFFON1 = self.RGB(255, 250, 205)
        LEMONCHIFFON2 = self.RGB(238, 233, 191)
        LEMONCHIFFON3 = self.RGB(205, 201, 165)
        LEMONCHIFFON4 = self.RGB(139, 137, 112)
        LIGHTBLUE = self.RGB(173, 216, 230)
        LIGHTBLUE1 = self.RGB(191, 239, 255)
        LIGHTBLUE2 = self.RGB(178, 223, 238)
        LIGHTBLUE3 = self.RGB(154, 192, 205)
        LIGHTBLUE4 = self.RGB(104, 131, 139)
        LIGHTCORAL = self.RGB(240, 128, 128)
        LIGHTCYAN1 = self.RGB(224, 255, 255)
        LIGHTCYAN2 = self.RGB(209, 238, 238)
        LIGHTCYAN3 = self.RGB(180, 205, 205)
        LIGHTCYAN4 = self.RGB(122, 139, 139)
        LIGHTGOLDENROD1 = self.RGB(255, 236, 139)
        LIGHTGOLDENROD2 = self.RGB(238, 220, 130)
        LIGHTGOLDENROD3 = self.RGB(205, 190, 112)
        LIGHTGOLDENROD4 = self.RGB(139, 129, 76)
        LIGHTGOLDENRODYELLOW = self.RGB(250, 250, 210)
        LIGHTGREY = self.RGB(211, 211, 211)
        LIGHTPINK = self.RGB(255, 182, 193)
        LIGHTPINK1 = self.RGB(255, 174, 185)
        LIGHTPINK2 = self.RGB(238, 162, 173)
        LIGHTPINK3 = self.RGB(205, 140, 149)
        LIGHTPINK4 = self.RGB(139, 95, 101)
        LIGHTSALMON1 = self.RGB(255, 160, 122)
        LIGHTSALMON2 = self.RGB(238, 149, 114)
        LIGHTSALMON3 = self.RGB(205, 129, 98)
        LIGHTSALMON4 = self.RGB(139, 87, 66)
        LIGHTSEAGREEN = self.RGB(32, 178, 170)
        LIGHTSKYBLUE = self.RGB(135, 206, 250)
        LIGHTSKYBLUE1 = self.RGB(176, 226, 255)
        LIGHTSKYBLUE2 = self.RGB(164, 211, 238)
        LIGHTSKYBLUE3 = self.RGB(141, 182, 205)
        LIGHTSKYBLUE4 = self.RGB(96, 123, 139)
        LIGHTSLATEBLUE = self.RGB(132, 112, 255)
        LIGHTSLATEGRAY = self.RGB(119, 136, 153)
        LIGHTSTEELBLUE = self.RGB(176, 196, 222)
        LIGHTSTEELBLUE1 = self.RGB(202, 225, 255)
        LIGHTSTEELBLUE2 = self.RGB(188, 210, 238)
        LIGHTSTEELBLUE3 = self.RGB(162, 181, 205)
        LIGHTSTEELBLUE4 = self.RGB(110, 123, 139)
        LIGHTYELLOW1 = self.RGB(255, 255, 224)
        LIGHTYELLOW2 = self.RGB(238, 238, 209)
        LIGHTYELLOW3 = self.RGB(205, 205, 180)
        LIGHTYELLOW4 = self.RGB(139, 139, 122)
        LIMEGREEN = self.RGB(50, 205, 50)
        LINEN = self.RGB(250, 240, 230)
        MAGENTA = self.RGB(255, 0, 255)
        MAGENTA2 = self.RGB(238, 0, 238)
        MAGENTA3 = self.RGB(205, 0, 205)
        MAGENTA4 = self.RGB(139, 0, 139)
        MANGANESEBLUE = self.RGB(3, 168, 158)
        MAROON = self.RGB(128, 0, 0)
        MAROON1 = self.RGB(255, 52, 179)
        MAROON2 = self.RGB(238, 48, 167)
        MAROON3 = self.RGB(205, 41, 144)
        MAROON4 = self.RGB(139, 28, 98)
        MEDIUMORCHID = self.RGB(186, 85, 211)
        MEDIUMORCHID1 = self.RGB(224, 102, 255)
        MEDIUMORCHID2 = self.RGB(209, 95, 238)
        MEDIUMORCHID3 = self.RGB(180, 82, 205)
        MEDIUMORCHID4 = self.RGB(122, 55, 139)
        MEDIUMPURPLE = self.RGB(147, 112, 219)
        MEDIUMPURPLE1 = self.RGB(171, 130, 255)
        MEDIUMPURPLE2 = self.RGB(159, 121, 238)
        MEDIUMPURPLE3 = self.RGB(137, 104, 205)
        MEDIUMPURPLE4 = self.RGB(93, 71, 139)
        MEDIUMSEAGREEN = self.RGB(60, 179, 113)
        MEDIUMSLATEBLUE = self.RGB(123, 104, 238)
        MEDIUMSPRINGGREEN = self.RGB(0, 250, 154)
        MEDIUMTURQUOISE = self.RGB(72, 209, 204)
        MEDIUMVIOLETRED = self.RGB(199, 21, 133)
        MELON = self.RGB(227, 168, 105)
        MIDNIGHTBLUE = self.RGB(25, 25, 112)
        MINT = self.RGB(189, 252, 201)
        MINTCREAM = self.RGB(245, 255, 250)
        MISTYROSE1 = self.RGB(255, 228, 225)
        MISTYROSE2 = self.RGB(238, 213, 210)
        MISTYROSE3 = self.RGB(205, 183, 181)
        MISTYROSE4 = self.RGB(139, 125, 123)
        MOCCASIN = self.RGB(255, 228, 181)
        NAVAJOWHITE1 = self.RGB(255, 222, 173)
        NAVAJOWHITE2 = self.RGB(238, 207, 161)
        NAVAJOWHITE3 = self.RGB(205, 179, 139)
        NAVAJOWHITE4 = self.RGB(139, 121, 94)
        NAVY = self.RGB(0, 0, 128)
        OLDLACE = self.RGB(253, 245, 230)
        OLIVE = self.RGB(128, 128, 0)
        OLIVEDRAB = self.RGB(107, 142, 35)
        OLIVEDRAB1 = self.RGB(192, 255, 62)
        OLIVEDRAB2 = self.RGB(179, 238, 58)
        OLIVEDRAB3 = self.RGB(154, 205, 50)
        OLIVEDRAB4 = self.RGB(105, 139, 34)
        ORANGE = self.RGB(255, 128, 0)
        ORANGE1 = self.RGB(255, 165, 0)
        ORANGE2 = self.RGB(238, 154, 0)
        ORANGE3 = self.RGB(205, 133, 0)
        ORANGE4 = self.RGB(139, 90, 0)
        ORANGERED1 = self.RGB(255, 69, 0)
        ORANGERED2 = self.RGB(238, 64, 0)
        ORANGERED3 = self.RGB(205, 55, 0)
        ORANGERED4 = self.RGB(139, 37, 0)
        ORCHID = self.RGB(218, 112, 214)
        ORCHID1 = self.RGB(255, 131, 250)
        ORCHID2 = self.RGB(238, 122, 233)
        ORCHID3 = self.RGB(205, 105, 201)
        ORCHID4 = self.RGB(139, 71, 137)
        PALEGOLDENROD = self.RGB(238, 232, 170)
        PALEGREEN = self.RGB(152, 251, 152)
        PALEGREEN1 = self.RGB(154, 255, 154)
        PALEGREEN2 = self.RGB(144, 238, 144)
        PALEGREEN3 = self.RGB(124, 205, 124)
        PALEGREEN4 = self.RGB(84, 139, 84)
        PALETURQUOISE1 = self.RGB(187, 255, 255)
        PALETURQUOISE2 = self.RGB(174, 238, 238)
        PALETURQUOISE3 = self.RGB(150, 205, 205)
        PALETURQUOISE4 = self.RGB(102, 139, 139)
        PALEVIOLETRED = self.RGB(219, 112, 147)
        PALEVIOLETRED1 = self.RGB(255, 130, 171)
        PALEVIOLETRED2 = self.RGB(238, 121, 159)
        PALEVIOLETRED3 = self.RGB(205, 104, 137)
        PALEVIOLETRED4 = self.RGB(139, 71, 93)
        PAPAYAWHIP = self.RGB(255, 239, 213)
        PEACHPUFF1 = self.RGB(255, 218, 185)
        PEACHPUFF2 = self.RGB(238, 203, 173)
        PEACHPUFF3 = self.RGB(205, 175, 149)
        PEACHPUFF4 = self.RGB(139, 119, 101)
        PEACOCK = self.RGB(51, 161, 201)
        PINK = self.RGB(255, 192, 203)
        PINK1 = self.RGB(255, 181, 197)
        PINK2 = self.RGB(238, 169, 184)
        PINK3 = self.RGB(205, 145, 158)
        PINK4 = self.RGB(139, 99, 108)
        PLUM = self.RGB(221, 160, 221)
        PLUM1 = self.RGB(255, 187, 255)
        PLUM2 = self.RGB(238, 174, 238)
        PLUM3 = self.RGB(205, 150, 205)
        PLUM4 = self.RGB(139, 102, 139)
        POWDERBLUE = self.RGB(176, 224, 230)
        PURPLE = self.RGB(128, 0, 128)
        PURPLE1 = self.RGB(155, 48, 255)
        PURPLE2 = self.RGB(145, 44, 238)
        PURPLE3 = self.RGB(125, 38, 205)
        PURPLE4 = self.RGB(85, 26, 139)
        RASPBERRY = self.RGB(135, 38, 87)
        RAWSIENNA = self.RGB(199, 97, 20)
        RED1 = self.RGB(255, 0, 0)
        RED2 = self.RGB(238, 0, 0)
        RED3 = self.RGB(205, 0, 0)
        RED4 = self.RGB(139, 0, 0)
        ROSYBROWN = self.RGB(188, 143, 143)
        ROSYBROWN1 = self.RGB(255, 193, 193)
        ROSYBROWN2 = self.RGB(238, 180, 180)
        ROSYBROWN3 = self.RGB(205, 155, 155)
        ROSYBROWN4 = self.RGB(139, 105, 105)
        ROYALBLUE = self.RGB(65, 105, 225)
        ROYALBLUE1 = self.RGB(72, 118, 255)
        ROYALBLUE2 = self.RGB(67, 110, 238)
        ROYALBLUE3 = self.RGB(58, 95, 205)
        ROYALBLUE4 = self.RGB(39, 64, 139)
        SALMON = self.RGB(250, 128, 114)
        SALMON1 = self.RGB(255, 140, 105)
        SALMON2 = self.RGB(238, 130, 98)
        SALMON3 = self.RGB(205, 112, 84)
        SALMON4 = self.RGB(139, 76, 57)
        SANDYBROWN = self.RGB(244, 164, 96)
        SAPGREEN = self.RGB(48, 128, 20)
        SEAGREEN1 = self.RGB(84, 255, 159)
        SEAGREEN2 = self.RGB(78, 238, 148)
        SEAGREEN3 = self.RGB(67, 205, 128)
        SEAGREEN4 = self.RGB(46, 139, 87)
        SEASHELL1 = self.RGB(255, 245, 238)
        SEASHELL2 = self.RGB(238, 229, 222)
        SEASHELL3 = self.RGB(205, 197, 191)
        SEASHELL4 = self.RGB(139, 134, 130)
        SEPIA = self.RGB(94, 38, 18)
        SGIBEET = self.RGB(142, 56, 142)
        SGIBRIGHTGRAY = self.RGB(197, 193, 170)
        SGICHARTREUSE = self.RGB(113, 198, 113)
        SGIDARKGRAY = self.RGB(85, 85, 85)
        SGIGRAY12 = self.RGB(30, 30, 30)
        SGIGRAY16 = self.RGB(40, 40, 40)
        SGIGRAY32 = self.RGB(81, 81, 81)
        SGIGRAY36 = self.RGB(91, 91, 91)
        SGIGRAY52 = self.RGB(132, 132, 132)
        SGIGRAY56 = self.RGB(142, 142, 142)
        SGIGRAY72 = self.RGB(183, 183, 183)
        SGIGRAY76 = self.RGB(193, 193, 193)
        SGIGRAY92 = self.RGB(234, 234, 234)
        SGIGRAY96 = self.RGB(244, 244, 244)
        SGILIGHTBLUE = self.RGB(125, 158, 192)
        SGILIGHTGRAY = self.RGB(170, 170, 170)
        SGIOLIVEDRAB = self.RGB(142, 142, 56)
        SGISALMON = self.RGB(198, 113, 113)
        SGISLATEBLUE = self.RGB(113, 113, 198)
        SGITEAL = self.RGB(56, 142, 142)
        SIENNA = self.RGB(160, 82, 45)
        SIENNA1 = self.RGB(255, 130, 71)
        SIENNA2 = self.RGB(238, 121, 66)
        SIENNA3 = self.RGB(205, 104, 57)
        SIENNA4 = self.RGB(139, 71, 38)
        SILVER = self.RGB(192, 192, 192)
        SKYBLUE = self.RGB(135, 206, 235)
        SKYBLUE1 = self.RGB(135, 206, 255)
        SKYBLUE2 = self.RGB(126, 192, 238)
        SKYBLUE3 = self.RGB(108, 166, 205)
        SKYBLUE4 = self.RGB(74, 112, 139)
        SLATEBLUE = self.RGB(106, 90, 205)
        SLATEBLUE1 = self.RGB(131, 111, 255)
        SLATEBLUE2 = self.RGB(122, 103, 238)
        SLATEBLUE3 = self.RGB(105, 89, 205)
        SLATEBLUE4 = self.RGB(71, 60, 139)
        SLATEGRAY = self.RGB(112, 128, 144)
        SLATEGRAY1 = self.RGB(198, 226, 255)
        SLATEGRAY2 = self.RGB(185, 211, 238)
        SLATEGRAY3 = self.RGB(159, 182, 205)
        SLATEGRAY4 = self.RGB(108, 123, 139)
        SNOW1 = self.RGB(255, 250, 250)
        SNOW2 = self.RGB(238, 233, 233)
        SNOW3 = self.RGB(205, 201, 201)
        SNOW4 = self.RGB(139, 137, 137)
        SPRINGGREEN = self.RGB(0, 255, 127)
        SPRINGGREEN1 = self.RGB(0, 238, 118)
        SPRINGGREEN2 = self.RGB(0, 205, 102)
        SPRINGGREEN3 = self.RGB(0, 139, 69)
        STEELBLUE = self.RGB(70, 130, 180)
        STEELBLUE1 = self.RGB(99, 184, 255)
        STEELBLUE2 = self.RGB(92, 172, 238)
        STEELBLUE3 = self.RGB(79, 148, 205)
        STEELBLUE4 = self.RGB(54, 100, 139)
        TAN = self.RGB(210, 180, 140)
        TAN1 = self.RGB(255, 165, 79)
        TAN2 = self.RGB(238, 154, 73)
        TAN3 = self.RGB(205, 133, 63)
        TAN4 = self.RGB(139, 90, 43)
        TEAL = self.RGB(0, 128, 128)
        THISTLE = self.RGB(216, 191, 216)
        THISTLE1 = self.RGB(255, 225, 255)
        THISTLE2 = self.RGB(238, 210, 238)
        THISTLE3 = self.RGB(205, 181, 205)
        THISTLE4 = self.RGB(139, 123, 139)
        TOMATO1 = self.RGB(255, 99, 71)
        TOMATO2 = self.RGB(238, 92, 66)
        TOMATO3 = self.RGB(205, 79, 57)
        TOMATO4 = self.RGB(139, 54, 38)
        TURQUOISE = self.RGB(64, 224, 208)
        TURQUOISE1 = self.RGB(0, 245, 255)
        TURQUOISE2 = self.RGB(0, 229, 238)
        TURQUOISE3 = self.RGB(0, 197, 205)
        TURQUOISE4 = self.RGB(0, 134, 139)
        TURQUOISEBLUE = self.RGB(0, 199, 140)
        VIOLET = self.RGB(238, 130, 238)
        VIOLETRED = self.RGB(208, 32, 144)
        VIOLETRED1 = self.RGB(255, 62, 150)
        VIOLETRED2 = self.RGB(238, 58, 140)
        VIOLETRED3 = self.RGB(205, 50, 120)
        VIOLETRED4 = self.RGB(139, 34, 82)
        WARMGREY = self.RGB(128, 128, 105)
        WHEAT = self.RGB(245, 222, 179)
        WHEAT1 = self.RGB(255, 231, 186)
        WHEAT2 = self.RGB(238, 216, 174)
        WHEAT3 = self.RGB(205, 186, 150)
        WHEAT4 = self.RGB(139, 126, 102)
        WHITE = self.RGB(255, 255, 255)
        WHITESMOKE = self.RGB(245, 245, 245)
        WHITESMOKE = self.RGB(245, 245, 245)
        YELLOW1 = self.RGB(255, 255, 0)
        YELLOW2 = self.RGB(238, 238, 0)
        YELLOW3 = self.RGB(205, 205, 0)
        YELLOW4 = self.RGB(139, 139, 0)

        dict_containing_variables = locals()
        del dict_containing_variables['self']

        return dict_containing_variables # <= NOTE Return a dictionary containing the current scope's local variables.

    class RGB(namedtuple(typename='RGB', field_names='red, green, blue')):
        ''' Provide RGB color constants and a colors dictionary with elements formatted '''
        def __init__(self, red: int=0, green: int=0, blue: int=0): # DESC => initialize constructor
            """Initialize the RGB object with red, green, and blue values."""

        def rgb_format(self) -> tuple: # DESC => RGB format
            """Returns the color in RGB format.

            Returns:
                str: The color in RGB format.

            Example:
            ```python
                color = ColorsConstants.RGB(240, 248, 255)
                rgb = color.rgb_format()
                print(rgb)  # Output: '(240, 248, 255)'
            ```
            """
            # return '({:d}, {:d}, {:d})'.format(self.red, self.green, self.blue)
            return (self.red, self.green, self.blue)

        def hex_format(self) -> str: # DESC => hex format
            """Returns the color in hexadecimal format.

            Returns:
                str: The color in hexadecimal format.

            Example:
            ```python
                color = ColorsConstants.RGB(240, 248, 255)
                hex_value = color.hex_format()
                print(hex_value)  # Output: '#F0F8FF'
            ```
            """
            return '#{:02X}{:02X}{:02X}'.format(self.red, self.green, self.blue)

class ColorsConvartor:
    """Color converter class for different color formats."""
    def __init__(self): # DESC => initialize constructor
        """Initialize the ColorsConvartor object.
        """
        super(ColorsConvartor, self).__init__()

    def cmyk_to_rgb(self, cyan: float=0, magenta: float=0, yellow: float=0, black: float=0): # DESC => convert CMYK to RGB format
        """Convert CMYK color to RGB format.

        Args:
            `cyan` (float, optional): Cyan component (0-100). Defaults to 0.
            `magenta` (float, optional): Magenta component (0-100). Defaults to 0.
            `yellow` (float, optional): Yellow component (0-100). Defaults to 0.
            `black` (float, optional): Black component (0-100). Defaults to 0.

        Returns:
            tuple: RGB color tuple (red, green, blue).

        Example:
        ```python
            converter = ColorsConverter()
            rgb = converter.cmyk_to_rgb(cyan=50, magenta=30, yellow=10, black=0)
            print(rgb)  # Output: (159, 191, 217)
        ```
        """
        RGB_SCALE = 255
        CMYK_SCALE = 100

        red     = int(RGB_SCALE * (1 - cyan / CMYK_SCALE) * (1 - black / CMYK_SCALE))
        green   = int(RGB_SCALE * (1 - magenta / CMYK_SCALE) * (1 - black / CMYK_SCALE))
        blue    = int(RGB_SCALE * (1 - yellow / CMYK_SCALE) * (1 - black / CMYK_SCALE))
        return red, green, blue

    def rgb_to_cmyk(self, red: int=0, green: int=0, blue: int=0): # DESC => convert RGB to CMYK format
        """Convert RGB color to CMYK format.

        Args:
            `red` (int, optional): Red component (0-255).
            `green` (int, optional): Green component (0-255).
            `blue` (int, optional): Blue component (0-255).

        Returns:
            tuple: CMYK color tuple (cyan, magenta, yellow, black).

        Example:
        ```python
            converter = ColorsConverter()
            cmyk = converter.rgb_to_cmyk(red=159, green=191, blue=217)
            print(cmyk)  # Output: (26.667, 12.084, 0.0, 15.686)
        ```
        """
        RGB_SCALE = 255
        CMYK_SCALE = 100

        # DESC => extract out k [0, 1]
        max_rgb = 1 - (max(red, green, blue) / RGB_SCALE)
        c = (1 - red / RGB_SCALE - max_rgb) / (1 - max_rgb)
        m = (1 - green / RGB_SCALE - max_rgb) / (1 - max_rgb)
        y = (1 - blue / RGB_SCALE - max_rgb) / (1 - max_rgb)
        k = max_rgb

        # DESC => rescale to the range [0,CMYK_SCALE]
        cyan, magenta, yellow, black = (round(c * CMYK_SCALE, 2), round(m * CMYK_SCALE, 2), round(y * CMYK_SCALE, 2), round(k * CMYK_SCALE, 2))
        return cyan, magenta, yellow, black


    def rgb_to_hex(self, red: int=0, green: int=0, blue: int=0): # DESC => convert RGB to HEX format
        """Convert RGB color to hexadecimal format.

        Args:
            `red` (int, optional): Red component (0-255).
            `green` (int, optional): Green component (0-255).
            `blue` (int, optional): Blue component (0-255).

        Returns:
            str: Color in hexadecimal format.

        Example:
        ```python
            converter = ColorsConverter()
            hex_value = converter.rgb_to_hex(red=159, green=191, blue=217)
            print(hex_value)  # Output: '#9FBFD9'
        ```
        """
        return '#{:02X}{:02X}{:02X}'.format(red, green, blue)

    def hex_to_rgb(self, hex): # DESC => convert HEX to RGB format
        """Convert hexadecimal color to RGB format.

        Args:
            `hex_value` (str): Color in hexadecimal format.

        Returns:
            tuple: RGB color tuple (red, green, blue).

        Example:
        ```python
            converter = ColorsConverter()
            rgb = converter.hex_to_rgb('#9FBFD9')
            print(rgb)  # Output: (159, 191, 217)
        ```
        """
        hex = hex.lstrip('#')
        return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))


    def rgb_to_hls(self, red: int=0, green: int=0, blue: int=0): # DESC => convert RGB to HLS format
        """Convert RGB color to HLS format.

        Args:
            `red` (int, optional): Red component (0-255).
            `green` (int, optional): Green component (0-255).
            `blue` (int, optional): Blue component (0-255).

        Returns:
            tuple: HLS color tuple (hue, lightness, saturation).

        Example:
        ```python
            converter = ColorsConverter()
            hls = converter.rgb_to_hls(red=159, green=191, blue=217)
            print(hls)  # Output: (0.58, 0.669, 0.389)
        ```
        """
        hue, lightness, saturation = colorsys.rgb_to_hls(r=(red/255.0), g=(green/255.0), b=(blue/255.0))
        return (round(hue, 3), round(lightness, 3), round(saturation, 3))

    def hls_to_rgb(self, hue: float=0, lightness: float=0, saturation: float=0): # DESC => convert HLS to RGB format
        """Convert HLS color to RGB format.

        Args:
            `hue` (float, optional): Hue component (0-1).
            `lightness` (float, optional): Hue component (0-1).
            `saturation` (float, optional): Saturation component (0-1).

        Returns:
            tuple: RGB color tuple (red, green, blue).

        Example:
        ```python
            converter = ColorsConverter()
            rgb = converter.hls_to_rgb(hue=0.58, lightness=0.669, saturation=0.389)
            print(rgb)  # Output: (159, 191, 217)
        ```
        """
        red, green, bleu = colorsys.hls_to_rgb(h=hue, l=lightness, s=saturation)
        return (int(red*255), int(green*255), int(bleu*255))

class Promise:
    """A simplified implementation of promises in Python."""
    def __init__(self, executor: Callable[[Callable, Callable], None]) -> None: # DESC => initialize constructor
        """Initializes a new Promise object.

        Args:
            `executor` (Callable[[Callable[[Any], None], Callable[[Exception], None]], None]):
                A function that takes two arguments, `resolve` and `reject`.
                It performs an asynchronous operation and calls `resolve` with the result
                or `reject` with an error if the operation fails.
        Example:
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

        Notes:
            - This implementation of promises follows a simplified approach and may not cover all the features of full-fledged promise libraries.
            - Promises can be useful for handling asynchronous operations and managing their outcomes in a more structured manner.
        """
        super(Promise, self).__init__()
        # DESC => Initialize the state variables attribute
        self.resolved = False
        self.rejected = False
        self.result = None
        self.error = None
        self.callbacks = []

        def resolve(value: Any) -> None:
            """Resolves the promise with the given value.

            Args:
                `value` (Any): The resolved value.
            """
            # DESC => Check if the promise is not already resolved or rejected
            if not self.resolved and not self.rejected:
                self.resolved = True
                self.result = value
                # DESC => Execute all the registered callback functions
                for callback in self.callbacks:
                    callback(self.result)

        def reject(error: Exception) -> None:
            """Rejects the promise with the given error.

            Args:
                `error` (Any): The error object.
            """
            # DESC => Check if the promise is not already resolved or rejected
            if not self.resolved and not self.rejected:
                self.rejected = True
                self.error = error
                # DESC => Execute all the registered callback functions
                for callback in self.callbacks:
                    callback(self.error)

        try:
            # DESC => Execute the provided executor function
            executor(resolve, reject)
        except Exception as error:
            # DESC => If an exception occurs, reject the promise with the error
            reject(error)

    def then(self, on_fulfilled: Callable[[Any], None]) -> 'Promise':
        """Attaches a callback function to the promise for fulfillment.

        Args:
            `on_fulfilled` (Callable[[Any], None]):
                A function that takes the fulfilled value as an argument and performs further actions.

        Returns:
            Promise: A new Promise object.
        
        Example:
        ```python
            # Example usage of the then() method
            promise.then(lambda result: print("Promise resolved with result:", result))
        ```
        """
        # DESC => If promise is already resolved, execute the on_fulfilled callback immediately
        if self.resolved:
            on_fulfilled(self.result)
        else:
            # DESC => Otherwise, add the on_fulfilled callback to the list of callbacks
            self.callbacks.append(on_fulfilled)
        return self

    def catch(self, on_rejected: Callable[[Exception], None]) -> 'Promise':
        """Attaches a callback function to the promise for rejection.

        Args:
            `on_rejected` (Callable[[Exception], None]):
                A function that takes the rejected error as an argument and handles the error.

        Returns:
            Promise: The Promise object itself.

        Example:
        ```python
            # Example usage of the catch() method
            promise.catch(lambda error: print("Promise rejected with error:", error))
        ```
        """
        # DESC => If promise is already rejected, execute the on_rejected callback immediately
        if self.rejected:
            on_rejected(self.error)
        else:
            # DESC => Otherwise, add the on_rejected callback to the list of callbacks
            self.callbacks.append(on_rejected)
        return self

    @staticmethod
    def executor(function: Callable[..., Any], args: tuple) -> 'Promise':
        """Creates a new promise using an executor function.

        Args:
            `function` (Callable): The function to execute asynchronously
            `args` (tuple): The arguments to pass to the function.

        Returns:
            Promise: A Promise instance that represents the asynchronous operation.
        """
        # DESC => Define the executor_function that will be passed to the Promise constructor
        def executor_function(resolve: Callable[[Any], None], reject: Callable[[Exception], None]) -> None:
            try:
                # DESC => Execute the provided function with the given arguments
                result = function(*args)
                # DESC => Resolve the promise with the result
                resolve(result)
            except Exception as error:
                # DESC => If an exception occurs, reject the promise with the error
                reject(error)
        return Promise(executor_function)

class ExceptionsBase:
    """Class that defines variables for built-in exceptions derived from BaseException.

    Notes:
        - Access the exception classes directly using the class name followed by the exception variable name.
            For example, EXCEPTIONS.BASE_EXCEPTION represents the BaseException class.
        - Exception variables can be used for handling specific exception types or for type hinting purposes.

    Example:
    ```python
        try:
            # Some code that may raise an exception
        except EXCEPTIONS.ZERO_DIVISION_ERROR as e:
            # Handle ZeroDivisionError

        def my_function() -> EXCEPTIONS.TYPE_ERROR:
            # Function annotation indicating that the return type should be TypeError
    ```
    """

    BASE_EXCEPTION = BaseException
    """The base class for all built-in exceptions."""

    SYSTEM_EXIT = SystemExit
    """This exception is raised by the sys.exit() function."""

    KEYBOARD_INTERRUPT = KeyboardInterrupt
    """This exception is raised when the user interrupts program execution, usually by pressing Ctrl+C."""

    GENERATOR_EXIT = GeneratorExit
    """This exception is raised when a generator is closed."""

    EXCEPTION = Exception
    """The most general exception class. All built-in, non-system-exiting exceptions are derived from this class."""

    STOP_ITERATION = StopIteration
    """Raised by built-in functions like next() and an iterator's __next__() method to signal the end of iteration."""

    STOP_ASYNC_ITERATION = StopAsyncIteration
    """Raised by a coroutine object's __anext__() method to signal the end of asynchronous iteration."""

    ARITHMETIC_ERROR = ArithmeticError
    """The base class for arithmetic errors."""

    FLOATING_POINT_ERROR = FloatingPointError
    """Raised when a floating-point operation fails."""

    OVERFLOW_ERROR = OverflowError
    """Raised when the result of an arithmetic operation is too large to be expressed as a Python integer."""

    ZERO_DIVISION_ERROR = ZeroDivisionError
    """Raised when division or modulo by zero occurs."""

    ASSERTION_ERROR = AssertionError
    """Raised when an assert statement fails."""

    ATTRIBUTE_ERROR = AttributeError
    """Raised when an attribute reference or assignment fails."""

    BUFFER_ERROR = BufferError
    """Raised when a buffer-related operation cannot be performed."""

    EOF_ERROR = EOFError
    """Raised when there is no input from either the input() function or readline() method of file objects."""

    IMPORT_ERROR = ImportError
    """Raised when an import statement fails to find the module definition or when a from ... import fails."""

    MODULE_NOT_FOUND_ERROR = ModuleNotFoundError
    """Raised when a module could not be found during an import statement."""

    LOOKUP_ERROR = LookupError
    """The base class for lookup errors."""

    INDEX_ERROR = IndexError
    """Raised when a sequence subscript is out of range."""

    KEY_ERROR = KeyError
    """Raised when a mapping (dictionary) key is not found in the set of existing keys."""

    MEMORY_ERROR = MemoryError
    """Raised when an operation runs out of memory."""

    NAME_ERROR = NameError
    """Raised when a local or global name is not found."""

    UNBOUND_LOCAL_ERROR = UnboundLocalError
    """Raised when trying to access a local variable in a function or method that has not been assigned a value."""

    RECURSION_ERROR = RecursionError
    """Raised when the maximum recursion depth is exceeded."""

    SYSTEM_ERROR = SystemError
    """A generic error raised when a C/C++ exception is thrown but not caught."""

    TypeError = TypeError
    """Raised when an operation or function is applied to an object of inappropriate type."""

    ValueError = ValueError
    """Raised when an operation or function receives an argument of the correct type but an inappropriate value."""

    UnicodeError = UnicodeError
    """The base class for Unicode-related errors."""

    UnicodeDecodeError = UnicodeDecodeError
    """Raised when a Unicode-related error occurs during decoding."""

    UnicodeEncodeError = UnicodeEncodeError
    """Raised when a Unicode-related error occurs during encoding."""

    UnicodeTranslateError = UnicodeTranslateError
    """Raised when a Unicode-related error occurs during translation."""

    RuntimeError = RuntimeError
    """The base class for runtime errors."""

    NotImplementedError = NotImplementedError
    """Raised when an abstract method that should be implemented in a subclass is not actually implemented."""

    # Notes: For Python versions before 3.10, uncomment the following line
    # OS_ERROR = OSError
    """The base class for OS-related errors. (Notes: Uncomment this line for Python versions before 3.10)"""

    BLOCKING_IO_ERROR = BlockingIOError
    """Raised when an I/O operation is interrupted by a signal."""

    CHILD_PROCESS_ERROR = ChildProcessError
    """Raised when an operation on a child process fails."""

    CONNECTION_ERROR = ConnectionError
    """The base class for connection-related errors."""

    BROKEN_PIPE_ERROR = BrokenPipeError
    """Raised when a pipe is broken or disconnected by a reader process."""

    CONNECTION_ABORTED_ERROR = ConnectionAbortedError
    """Raised when a connection attempt is aborted by the network."""

    CONNECTION_REFUSED_ERROR = ConnectionRefusedError
    """Raised when a connection attempt is refused by the network."""

    CONNECTION_RESET_ERROR = ConnectionResetError
    """Raised when a connection is reset by the peer."""

    FILE_EXISTS_ERROR = FileExistsError
    """Raised when trying to create a file or directory that already exists."""

    FILE_NOT_FOUND_ERROR = FileNotFoundError
    """Raised when a file or directory is requested but cannot be found."""

    INTERRUPTED_ERROR = InterruptedError
    """Raised when an operation is interrupted by a signal."""

    IS_A_DIRECTORY_ERROR = IsADirectoryError
    """Raised when a directory is expected, but a file is found instead."""

    NOT_A_DIRECTORY_ERROR = NotADirectoryError
    """Raised when a directory is expected, but a non-directory object is found instead."""

    PERMISSION_ERROR = PermissionError
    """Raised when trying to perform an operation without the required permissions."""

    PROCESS_LOOKUP_ERROR = ProcessLookupError
    """Raised when a process with the given process ID (PID) cannot be found."""

    TIMEOUT_ERROR = TimeoutError
    """Raised when an operation times out."""

    REFERENCE_ERROR = ReferenceError
    """Raised when a weak reference object is used after the referred object has been deleted."""

    SYNTAX_ERROR = SyntaxError
    """Raised when there is a syntax error in Python code."""

    INDENTATION_ERROR = IndentationError
    """Raised when there is an indentation-related syntax error in Python code."""

    TAB_ERROR = TabError
    """Raised when indentation contains inconsistent use of tabs and spaces."""

    SYSTEM_ERROR = SystemError
    """A generic error raised when a C/C++ exception is thrown but not caught."""

    TYPE_ERROR = TypeError
    """Raised when an operation or function is applied to an object of inappropriate type."""

    VALUE_ERROR = ValueError
    """Raised when an operation or function receives an argument of the correct type but an inappropriate value."""

    UNICODE_ERROR = UnicodeError
    """The base class for Unicode-related errors."""

    UNICODE_DECODE_ERROR = UnicodeDecodeError
    """Raised when a Unicode-related error occurs during decoding."""

    UNICODE_ENCODE_ERROR = UnicodeEncodeError
    """Raised when a Unicode-related error occurs during encoding."""

    UNICODE_TRANSLATE_ERROR = UnicodeTranslateError
    """Raised when a Unicode-related error occurs during translation."""

    WARNING = Warning
    """The base class for warning categories."""

    DEPRECATION_WARNING = DeprecationWarning
    """A warning category used for deprecated features that will be removed in future versions."""

    PENDING_DEPRECATION_WARNING = PendingDeprecationWarning
    """A warning category used for features that are still considered deprecated but will be deprecated in the future."""

    RUNTIME_WARNING = RuntimeWarning
    """A warning category used for questionable runtime behavior."""

    SYNTAX_WARNING = SyntaxWarning
    """A warning category used for questionable syntax usage."""

    USER_WARNING = UserWarning
    """A warning category used for user-defined warnings."""

    FUTURE_WARNING = FutureWarning
    """A warning category used for warnings about features that will change in future versions."""

    IMPORT_WARNING = ImportWarning
    """A warning category used for warnings related to import statements."""

    UNICODE_WARNING = UnicodeWarning
    """A warning category used for warnings related to Unicode."""

    BYTES_WARNING = BytesWarning
    """A warning category used for warnings related to bytes and bytearray."""

    RESOURCE_WARNING = ResourceWarning
    """A warning category used for warnings related to resource usage."""

class Argparse(ArgumentParser):
    """Argparse - Extended Argument Parser for Command-Line Argument Handling. """
    def __init__(self, 
        prog: Optional[Union[str, Any]] = None,
        usage: Optional[str] = None,
        description: Optional[str] = None,
        epilog: Optional[str] = None,
        prefix_chars: Optional[str] = '-',
        argument_default=None,
        conflict_handler: Optional[str] = 'error',
        add_help: bool = True,
        allow_abbrev: bool = True,
        exit_on_error: bool = True): # DESC => initialize constructor.
        """Initialize the Argparse object.

        Args:
            `prog` (Optional[Union[str, Any]], optional): The name of the program.
                    Defaults to sys.argv[0]. Example ('myprogram')
            `usage` (Optional[str], optional): A usage to customize the usage message that is displayed.
                    Defaults to None to auto-generated from arguments. Example (`'%(prog)s [options] <input>'`)
            `description` (Optional[str], optional): A description of what the program does.
                    Defaults to None.
            `epilog` (Optional[str], optional): Text following the argument descriptions.
                    to add additional text at the end of the help message.
                    Defaults to None. Example ('Additional information goes here')
            `prefix_chars` (Optional[str], optional): By default, argparse recognizes options
                    with either a single dash (`-`) or double dash (`--`) prefix. Defaults to '-'.
            `argument_default` (_type_, optional): The default value for all arguments.
                    Defaults to None.
            `conflict_handler` (Optional[str], optional): String indicating how to handle conflicts.
                    Defaults to 'error'.
            `add_help` (bool, optional): Add automatically adds a `-h` / `--help` option
                    to display the help message. Defaults to True.
            `allow_abbrev` (bool, optional): By default, allows long option names abbreviations.
                    Setting to False disables this behavior, requiring users to provide the full option names. Defaults to True.
            `exit_on_error` (bool, optional): Determines whether or not ArgumentParser exits.
                    with error info when an error occurs. Defaults to True.

        Example:
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

        Notes:
            - This class extends the `ArgumentParser` class from the `argparse` module and provides additional functionality for handling command-line arguments.
        """
        super(Argparse, self).__init__(prog=prog, usage=usage, description=description, epilog=epilog,  
            prefix_chars=prefix_chars, argument_default=argument_default, conflict_handler=conflict_handler, 
            add_help=add_help, allow_abbrev=allow_abbrev, exit_on_error=exit_on_error)
        # DESC => Initialize the state variables attribute
        self.args_group = self.add_argument_group('Argument Options') # DESC => Initialize the argument group

    def add_args(self, 
        *name_or_flags: str, 
        arg_type: Optional[Union[str, int, float, bool, dir, argparse.FileType]] = ..., 
        choices: Optional[Iterable] = None,
        action: Optional[str] = ..., 
        default: Optional[Any] = ..., 
        nargs: Optional[Union[int, Literal['?', '*', '+']]] = None, 
        help_message: str = None):
        """Add command-line arguments to the argument group.

        Args:
            `name_or_flags` (tuple[str, ...]):The name or flags for the argument.
                    You can use positional Example (`'name'`) or optional arguments 
                    Example (`'-h'`, `'--help'`).

            `arg_type` (Optional[Union[str, int, float, bool]], optional): Automatically convert an argument 
                        to the given type of input Here's a list
                        `str` (default): Accepts any string value.
                        `int`: Accepts an integer value.
                        `float`: Accepts a floating-point value.
                        `bool`: Accepts a boolean value.
                            This type is typically used for flags or options that don't require a value.
                        `dir`: Accepts a directory path.
                        `argparse.FileType`: Accepts a file path.
                            It can automatically open the file for reading or writing, depending on 
                            the specified mode ex: (`argparse.FileType('r')`).

            `choices` (Optional[Iterable], optional): The should a list, tuple, set, of acceptable
                        choices for the argument. Accepts one of the specified choices.
                        ex choices=['a', 'b', 'c'].

            `action` (Optional[str], optional): The action to be taken when the argument is encountered.
                        Here's a list of commonly used action types
                        `'store'` (default): Stores the value specified for the argument.
                            This is the default action if no action is specified.
                        `'store_const`': Stores a constant value specified
                            by the const parameter when the argument is encountered.
                        `'store_true'`/`'store_false'`: Stores True or False respectively when
                            the argument is encountered. These actions are typically used for boolean flags.
                        `'append'`: Appends the value specified for the argument to a list.
                            This allows you to collect multiple occurrences of the argument.
                        `'append_const'`: Appends a constant value specified by the const parameter
                            to a list when the argument is encountered.
                        `'count'`: Counts the number of times the argument is encountered
                            and stores the count.
                        `'help'`: Displays the help message and exits the program.

            `default` (Optional[Any], optional): The default value for the argument.
                        you can set default values for command-line arguments
                        Here's a list of ways to specify default values.

            `nargs` (Optional[Any], optional): The allows you to specify the number of command line arguments.
                        that should be consumed for a given option. Here are some possible values
                        `None` (default): This is the default value when nargs is not specified explicitly.
                            It means that a single command-line argument is expected for the option.
                        `'?'`: Specifies that the option should match zero or one command-line argument.
                            If the option is not provided, the default value for the option will be used.
                        `'*'`: Allows zero or more command-line arguments for the option.
                            All the arguments will be collected into a list.
                        `'+'`: Requires one or more command-line arguments for the option.
                            Like *, the arguments will be collected into a list.
                        `int`: Allows a specific number of command-line arguments to be consumed.
                            For example, nargs=3 means that three arguments are required for the option.
                        `argparse.REMAINDER`: Collects all the remaining command-line arguments into a list,
                            regardless of their number.

            `help_message` (str, optional): The help message for the argument you can provide.
                        help messages for command-line arguments on how to use your script.
        """
        
        kwargs = {
            # 'required': required,
            'type': arg_type,
            'choices': choices,
            'action': action,
            'default': default,
            'nargs': nargs,
            'help': help_message,
            # 'dest': dest
        }

        self.args_group.add_argument(*name_or_flags, **kwargs)

    def get_args_namespace(self):
        """Parse the command-line arguments and return the namespace.

        Returns:
            Namespace: The parsed command-line arguments as a namespace.
        """
        # DESC => get the argparse and convert to a namespace.
        self.args_namespace = self.parse_args()
        return self.args_namespace

    def get_args_dictionary(self):
        """Parse the command-line arguments and return a dictionary.

        Returns:
            dict: The parsed command-line arguments as a dictionary.
        """
        # DESC => get the argparse the namespace and convert to a dictionary.
        self.args_dictionary = dict(self.get_args_namespace().__dict__)
        return self.args_dictionary

class EventsSignature:
    """EventsSignature class."""
    def __init__(self):
        """Initialize the EventsSignature object.
        
        The EventsSignature class is used to set and get attributes, and signature the callback object function and init event.

        Methods:
            `setattribute(attribute_name: str, value: Any)`: 
                Sets the named attribute of the object to the specified value.
            `getattribute(attribute_name: str)`: 
                Get a named attribute from object.
            `signature_obj_and_init_callback(callback: Callable, init_event: Any = None)`: 
                Signature of callback the object function and init event.

        Example:
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
        """
        self.init = None

    # DESC => the initialize method inside the class.
    @staticmethod
    def setattribute(attribute_name: str, value: Any):
        """Sets the named attribute of the object to the specified value.

        Args:
            `attribute_name` (str): The name of the attribute.
            `value` (Any): The value of the attribute.

        Returns:
            None
        """
        setattr(EventsSignature, attribute_name, value)
    
    @staticmethod
    def getattribute(attribute_name: str):
        """Get a named attribute from object.

        Args:
            `attribute_name` (str): The name of the attribute.
        
        Returns:
            value: the value of attribute.
        """
        return getattr(EventsSignature, attribute_name)

    @staticmethod
    def signature_obj_and_init_callback(callback: Callable, init_event: Any = None):
        """Signature of callback the object function and init event.

        Args:
            `callback` (Callable): The represent any callable object, such as a function,
                a method, or a lambda expression.
            `event` (Any, EventsSignature): The send Events data to callback object. Defaults to None.
        """
        sig = inspect.signature(callback) # DESC => Get the signature of the function.
        params = [param.name for param in sig.parameters.values()] # DESC => Convert the signature to a list of strings
        
        if "event" in params:
            callback.__call__(event=init_event)
        elif "e" in params:
            callback.__call__(e=init_event)
        elif "_" in params:
            callback.__call__(_=init_event)
        else:
            callback.__call__()

class AxisCalc:
    """Calculate the top, bottom, right, and left coordinates of an object based on its axis."""
    def __init__(self, 
        local_x: Union[int, float] = None, 
        local_y: Union[int, float] = None, 
        global_x: Union[int, float] = None, 
        global_y: Union[int, float] = None): # DESC => initialize constructor.
        """Initialize the AxisCalc object.

        Args:
            `local_x` (Union[int, float]): The axis local x-coordinate of the object.
            `local_y` (Union[int, float]): The axis local y-coordinate of the object.
            `global_x` (Union[int, float]): The axis global x-coordinate of the object.
            `global_y` (Union[int, float]): The axis global y-coordinate of the object.

        Methods:
            `calculate_top_bottom_right_left_of_local_global()`: 
                Calculate the top, bottom, right, and left of an object given its local and global coordinates.
            `calculate_top_bottom_right_left_of_global()`: 
                Calculate the top, bottom, right, and left of an object given its global coordinates.
            `calculate_top_bottom_right_left_of_local()`: 
                Calculate the top, bottom, right, and left of an object given its local coordinates.

        """
        # DESC => Initialize the state variables attribute.
        self.local_x = local_x
        self.local_y = local_y
        self.global_x = global_x
        self.global_y = global_y

    def calculate_top_bottom_right_left_of_local_global(self):
        """Calculate the top, bottom, right, and left of an object given its local and global coordinates.

        Returns:
            `top` (float): The top coordinate of the object.
            `bottom` (float): The bottom coordinate of the object.
            `right` (float): The right coordinate of the object.
            `left` (float): The left coordinate of the object.
        """

        try:
            top = float(self.global_y - self.local_y)
            bottom = float(top + self.local_y)
            right = float(self.global_x + self.local_x)
            left = float(right - self.local_x)

            return top, bottom, right, left
        except Exception as error:
            raise Exception(f"Error: {error}")

    def calculate_top_bottom_right_left_of_global(self):
        """Calculate the top, bottom, right, and left of an object given its global coordinates.

        Returns:
            `top` (float): The top coordinate of the object.
            `bottom` (float): The bottom coordinate of the object.
            `right` (float): The right coordinate of the object.
            `left` (float): The left coordinate of the object.
        """
        try:
            top = float(self.global_y)
            bottom = float(top + 1)
            right = float(self.global_x + 1)
            left = float(right - 1)

            return top, bottom, right, left
        except Exception as error:
            raise Exception(f"Error: {error}")

    def calculate_top_bottom_right_left_of_local(self):
        """Calculate the top, bottom, right, and left of an object given its local coordinates.

        Returns:
            `top` (float): The top coordinate of the object.
            `bottom` (float): The bottom coordinate of the object.
            `right` (float): The right coordinate of the object.
            `left` (float): The left coordinate of the object.
        """
        try:
            top = float(self.local_y)
            bottom = float(top + 1)
            right = float(self.local_x + 1)
            left = float(right - 1)

            return top, bottom, right, left
        except Exception as error:
            raise Exception(f"Error: {error}")

class GenerateID:
    """A class to generate a unique id"""
    def __init__(self): # DESC => initialize constructor.
        """Initialize the GenerateID object.

        Methods:
            `generate_random_id()`: Generate a unique id random.
            `generate_md5_id()`: Generate a unique id of MD5 hash namespace.
            `generate_sha1_id()`: Generate a unique id of SHA-1 hash namespace.
            `check_name_md5()`: Check id of uuid version 3 the MD5 hash it match name.
            `check_name_sha1()`: Check id of uuid version 5 the SHA-1 hash it match name.

        Example:
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
        """
        # DESC => Initialize the state variables attribute.

    def generate_random_id(self, hex_id: Optional[bool] = None, short_id: Optional[int] = None):
        """Generate a unique id random.

        Args:
            `hex_id` (Optional[bool], optional): Set hexadecimal representation of id. Defaults to None.
            `short_id` (Optional[int], optional): Set short id. Defaults to None.

        Returns:
            str.
        """
        # DESC => Generate a unique id random.
        unique_id = uuid.uuid4()

        if hex_id:
            unique_id = unique_id.hex # DESC => Set hexadecimal representation of id

        if short_id:
            unique_id = str(unique_id)[:short_id] # DESC => Set short id.
        return unique_id

    def generate_md5_id(self, namespace: str):
        """Generate a unique id of MD5 hash namespace.

        Args:
            `namespace` (str): Set any name for generate id to same name.

        Returns:
            UUID.
        """
        # DESC => Generate a unique id of MD5 hash.
        return uuid.uuid3(namespace=uuid.NAMESPACE_DNS, name=namespace)

    def generate_sha1_id(self, namespace: str):
        """Generate a unique id of SHA-1 hash namespace.

        Args:
            `namespace` (str): Set any name for generate id to same name.

        Returns:
            UUID.
        """
        # DESC => Generate a unique id of SHA-1 hash.
        return uuid.uuid5(namespace=uuid.NAMESPACE_DNS, name=namespace)

    def check_name_md5(self, namespace: str, md5: uuid.UUID):
        """Check id of uuid version 3 the MD5 hash it match name.

        Args:
            `namespace` (str): The name to checke a match.
            `md5` (Optional[uuid.UUID, str]): The id of uuid version 3 to checke a match same name.

        Returns:
            bool: If the provided UUID match, it returns True; otherwise, it returns False.
        """
        if isinstance(md5, uuid.UUID):
            provided_uuid3 = md5
        else:
            provided_uuid3 = uuid.UUID(hex=md5)

        generated_match = uuid.uuid3(namespace=uuid.NAMESPACE_DNS, name=namespace)

        return generated_match == provided_uuid3

    def check_name_sha1(self, namespace: str, sha1: uuid.UUID):
        """Check id of uuid version 5 the SHA-1 hash it match name.

        Args:
            `namespace` (str): The name to checke a match.
            `sha1` (Optional[uuid.UUID, str]): The id of uuid version 5 to checke a match same name.

        Returns:
            bool: If the provided UUID match, it returns True; otherwise, it returns False.
        """
        if isinstance(sha1, uuid.UUID):
            provided_uuid5 = sha1
        else:
            provided_uuid5 = uuid.UUID(hex=sha1)

        generated_match = uuid.uuid5(namespace=uuid.NAMESPACE_DNS, name=namespace)

        return generated_match == provided_uuid5

class AttrRegisterMap:
    """A class AttrRegisterMap the attributes register and manages map.

    Methods:
        `setattribute`(attribute_name: str, value: Any, attribute_update: bool = True): Sets the named attribute of the object to the specified value.
        `getattribute`(attribute_name: str): Gets the named attribute from object.

    Example:
    ```python
        # DESC => Set attributes.
        AttrRegisterMap.setattribute(attribute_name="Main", value={'control': self, 'locals': locals()})
        
        print(AttrRegisterMap.getattribute("Main"))
        # DESC => {'control': self, 'locals': locals()}
    ```

    Notes:
        - `setattribute`: This for set attribute object to the specified value. 
            if attribute exists and attributeis whether (Dict or List or Tuple or Set) 
            and `attribute_update` is True it add a new values to attribute object.
    """
    ATTRIBUTE_MAP = None

    # DESC => the initialize method inside the class.
    @staticmethod
    def setattribute(attribute_name: str, value: Any, attribute_update: bool = True):
        """Sets the named attribute of the object to the specified value.

        Args:
            `attribute_name` (str): The name of the attribute.
            `value` (Any): The value of the attribute.
            `attribute_update` (bool): if whether True it add a new values to attribute object.
                of type (Dict or List or Tuple or Set).

        Returns:
            None
            
        Notes:
            - `setattribute`: This for set attribute object to the specified value. 
                if attribute exists and attributeis whether (Dict or List or Tuple or Set) 
                and `attribute_update` is True it add a new values to attribute object.
        """
        # DESC => Check if attribute of attribute_name not available in class AttrRegisterMap.
        if not hasattr(AttrRegisterMap, attribute_name):
            setattr(AttrRegisterMap, attribute_name, value)
        else:
            # print(f"Attribute: '{attribute_name}' already exists in AttrRegisterMap.!")
            if attribute_update:
                if isinstance(AttrRegisterMap.getattribute(attribute_name), Dict):
                    # DESC => Add a new name and value to the Dictionary.
                    AttrRegisterMap.getattribute(attribute_name).update(value)
                elif isinstance(AttrRegisterMap.getattribute(attribute_name), List):
                    # DESC => Add a new value to the List.
                    AttrRegisterMap.getattribute(attribute_name).extend(value)
                elif isinstance(AttrRegisterMap.getattribute(attribute_name), Tuple):
                    # DESC => Add a new value to the Tuple.
                    updated_tuple = AttrRegisterMap.getattribute(attribute_name) + value
                    setattr(AttrRegisterMap, attribute_name, updated_tuple)
                elif isinstance(AttrRegisterMap.getattribute(attribute_name), Set):
                    # DESC => Add a new value to the Set.
                    if isinstance(value, Set):
                        AttrRegisterMap.getattribute(attribute_name).update(value)
                    else:
                        AttrRegisterMap.getattribute(attribute_name).add(value)
                else:
                    setattr(AttrRegisterMap, attribute_name, value)
            else:
                setattr(AttrRegisterMap, attribute_name, value)
    
    @staticmethod
    def getattribute(attribute_name: str):
        """Get a named attribute from object.

        Args:
            `attribute_name` (str): The name of the attribute.
        
        Returns:
            Any: The returns value of attribute.
        """
        assert hasattr(AttrRegisterMap, attribute_name), f"Attribute '{attribute_name}' does not exist."
        return getattr(AttrRegisterMap, attribute_name)


