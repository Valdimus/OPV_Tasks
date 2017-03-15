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
# Description: Find control points using hugin cpfind.

import logging
import os
import json
from shutil import copyfile
from path import Path
from opv_tasks.const import Const

from opv_tasks.task import Task


class CpfindTask(Task):
    """
    Manage rotation for source set of images.

    As they need to be in portrait mode.
    """

    BASE_TEMPLATE_REL_PATH = "../ressources/base.pto"
    TMP_PTONAME = "cp.pto"
    TMP_OUTPUT = "out.pto"
    CPFIND_OPTIONS = [
        "--multirow",
        "--sieve1width", "25",
        "--sieve1height", "25",
        "--sieve1size", "625",
        "--kdtreesteps", "300"]

    def searchCP(self):
        """Run cli CP search."""
        # Getting base template
        this_dir, _ = os.path.split(__file__)
        base_pto_path = Path(this_dir) / self.BASE_TEMPLATE_REL_PATH

        with self._opv_directory_manager.Open(self.lot.pictures_path) as (_, pictures_dir):
            local_tmp_pto = Path(pictures_dir) / self.TMP_PTONAME
            tmp_output_pto = Path(pictures_dir) / self.TMP_OUTPUT
            logging.debug("Copy base template " + base_pto_path + " -> " + local_tmp_pto)
            copyfile(base_pto_path, local_tmp_pto)  # need pto to be local as pictures path are relatives

            options = list(self.CPFIND_OPTIONS)
            options.append('-o')  # output pto file
            options.append(tmp_output_pto)
            options.append(local_tmp_pto)          # input pto file
            logging.debug("Starting CP search with options" + " ".join(options))
            self._run_cli("cpfind", options)

            cp_pto_dest = Path(self.ptoDirMan.local_directory) / Const.CP_PTO_FILENAME
            logging.debug("Moving " + local_tmp_pto + " -> " + cp_pto_dest + " (UUID : " + self.ptoDirMan.uuid + ")")
            os.unlink(local_tmp_pto)  # remove based file
            os.rename(tmp_output_pto, cp_pto_dest)  # copies PTO to is't directory man

    def findCP(self):
        """Initiate cp object and run search."""
        logging.info("Running cpfind for lot : " + str(self.lot.id))
        self.cp = self._client_requestor.Cp()
        self.cp.search_algo_version = Const.CP_SEARCHALGO_VERSION
        self.cp.lot = self.lot
        self.ptoDirMan = self._opv_directory_manager.Open()
        self.cp.pto_dir = self.ptoDirMan.uuid

        self.searchCP()

        self.ptoDirMan.save()
        self.cp.save()

    def run(self, options={}):
        """Run Cp find task."""
        idCp = None

        if "id" in options:
            self.lot = self._client_requestor.Lot(options["id"])
            self.findCP()
            idCp = self.cp.id

        return json.dumps({'id': idCp})
