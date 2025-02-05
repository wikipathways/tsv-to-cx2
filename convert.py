import csv
import json

tsv_filename = 'input.tsv'
cx_filename = 'output.cx2'

cx = []

cx.append({
    "CXVersion": "2.0",
    "hasFragments": False
})

nodes = []
node_id = 0

with open(tsv_filename, 'r', newline='', encoding='utf-8') as tsvfile:
    reader = csv.DictReader(tsvfile, delimiter='\t')
    for row in reader:
        if not row or all(not (value or "").strip() for value in row.values()):
            continue

        gene_symbol = row.get("ncbigene_symbol", "").strip()
        if not gene_symbol:
            continue

        x = 100 * (node_id % 10)
        y = 100 * (node_id // 10)

        node = {
            "id": node_id,
            "x": x,
            "y": y,
            "v": {
                "name": gene_symbol,
                "type": "gene"
            }
        }
        nodes.append(node)
        node_id += 1

cx.append({"nodes": nodes})

visual_properties = {
    "visualProperties": [
      {
        "default": {
          "node": {
            "NODE_BORDER_COLOR": "#CCCCCC",
            "NODE_BORDER_STYLE": "solid",
            "NODE_BORDER_OPACITY": 1,
            "NODE_BORDER_WIDTH": 1,
            "NODE_BACKGROUND_COLOR": "#FFFFFF",
            "NODE_HEIGHT": 35,
            "NODE_LABEL": "",
            "NODE_LABEL_COLOR": "#000000",
            "NODE_LABEL_FONT_FACE": {
              "FONT_FAMILY": "sans-serif",
              "FONT_STYLE": "normal",
              "FONT_WEIGHT": "normal"
            },
            "NODE_LABEL_FONT_SIZE": 12,
            "NODE_LABEL_OPACITY": 1,
            "NODE_LABEL_POSITION": {
              "HORIZONTAL_ALIGN": "center",
              "VERTICAL_ALIGN": "center",
              "HORIZONTAL_ANCHOR": "center",
              "VERTICAL_ANCHOR": "center",
              "MARGIN_X": 0,
              "MARGIN_Y": 0,
              "JUSTIFICATION": "center"
            },
            "NODE_LABEL_ROTATION": 0,
            "NODE_LABEL_MAX_WIDTH": 200,
            "NODE_BACKGROUND_OPACITY": 1,
            "NODE_SELECTED_PAINT": "#FFFF00",
            "NODE_SHAPE": "round-rectangle",
            "NODE_VISIBILITY": "element",
            "NODE_WIDTH": 75,
            "NODE_Z_LOCATION": "0.0"
          }
        },
        "nodeMapping": {
          "NODE_BORDER_COLOR": {
            "type": "DISCRETE",
            "definition": {
              "attribute": "type",
              "map": [
                { "v": "gene", "vp": "#467CA8" }
              ]
            }
          },
          "NODE_BORDER_WIDTH": {
            "type": "DISCRETE",
            "definition": {
              "attribute": "type",
              "map": [
                { "v": "gene", "vp": 4 }
              ]
            }
          },
          "NODE_BACKGROUND_COLOR": {
            "type": "DISCRETE",
            "definition": {
              "attribute": "type",
              "map": [
                { "v": "protein", "vp": "#D1F5FF" }
              ]
            }
          },
          "NODE_HEIGHT": {
            "type": "DISCRETE",
            "definition": {
              "attribute": "type",
              "map": [
                { "v": "gene", "vp": 25 }
              ]
            }
          },
          "NODE_LABEL": {
            "type": "PASSTHROUGH",
            "definition": {
              "attribute": "name"
            }
          },
          "NODE_SHAPE": {
            "type": "DISCRETE",
            "definition": {
              "attribute": "type",
              "map": [
                { "v": "protein", "vp": "ellipse" }
              ]
            }
          },
          "NODE_WIDTH": {
            "type": "DISCRETE",
            "definition": {
              "attribute": "type",
              "map": [
                { "v": "gene", "vp": 60 }
              ]
            }
          }
        }
      }
    ]
}

cx.append(visual_properties)

cy_table_columns = {
    "cyTableColumn": [
      { "applies_to": "node_table", "n": "shared name" },
      { "applies_to": "node_table", "n": "name" },
      { "applies_to": "node_table", "n": "ncbigene", "d": "integer" },
      { "applies_to": "node_table", "n": "word" },
      { "applies_to": "node_table", "n": "symbol" },
      { "applies_to": "node_table", "n": "source" },
      { "applies_to": "node_table", "n": "hgnc.symbol" },
      { "applies_to": "node_table", "n": "type" },
      { "applies_to": "edge_table", "n": "shared name" },
      { "applies_to": "edge_table", "n": "shared interaction" },
      { "applies_to": "edge_table", "n": "name" },
      { "applies_to": "edge_table", "n": "interaction" },
      { "applies_to": "network_table", "n": "shared name" },
      { "applies_to": "network_table", "n": "name" },
      { "applies_to": "network_table", "n": "__Annotations", "d": "list_of_string" },
      { "applies_to": "network_table", "n": "pmcid" },
      { "applies_to": "network_table", "n": "pfocr_id" },
      { "applies_to": "network_table", "n": "figure_number" },
      { "applies_to": "network_table", "n": "figure_title" },
      { "applies_to": "network_table", "n": "description" },
      { "applies_to": "network_table", "n": "figure_link" },
      { "applies_to": "network_table", "n": "paper_title" },
      { "applies_to": "network_table", "n": "reference" },
      { "applies_to": "network_table", "n": "publication_year" },
      { "applies_to": "network_table", "n": "paper_link" },
      { "applies_to": "network_table", "n": "version" },
      { "applies_to": "network_table", "n": "organism" },
      { "applies_to": "network_table", "n": "rights" },
      { "applies_to": "network_table", "n": "methods" },
      { "applies_to": "network_table", "n": "networkType" }
    ]
}

cx.append(cy_table_columns)

with open(cx_filename, 'w', encoding='utf-8') as outfile:
    json.dump(cx, outfile, indent=2)

print(f"Conversion complete! {len(nodes)} nodes written to {cx_filename}.")