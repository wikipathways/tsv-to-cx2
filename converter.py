import csv
import json
import os

input_file = input("Enter the input TSV file name (including extension): ").strip()

base, _ = os.path.splitext(input_file)
output_file = f"{base}.cx2"

nodes = []
node_id = 0

with open(input_file, 'r', newline='', encoding='utf-8') as tsvfile:
    reader = csv.DictReader(tsvfile, delimiter='\t')
    for row in reader:
        if not row or all(not (value or "").strip() for value in row.values()):
            continue

        gene_symbol = row.get("ncbigene_symbol", "").strip()
        if not gene_symbol:
            continue

        ncbigene_id_str = row.get("ncbigene_id", "").strip()
        if not ncbigene_id_str:
            continue
        try:
            ncbigene_id = int(ncbigene_id_str)
        except ValueError:
            continue

        source_value = row.get("source", "").strip()
        word_value = row.get("word", "").strip()

        represents = f"ncbigene:{ncbigene_id}"

        x = 100 * (node_id % 10)
        y = 100 * (node_id // 10)

        node = {
            "id": node_id,
            "x": x,
            "y": y,
            "v": {
                "name": gene_symbol,
                "represents": represents,
                "symbol": gene_symbol,
                "source": source_value,
                "hgnc.symbol": gene_symbol,
                "ncbigene": ncbigene_id,
                "type": "gene",
                "word": word_value
            }
        }
        nodes.append(node)
        node_id += 1

node_count = len(nodes)

cx = []

cx.append({
    "CXVersion": "2.0",
    "hasFragments": False
})

metaData = {
    "metaData": [
        {"name": "attributeDeclarations", "elementCount": 1},
        {"name": "networkAttributes", "elementCount": 1},
        {"name": "nodes", "elementCount": node_count},
        {"name": "edges", "elementCount": 0},
        {"name": "visualProperties", "elementCount": 1},
        {"name": "nodeBypasses", "elementCount": 0},
        {"name": "edgeBypasses", "elementCount": 0},
        {"name": "visualEditorProperties", "elementCount": 1},
        {"name": "cyHiddenAttributes", "elementCount": 1},
        {"name": "cyTableColumn", "elementCount": 30}
    ]
}
cx.append(metaData)

attributeDeclarations = {
    "attributeDeclarations": [
        {
            "networkAttributes": {
                "__NetworkImage": {"d": "string"},
                "figureLink": {"d": "string"},
                "figureNumber": {"d": "string"},
                "figureTitle": {"d": "string"},
                "methods": {"d": "string"},
                "networkType": {"d": "string"},
                "organism": {"d": "string"},
                "paperLink": {"d": "string"},
                "paperTitle": {"d": "string"},
                "pfocrId": {"d": "string"},
                "pmcId": {"d": "string"},
                "publicationYear": {"d": "string"},
                "rights": {"d": "string"},
                "reference": {"d": "string"},
                "disease": {"d": "string"},
                "name": {"d": "string"},
                "description": {"d": "string"},
                "version": {"d": "string"}
            },
            "nodes": {
                "hgnc.symbol": {"d": "string"},
                "name": {"d": "string"},
                "ncbigene": {"d": "integer"},
                "represents": {"d": "string"},
                "source": {"d": "string"},
                "symbol": {"d": "string"},
                "type": {"d": "string"},
                "word": {"d": "string"}
            },
            "edges": {}
        }
    ]
}
cx.append(attributeDeclarations)

cx.append({"nodes": nodes})

cx.append({"edges": []})

visual_properties = {
    "visualProperties": [
        {
            "default": {
                "network": {"NETWORK_BACKGROUND_COLOR": "#FFFFFF"},
                "edge": {
                    "EDGE_LABEL": "",
                    "EDGE_LABEL_COLOR": "#000000",
                    "EDGE_LABEL_FONT_FACE": {
                        "FONT_FAMILY": "sans-serif",
                        "FONT_STYLE": "normal",
                        "FONT_WEIGHT": "normal"
                    },
                    "EDGE_LABEL_FONT_SIZE": 10,
                    "EDGE_LABEL_OPACITY": 1,
                    "EDGE_LABEL_ROTATION": 0,
                    "EDGE_LABEL_MAX_WIDTH": 200,
                    "EDGE_LINE_STYLE": "solid",
                    "EDGE_OPACITY": 1,
                    "EDGE_SELECTED_PAINT": "#FF0000",
                    "EDGE_SOURCE_ARROW_COLOR": "#000000",
                    "EDGE_SOURCE_ARROW_SHAPE": "none",
                    "EDGE_LINE_COLOR": "#848484",
                    "EDGE_TARGET_ARROW_COLOR": "#000000",
                    "EDGE_TARGET_ARROW_SHAPE": "none",
                    "EDGE_VISIBILITY": "element",
                    "EDGE_WIDTH": 2,
                    "EDGE_Z_LOCATION": 0
                },
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
                            {"v": "gene", "vp": "#467CA8"}
                        ]
                    }
                },
                "NODE_BORDER_WIDTH": {
                    "type": "DISCRETE",
                    "definition": {
                        "attribute": "type",
                        "map": [
                            {"v": "gene", "vp": 4}
                        ]
                    }
                },
                "NODE_BACKGROUND_COLOR": {
                    "type": "DISCRETE",
                    "definition": {
                        "attribute": "type",
                        "map": [
                            {"v": "protein", "vp": "#D1F5FF"}
                        ]
                    }
                },
                "NODE_HEIGHT": {
                    "type": "DISCRETE",
                    "definition": {
                        "attribute": "type",
                        "map": [
                            {"v": "gene", "vp": 25}
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
                            {"v": "protein", "vp": "ellipse"}
                        ]
                    }
                },
                "NODE_WIDTH": {
                    "type": "DISCRETE",
                    "definition": {
                        "attribute": "type",
                        "map": [
                            {"v": "gene", "vp": 60}
                        ]
                    }
                }
            },
            "edgeMapping": {}
        }
    ]
}
cx.append(visual_properties)

