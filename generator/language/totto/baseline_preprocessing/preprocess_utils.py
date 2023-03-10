# coding=utf-8
# Copyright 2018 The Google AI Language Team Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# Lint as: python3
"""Baseline preprocessing utilities."""
from configparser import InterpolationMissingOptionError
import copy
from email import header
import random
from pyparsing import col
from stemming.porter2 import stem 
from scipy import rand

def _add_adjusted_col_offsets(table):
  """Add adjusted column offsets to take into account multi-column cells."""
  adjusted_table = []
  for row in table:
    real_col_index = 0
    adjusted_row = []
    for cell in row:
      adjusted_cell = copy.deepcopy(cell)
      adjusted_cell["adjusted_col_start"] = real_col_index
      adjusted_cell["adjusted_col_end"] = (
          adjusted_cell["adjusted_col_start"] + adjusted_cell["column_span"])
      real_col_index += adjusted_cell["column_span"]
      adjusted_row.append(adjusted_cell)
    adjusted_table.append(adjusted_row)
  return adjusted_table


def _get_heuristic_row_headers(adjusted_table, row_index, col_index):
  """Heuristic to find row headers."""
  row_headers = []
  row = adjusted_table[row_index]
  for i in range(0, col_index):
    if row[i]["is_header"]:
      row_headers.append(row[i])
  return row_headers


def _get_heuristic_col_headers(adjusted_table, row_index, col_index):
  """Heuristic to find column headers."""
  adjusted_cell = adjusted_table[row_index][col_index]
  adjusted_col_start = adjusted_cell["adjusted_col_start"]
  adjusted_col_end = adjusted_cell["adjusted_col_end"]
  col_headers = []
  for r in range(0, row_index):
    row = adjusted_table[r]
    for cell in row:
      if (cell["adjusted_col_start"] < adjusted_col_end and
          cell["adjusted_col_end"] > adjusted_col_start):
        if cell["is_header"]:
          col_headers.append(cell)

  return col_headers


def get_highlighted_subtable1(table, cell_indices, with_heuristic_headers=False,reference_tokens=[]):
  """Extract out the highlighted part of a table."""
  highlighted_table = []

  adjusted_table = _add_adjusted_col_offsets(table)
  # print(len(adjusted_table))
  # print(len(adjusted_table[0]))
  
   ########################################################################## add noise
  row =  len(table)
  col = 999
  for e in table:
     if len(e)<col:
       col = len(e)
  noise = [random.randint(0,row),random.randint(0,col)]
   # print(row,'   ',col)
   # print('-----------------------------')
   # print(cell_indices)
  while noise in cell_indices:
    noise = [random.randint(0,row),random.randint(0,col)]
  cell_indices.append(noise)

  for (row_index, col_index) in cell_indices:
    try:
      cell = table[row_index][col_index]
      
      # break
      if with_heuristic_headers:
        row_headers = _get_heuristic_row_headers(adjusted_table, row_index,
                                                col_index)
        col_headers = _get_heuristic_col_headers(adjusted_table, row_index,
                                                col_index)
      else:
        row_headers = []
        col_headers = []

      highlighted_cell = {
          "cell": cell,
          "row_headers": row_headers,
          "col_headers": col_headers
      }
      # print(highlighted_cell)
      highlighted_table.append(highlighted_cell)
    except:
      pass

  return highlighted_table


def get_highlighted_subtable(table, cell_indices, with_heuristic_headers=False,reference_tokens=[]):
  """Extract out the highlighted part of a table."""
  highlighted_table = []

  adjusted_table = _add_adjusted_col_offsets(table)
  # print(len(adjusted_table))
  # print(len(adjusted_table[0]))
  
  for (row_index, col_index) in cell_indices:
    try:
      cell = table[row_index][col_index]
      
      # break
      if with_heuristic_headers:
        row_headers = _get_heuristic_row_headers(adjusted_table, row_index,
                                                col_index)
        col_headers = _get_heuristic_col_headers(adjusted_table, row_index,
                                                col_index)
      else:
        row_headers = []
        col_headers = []

      highlighted_cell = {
          "cell": cell,
          "row_headers": row_headers,
          "col_headers": col_headers
      }
      # print(highlighted_cell)
      highlighted_table.append(highlighted_cell)
    except:
      pass

  return highlighted_table

