# coding: utf-8

# Copyright (C) 2017 Open Path View, Maison Du Libre
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.

# Contributors: Christophe NOUCHET <christophe.nouchet@openpathview.fr>
# Email: team@openpathview.fr
# Description: Just a little workaround to launch cli command

import sys
import subprocess


def run_cli(cmd, args=[], stdout=sys.stdout, stderr=subprocess.STDOUT):
    """
    Run a command.

    :param cmd: Command to use
    :param args: Args to pass to the command
    :param stdout:
    :param stderr:
    :return: return code of the cli
    """
    my_cmd = cmd if isinstance(cmd, list) else [cmd]
    my_args = args if isinstance(args, list) else [args]
    ret = subprocess.run(my_cmd + my_args, stdout=stdout, stderr=stderr)
    return ret.returncode


def find_task(taskName):
    """Find the atsk with taskName."""
    try:
        moduleTask = __import__("opv_tasks.task.{}task".format(taskName))
        task = getattr(moduleTask, "{}Task".format(taskName.title()))
        return task
    except (ImportError, AttributeError) as e:
        import pprint
        pprint.pprint(e)
        return None  # Task not found