cx.append({"nodeBypasses": []})

cx.append({"edgeBypasses": []})

visual_editor_properties = {
    "visualEditorProperties": [
        {
            "properties": {
                "nodeSizeLocked": False,
                "arrowColorMatchesEdge": False
            }
        }
    ]
}
cx.append(visual_editor_properties)

cx.append({"cyHiddenAttributes": [{"n": "layoutAlgorithm", "v": "Prefuse Force Directed Layout"}]})

cy_table_columns = {
    "cyTableColumn": [
        {"applies_to": "node_table", "n": "shared name"},
        {"applies_to": "node_table", "n": "name"},
        {"applies_to": "node_table", "n": "ncbigene", "d": "integer"},
        {"applies_to": "node_table", "n": "word"},
        {"applies_to": "node_table", "n": "symbol"},
        {"applies_to": "node_table", "n": "source"},
        {"applies_to": "node_table", "n": "hgnc.symbol"},
        {"applies_to": "node_table", "n": "type"},
        {"applies_to": "edge_table", "n": "shared name"},
        {"applies_to": "edge_table", "n": "shared interaction"},
        {"applies_to": "edge_table", "n": "name"},
        {"applies_to": "edge_table", "n": "interaction"},
        {"applies_to": "network_table", "n": "shared name"},
        {"applies_to": "network_table", "n": "name"},
        {"applies_to": "network_table", "n": "__Annotations", "d": "list_of_string"},
        {"applies_to": "network_table", "n": "pmcid"},
        {"applies_to": "network_table", "n": "pfocr_id"},
        {"applies_to": "network_table", "n": "figure_number"},
        {"applies_to": "network_table", "n": "figure_title"},
        {"applies_to": "network_table", "n": "description"},
        {"applies_to": "network_table", "n": "figure_link"},
        {"applies_to": "network_table", "n": "paper_title"},
        {"applies_to": "network_table", "n": "reference"},
        {"applies_to": "network_table", "n": "publication_year"},
        {"applies_to": "network_table", "n": "paper_link"},
        {"applies_to": "network_table", "n": "version"},
        {"applies_to": "network_table", "n": "organism"},
        {"applies_to": "network_table", "n": "rights"},
        {"applies_to": "network_table", "n": "methods"},
        {"applies_to": "network_table", "n": "networkType"}
    ]
}
cx.append(cy_table_columns)

cx.append({"status": [{"error": "", "success": True}]})


with open(output_file, 'w', encoding='utf-8') as outfile:
    json.dump(cx, outfile, indent=2)

print(f"Conversion complete! {node_count} nodes written to {output_file}.")