def get_highlighted_subtable2(table, cell_indices, with_heuristic_headers=False,reference_tokens=[]):
  """Extract out the highlighted part of a table."""
  highlighted_table = []

  adjusted_table = _add_adjusted_col_offsets(table)
  # print(len(adjusted_table))
  # print(len(adjusted_table[0]))

  ################################################################################# header noise
  highlighted_num = len(cell_indices)
  header_noise = [0,cell_indices[random.randint(0,highlighted_num-1)][1]]
  cell_indices.append(header_noise)

  for (row_index, col_index) in cell_indices:
    try:
      cell = table[row_index][col_index]
      
      # break
      if with_heuristic_headers:
        row_headers = _get_heuristic_row_headers(adjusted_table, row_index,
                                                col_index)
        col_headers = _get_heuristic_col_headers(adjusted_table, row_index,
                                                col_index)
      else:
        row_headers = []
        col_headers = []

      highlighted_cell = {
          "cell": cell,
          "row_headers": row_headers,
          "col_headers": col_headers
      }
      # print(highlighted_cell)
      highlighted_table.append(highlighted_cell)
    except:
      pass

  return highlighted_table


def get_highlighted_subtable3(table, cell_indices, with_heuristic_headers=False,reference_tokens=[]):
  """Extract out the highlighted part of a table."""
  highlighted_table = []

  adjusted_table = _add_adjusted_col_offsets(table)
  # print(len(adjusted_table))
  # print(len(adjusted_table[0]))

  highlighted__num = len(cell_indices)
  if highlighted__num>=3: 
    cell_indices.pop(random.randint(0,highlighted__num-1))





  for (row_index, col_index) in cell_indices:
    try:
      cell = table[row_index][col_index]
      
      # break
      if with_heuristic_headers:
        row_headers = _get_heuristic_row_headers(adjusted_table, row_index,
                                                col_index)
        col_headers = _get_heuristic_col_headers(adjusted_table, row_index,
                                                col_index)
      else:
        row_headers = []
        col_headers = []

      highlighted_cell = {
          "cell": cell,
          "row_headers": row_headers,
          "col_headers": col_headers
      }
      # print(highlighted_cell)
      highlighted_table.append(highlighted_cell)
    except:
      pass

  return highlighted_table


def get_highlighted_subtable4(table, cell_indices, with_heuristic_headers=False,reference_tokens=[]):
  """Extract out the highlighted part of a table."""
  highlighted_table = []

  adjusted_table = _add_adjusted_col_offsets(table)
  # print(len(adjusted_table))
  # print(len(adjusted_table[0]))
  
# ########################################################################## add noise
#   row =  len(table)
#   col = 999
#   for e in table:
#     if len(e)<col:
#       col = len(e)
#   noise = [random.randint(0,row),random.randint(0,col)]
#   # print(row,'   ',col)
#   # print('-----------------------------')
#   # print(cell_indices)
#   while noise in cell_indices:
#     noise = [random.randint(0,row),random.randint(0,col)]
#   cell_indices.append(noise)
#   # print(cell_indices)
#   # print()
# ###############################################################################

# ############################################################################### mask
#   highlighted__num = len(cell_indices)
#   if highlighted__num>=3: 
#     cell_indices.pop(random.randint(0,highlighted__num-1))

# ###############################################################################

# ################################################################################# header noise
#   highlighted_num = len(cell_indices)
#   header_noise = [0,cell_indices[random.randint(0,highlighted_num-1)][1]]
#   cell_indices.append(header_noise)
# #################################################################################

