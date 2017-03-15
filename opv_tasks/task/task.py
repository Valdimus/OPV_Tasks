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
# Description: Abstract class for representing task, you must redefine the run methods.

import sys
import subprocess


class Task:
    """An abstract class, you must redefine the run method."""

    def __init__(self, client_requestor, opv_directorymanager_client):
        """
        Create a task.

        :param client_requestor: the client requestor to use for the task
        :param opv_directorymanager_client: The client directory manager to use
        """
        self._client_requestor = client_requestor
        self._opv_directory_manager = opv_directorymanager_client

    def run(self, options={}):
        """
        Run the task.

        :param options: Options to use
        :return:
        :raise
        """
        raise NotImplementedError

    def _run_cli(self, cmd, args=[], stdout=sys.stdout, stderr=subprocess.STDOUT):
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
