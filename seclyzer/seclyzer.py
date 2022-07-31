#!/usr/bin/env python
# -*- coding: utf_8 -*-
"""Integration: secscan."""
from pathlib import Path

from seclyzer import (
    settings,
    utils,
)

from secscan.secscan import SECScan
from secscan.settings import (
    IGNORE_PATHS,
    NODEJS_FILE_EXTENSIONS,
    TEMPLATE_FILE_EXTENSIONS,
)


def all_files(path, search=False, term=None):
    """Gather all files or search."""
    filelist = []
    ignote_paths = IGNORE_PATHS.union(settings.IGNORE_PATHS)
    supported_ext = NODEJS_FILE_EXTENSIONS.union(TEMPLATE_FILE_EXTENSIONS)
    for file_path in Path(path).rglob('*'):
        if not file_path.is_file():
            continue
        if file_path.suffix not in supported_ext:
            continue
        if any(ignore in file_path.as_posix()
                for ignore in ignote_paths):
            continue
        relative = file_path.as_posix().replace(
            settings.UPLOAD_FOLDER, '', 1)
        if relative.startswith('/'):
            relative = relative.replace('/', '', 1)
        if search:
            if term in utils.read_file(file_path.as_posix()):
                filelist.append(relative)
        else:
            filelist.append(relative)
    return filelist


def call_secscan(node_source):
    """Call secscan."""
    scanner = SECScan(
        [node_source],
        json=True,
        check_controls=settings.CHECK_MISSING_CONTROLS)
    return scanner.scan()


def add_ids(res):
    """Add hash to findings."""
    if not res:
        return
    for rule, finds in res.items():
        if not finds.get('files'):
            res[rule]['id'] = utils.sha256_finding(finds)
            continue
        for file in finds['files']:
            uniq = {
                'file': file,
                'rule': rule}
            file['id'] = utils.sha256_finding(uniq)


def scan(node_source):
    """Perform scan."""
    print('Analysing Repository')
    result = call_secscan(node_source)
    add_ids(result.get('nodejs'))
    add_ids(result.get('templates'))
    result['files'] = all_files(node_source)
    return result
