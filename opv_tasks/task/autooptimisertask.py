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

# Contributors: Benjamin BERNARD <benjamin.bernard@openpathview.fr>
# Email: team@openpathview.fr
# Description: Optimise CP geometrie.

import os
import logging
import json
from path import Path
from shutil import copyfile

from opv_tasks.const import Const
from opv_tasks.task import Task


class AutooptimiserTask(Task):
    """Optimise CP with cli autooptimiser."""

    AUTOOPTIMISER_OPTIONS = ["-a", "-m", "-l", "-s"]
    TMP_PTONAME = "opt.pto"
    TMP_OUTPUT = "out.pto"

    def optimise(self):
        """Optimise CP."""
        with self._opv_directory_manager.Open(self.cp.pto_dir) as (_, pto_dirpath):
            proj_pto = Path(pto_dirpath) / Const.CP_PTO_FILENAME

            with self._opv_directory_manager.Open(self.cp.lot.pictures_path) as (_, pictures_dir):
                local_tmp_pto = Path(pictures_dir) / self.TMP_PTONAME
                local_tmp_output = Path(pictures_dir) / self.TMP_OUTPUT

                logging.debug("Copy pto file " + proj_pto + " -> " + local_tmp_pto)
                copyfile(proj_pto, local_tmp_pto)

                options = list(self.AUTOOPTIMISER_OPTIONS)
                options.append("-o")
                options.append(local_tmp_output)  # Add output
                options.append(local_tmp_pto)  # Add input pto
                logging.debug("Running : " + "autooptimiser" + " ".join(options))
                self._run_cli("autooptimiser", options)
                self.cp.optimized = True

                os.rename(local_tmp_output, proj_pto)  # Copy back optimized verison
                os.unlink(local_tmp_pto)

    def run(self, options={}):
        """Run auto optimiser task."""
        if "id" in options:
            self.cp = self._client_requestor.Cp(options["id"])
            self.optimise()

            self.cp.save()

        return json.dumps({"id": self.cp.id})
