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
"""Augments json files with table linearization used by baselines.

Note that this code is merely meant to be starting point for research and
there may be much better table representations for this task.
"""
import copy
import json

from absl import app
from absl import flags

from language.totto.baseline_preprocessing import preprocess_utils

import six
from stemming.porter2 import stem

flags.DEFINE_string("input_path", None, "Input json file.")

flags.DEFINE_string("output_path", None, "Output directory.")

flags.DEFINE_integer("examples_to_visualize", 100,
                     "Number of examples to visualize.")

FLAGS = flags.FLAGS


def _generate_processed_examples(input_path):
  """Generate TF examples."""
  processed_json_examples = []
  step = 0
  with open(input_path, "r", encoding="utf-8") as input_file:
    for line in input_file:
      step+=1
      if len(processed_json_examples) % 100 == 0:
        print("Num examples processed: %d" % len(processed_json_examples))

      line = six.ensure_text(line, "utf-8")
      json_example = json.loads(line)
      table = json_example["table"]
      table_page_title = json_example["table_page_title"]
      table_section_title = json_example["table_section_title"]
      cell_indices = json_example["highlighted_cells"]

      ################################################################################## reference token mask
      reference_sentence = json_example['sentence_annotations'][0]['final_sentence']
      reference_sentence = reference_sentence.lower()
      reference_sentence = stem(reference_sentence)
      reference_sentence_tokens = reference_sentence.split(' ')
      ##################################################################################
      # print(reference_sentence_tokens)
      # break
      # print(cell_indices)
      # break
      # print(len(table))
      # print(len(table[0]))
      # print(subtable)
      # break 
      if step % 10 == 1:
        subtable = (
          preprocess_utils.get_highlighted_subtable1(
              table=table,
              cell_indices=cell_indices,
              with_heuristic_headers=True,reference_tokens=reference_sentence_tokens))
      
      if step % 10 == 2:
        subtable = (
          preprocess_utils.get_highlighted_subtable2(
              table=table,
              cell_indices=cell_indices,
              with_heuristic_headers=True,reference_tokens=reference_sentence_tokens))
      if step % 10 == 3:
        subtable = (
          preprocess_utils.get_highlighted_subtable3(
              table=table,
              cell_indices=cell_indices,
              with_heuristic_headers=True,reference_tokens=reference_sentence_tokens))
      if step % 10 == 4:
        subtable = (
          preprocess_utils.get_highlighted_subtable4(
              table=table,
              cell_indices=cell_indices,
              with_heuristic_headers=True,reference_tokens=reference_sentence_tokens))
      if step % 10 == 5:
        subtable = (
          preprocess_utils.get_highlighted_subtable(
              table=table,
              cell_indices=cell_indices,
              with_heuristic_headers=True,reference_tokens=reference_sentence_tokens))
      if step % 10 == 6:
        subtable = (
          preprocess_utils.get_highlighted_subtable(
              table=table,
              cell_indices=cell_indices,
              with_heuristic_headers=True,reference_tokens=reference_sentence_tokens))
      if step % 10 == 7:
        subtable = (
          preprocess_utils.get_highlighted_subtable(
              table=table,
              cell_indices=cell_indices,
              with_heuristic_headers=True,reference_tokens=reference_sentence_tokens))
      if step % 10 == 8:
        subtable = (
          preprocess_utils.get_highlighted_subtable(
              table=table,
              cell_indices=cell_indices,
              with_heuristic_headers=True,reference_tokens=reference_sentence_tokens))
      if step % 10 == 9:
        subtable = (
          preprocess_utils.get_highlighted_subtable(
              table=table,
              cell_indices=cell_indices,
              with_heuristic_headers=True,reference_tokens=reference_sentence_tokens))
      if step % 10 == 10:
        subtable = (
          preprocess_utils.get_highlighted_subtable(
              table=table,
              cell_indices=cell_indices,
              with_heuristic_headers=True,reference_tokens=reference_sentence_tokens))
            
        
      # print(subtable)
      # break

      # Table strings without page and section title.
      full_table_str = preprocess_utils.linearize_full_table(
          table=table,
          cell_indices=cell_indices,
          table_page_title=None,
          table_section_title=None)
      
      subtable_str = (
          preprocess_utils.linearize_subtable(
              subtable=subtable,
              table_page_title=None,
              table_section_title=None))

      full_table_metadata_str = (
          preprocess_utils.linearize_full_table(
              table=table,
              cell_indices=cell_indices,
              table_page_title=table_page_title,
              table_section_title=table_section_title))

      subtable_metadata_str = (
          preprocess_utils.linearize_subtable(
              subtable=subtable,
              table_page_title=table_page_title,
              table_section_title=table_section_title))

      processed_json_example = copy.deepcopy(json_example)
      processed_json_example["full_table_str"] = full_table_str
      processed_json_example["subtable_str"] = subtable_str
      processed_json_example[
          "full_table_metadata_str"] = full_table_metadata_str
      processed_json_example["subtable_metadata_str"] = subtable_metadata_str
      processed_json_examples.append(processed_json_example)

      # print(cell_indices)#test
      # print(subtable_str)
      # print(subtable_metadata_str)
      # break

  print("Num examples processed: %d" % len(processed_json_examples))
  return processed_json_examples


def main(_):
  input_path = FLAGS.input_path
  output_path = FLAGS.output_path
  processed_json_examples = _generate_processed_examples(input_path)
  with open(output_path, "w", encoding="utf-8") as f:
    for json_example in processed_json_examples:
      f.write(json.dumps(json_example) + "\n")


if __name__ == "__main__":
  app.run(main)

  