# ################################################################################# row col noise
#   row =  len(table)
#   col = 999
#   for e in table:
#     if len(e)<col:
#       col = len(e)
#   highlighted_num = len(cell_indices)
#   rand_highlighted_cell = cell_indices[random.randint(0,highlighted_num-1)]
#   # print(rand_highlighted_cell)
#   row_flag = random.randint(0,1)
#   if row_flag:
#     noise = [random.randint(0,row),rand_highlighted_cell[1]]
#     # while noise in cell_indices:
#     #   noise = [random.randint(0,row),rand_highlighted_cell[1]]
#   else:
#     noise = [rand_highlighted_cell[0],random.randint(0,col)]
#     # while noise in cell_indices:
#     #   noise =[rand_highlighted_cell[0],random.randint(0,col)]
#   # print(noise)
#   # print('----------------------')
#   # print(row,'   ',col)
#   # print('-----------------------------')
#   # print(cell_indices) 
#   cell_indices.append(noise)
#   # print(cell_indices)
#   # print('--------------------')
# #################################################################################


  ################################################################################### reference token mask
  # print(cell_indices)
  if reference_tokens!=[]:
    for (row_index, col_index) in cell_indices:
      # print((row_index, col_index))
      cell_text = table[row_index][col_index]['value']
      cell_text_tokens = stem(cell_text.lower()).split(' ')
      text_len = len(cell_text_tokens)
      count = 0
      for e in cell_text_tokens:
        for _ in reference_tokens:
          if e.find(_)>=0 or _.find(e)>=0:
            count+=1
      if count==0:
        cell_indices.remove([row_index,col_index])
  # print(cell_indices)
  # print('----------------------------------')
  ##################################################################################

  for (row_index, col_index) in cell_indices:
    try:
      cell = table[row_index][col_index]
      
      # break
      if with_heuristic_headers:
        row_headers = _get_heuristic_row_headers(adjusted_table, row_index,
                                                col_index)
        col_headers = _get_heuristic_col_headers(adjusted_table, row_index,
                                                col_index)
      else:
        row_headers = []
        col_headers = []

      highlighted_cell = {
          "cell": cell,
          "row_headers": row_headers,
          "col_headers": col_headers
      }
      # print(highlighted_cell)
      highlighted_table.append(highlighted_cell)
    except:
      pass

  return highlighted_table


def linearize_full_table(table, cell_indices, table_page_title,
                         table_section_title):
  """Linearize full table with localized headers and return a string."""
  table_str = ""
  if table_page_title:
    table_str += "<page_title> " + table_page_title + " </page_title> "
  if table_section_title:
    table_str += "<section_title> " + table_section_title + " </section_title> "

  table_str += "<table> "
  adjusted_table = _add_adjusted_col_offsets(table)
  for r_index, row in enumerate(table):
    row_str = "<row> "
    for c_index, col in enumerate(row):

      row_headers = _get_heuristic_row_headers(adjusted_table, r_index, c_index)
      col_headers = _get_heuristic_col_headers(adjusted_table, r_index, c_index)

      # Distinguish between highlighted and non-highlighted cells.
      if [r_index, c_index] in cell_indices:
        start_cell_marker = "<highlighted_cell> "
        end_cell_marker = "</highlighted_cell> "
      else:
        start_cell_marker = "<cell> "
        end_cell_marker = "</cell> "

      # The value of the cell.
      item_str = start_cell_marker + col["value"] + " "
      # print(item_str)

      # All the column headers associated with this cell.
      for col_header in col_headers:
        item_str += "<col_header> " + col_header["value"] + " </col_header> "

      # All the row headers associated with this cell.
      for row_header in row_headers:
        item_str += "<row_header> " + row_header["value"] + " </row_header> "

      item_str += end_cell_marker
      row_str += item_str

    row_str += "</row> "
    table_str += row_str
    # print(table_str)
    # break

  table_str += "</table>"
  if cell_indices:
    assert "<highlighted_cell>" in table_str
  # print(table_str)
  return table_str


def linearize_subtable(subtable, table_page_title, table_section_title):
  """Linearize the highlighted subtable and return a string of its contents."""
  table_str = ""
  if table_page_title:
    table_str += "<page_title> " + table_page_title + " </page_title> "
  if table_section_title:
    table_str += "<section_title> " + table_section_title + " </section_title> "
  table_str += "<table> "

  for item in subtable:
    cell = item["cell"]
    row_headers = item["row_headers"]
    col_headers = item["col_headers"]

    # The value of the cell.
    item_str = "<cell> " + cell["value"] + " "

    # All the column headers associated with this cell.
    for col_header in col_headers:
      item_str += "<col_header> " + col_header["value"] + " </col_header> "

    # All the row headers associated with this cell.
    for row_header in row_headers:
      item_str += "<row_header> " + row_header["value"] + " </row_header> "

    item_str += "</cell> "
    table_str += item_str

  table_str += "</table>"
  return table_str
