from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Sample Data (replace this with actual data from a JSON file or database in a real-world app)
data = [
    {
        "id": 58820,
        "previous_requisition_id": 58819,
        "project_id": 789,
        "billing_date": "2013-11-20",
        "created_at": "2013-11-15T12:00:00Z",
        "updated_at": "2013-11-15T12:00:00Z",
        "commitment_id": 701973,
        "commitment_type": "WorkOrderContract",
        "contract_name": "Contract SC-001",
        "deletable": False,
        "final": True,
        "vendor_name": "Ernie's Electrical",
        "vendor_id": 8881212,
        "invoice_number": 123,
        "origin_data": "XYZ-0012",
        "origin_id": "abc-123",
        "payment_date": "2013-11-15",
        "percent_complete": 0,
        "period_id": 4293,
        "requisition_start": "2013-11-01",
        "requisition_end": "2013-11-02",
        "status": "approved",
        "erp_status": "synced",
        "number": 1,
        "submitted_at": "2013-11-02",
        "total_claimed_amount": "100.00",
        "electronic_signature_id": 701973,
        "move_materials_to_previous_work_completed": False,
        "summary_text": {
            "project_name": "Project",
            "project_number": "100",
            "to_general_contractor": "Company A",
            "requisition_period_start": "2010-01-01",
            "requisition_period_end": "2010-01-01",
            "subcontractor_name": "Company B",
            "subcontractor_street": "101 XYZ Avenue",
            "subcontractor_city": "New York",
            "subcontractor_state_code": "NY",
            "subcontractor_zip": "10101",
            "subcontractor_country_code": "US",
            "application_number": "1",
            "contract_for": "Ceiling Tiles",
            "contract_date": "2010-01-01"
        },
        "summary": {
            "balance_to_finish_including_retainage": 1268346.55,
            "completed_work_retainage_percent": 10,
            "completed_work_retainage_amount": "1201.0",
            "contract_sum_to_date": 1279159.15,
            "current_payment_due": 10812.6,
            "formatted_period": "01/06/19 - 30/06/19",
            "less_previous_certificates_for_payment": 0,
            "negative_change_order_item_total": 0,
            "negative_new_change_order_item_total": 0,
            "negative_previous_change_order_item_total": 0,
            "net_change_by_change_orders": 256706.65,
            "original_contract_sum": 1022452.5,
            "positive_change_order_item_total": "0.00",
            "positive_new_change_order_item_total": "0.00",
            "positive_previous_change_order_item_total": "0.00",
            "stored_materials_retainage_amount": 0.4,
            "stored_materials_retainage_percent": 10,
            "tax_applicable_to_this_payment": 0,
            "total_completed_and_stored_to_date": 1201.4,
            "total_earned_less_retainage": 10812.6,
            "total_retainage": 1201.4,
            "new_materials": "1975.31",
            "new_materials_quantity": "98.7654",
            "stored_materials": "716.05",
            "stored_materials_quantity": "35.80249"
        },
        "created_by": {
            "id": 1738090,
            "name": "John Doe",
            "login": "johndoe@example.com",
            "company_name": "Builders Inc."
        },
        "custom_fields": {
            "custom_field_%{custom_field_string_definition_id}": {
                "data_type": "string",
                "value": "custom field value"
            },
            "custom_field_%{custom_field_decimal_definition_id}": {
                "data_type": "decimal",
                "value": 2.2
            },
            "custom_field_%{custom_field_boolean_definition_id}": {
                "data_type": "boolean",
                "value": True
            },
            "custom_field_%{custom_field_lov_entry_definition_id}": {
                "data_type": "lov_entry",
                "value": {
                    "id": 1,
                    "label": "Open"
                }
            },
            "custom_field_%{custom_field_lov_entries_definition_id}": {
                "data_type": "lov_entries",
                "value": [
                    {
                        "id": 2,
                        "label": "Open"
                    }
                ]
            }
        },
        "currency_configuration": {
            "currency_iso_code": "USD",
            "currency_exchange_rate": 1.8,
            "base_currency_iso_code": "EUR"
        },
        "attachments": [
            {
                "id": 5324,
                "url": "http://www.example.com/",
                "filename": "january_receipt_copy.jpg",
                "content_type": "image/jpeg"
            }
        ],
        "items": [
            {
                "id": 341256,
                "item_type": "contract_detail_item",
                "accounting_method": "amount",
                "cost_code_id": 21585118,
                "currency_configuration": {
                    "currency_iso_code": "USD",
                    "currency_exchange_rate": 1.8,
                    "base_currency_iso_code": "EUR"
                },
                "line_item_id": 3129856,
                "description_of_work": "Install windows",
                "net_amount": "100.00",
                "gross_amount": "200.00",
                "wbs_code": {
                    "id": 44,
                    "flat_code": "2.E",
                    "description": "Earthwork.Equipment",
                    "segment_items": [
                        {
                            "id": 55,
                            "code": 2,
                            "name": "Earthwork",
                            "path_ids": [
                                [
                                    55
                                ]
                            ],
                            "path_codes": [
                                [
                                    "2 - Earthwork"
                                ]
                            ],
                            "segment_type": "cost_code",
                            "segment_id": 42
                        }
                    ]
                },
                "scheduled_value": "1.00",
                "work_completed_from_previous_application": "0.00",
                "work_completed_this_period": "0.00",
                "materials_presently_stored": "2691.36",
                "materials_presently_stored_quantity": "134.56789",
                "materials_presently_stored_from_previous_progress": "0.00",
                "materials_previously_stored_quantity": 12.3456,
                "materials_moved": "0.00",
                "materials_retainage_retained_moved": "0.00",
                "total_completed_and_stored_to_date": "0.00",
                "total_completed_and_stored_to_date_percent": "0.0",
                "total_completed_and_stored_to_date_from_previous": "100.00",
                "work_completed_retainage_from_previous_application": "0.0",
                "work_completed_retainage_retained_this_period": "0.0",
                "work_completed_retainage_percent_this_period": "10.0",
                "materials_stored_retainage_currently_retained": "0.0",
                "materials_stored_retainage_percent_this_period": "10.0",
                "materials_stored_retainage_new_materials": "10.0",
                "work_completed_retainage_released_this_period": "0.0",
                "materials_stored_retainage_released_this_period": "0.0",
                "scheduled_quantity": "0.0",
                "scheduled_unit_price": "20.0",
                "work_completed_this_period_quantity": "0.0",
                "work_completed_from_previous_application_quantity": "0.0",
                "comment": "Installation charges",
                "status": "no_action",
                "position": 1,
                "line_number": "1.1",
                "ssr_manual_override": False,
                "subcontractor_claimed_amount": "0.0"
            }
        ]
    }
]

# API Key (For simplicity, using static API key in this case)
API_KEY = 'your-api-key'

# Function to authenticate API requests
def authenticate_request(api_key):
    if api_key != API_KEY:
        return False
    return True

# Endpoint to fetch top 5 invoices for a project
@app.route('/top_invoices', methods=['GET'])
def top_invoices():
    # Fetch the 'project_id' from the query parameters
    project_id = request.args.get('project_id', type=int)
    api_key = request.headers.get('API-Key')

    if not authenticate_request(api_key):
        return jsonify({"error": "Unauthorized access"}), 403

    # Filter invoices for the specific project
    project_invoices = [invoice for invoice in data if invoice['project_id'] == project_id]

    if not project_invoices:
        return jsonify({"error": "No invoices found for the given project"}), 404

    # Sort invoices by 'total_claimed_amount' in descending order
    sorted_invoices = sorted(project_invoices, key=lambda x: float(x['total_claimed_amount']), reverse=True)

    # Return top 5 invoices with necessary fields
    top_invoices = [{
    "Invoice ID": invoice["id"],
    "Contractor Name": invoice["summary_text"]["contract_for"],  
    "Vendor Name": invoice["vendor_name"],
    "Invoice Amount": invoice["total_claimed_amount"]
} for invoice in sorted_invoices[:5]]
    return jsonify({"message": "Here are the Top 5 Invoices based on the amount", "top_invoices": top_invoices})

# Endpoint to get summary of the invoice with the highest balance
@app.route('/invoice_summary', methods=['GET'])
def invoice_summary():
    # Get the API key from headers
    api_key = request.headers.get('API-Key')

    # Validate the API key
    if not authenticate_request(api_key):
        return jsonify({"error": "Unauthorized access"}), 403

    # Get the question from the query parameters or request body (as per your requirement)
    question = request.args.get('question')  # Or, use `request.json` if it's in the body

    if question:
        # Check if the question is related to invoice summaries
        if "invoice" not in question.lower() or "summary" not in question.lower():
            return jsonify({"error": "Sorry, I can only answer questions related to invoice summaries."}), 400
    
    try:
        # Find the invoice with the highest balance to finish including retainage
        highest_balance_invoice = max(data, key=lambda x: x["summary"]["balance_to_finish_including_retainage"])

        # Construct the response message
        response = {
            "message": "Here you go, The invoice with Id {} has the highest balance amount pending with an amount ${:,.2f}".format(
                highest_balance_invoice["id"],
                highest_balance_invoice["summary"]["balance_to_finish_including_retainage"]
            ),
            "Invoice ID": highest_balance_invoice["id"],
            "Vendor Name": highest_balance_invoice["vendor_name"],
            "Balance Amount": highest_balance_invoice["summary"]["balance_to_finish_including_retainage"]
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/ask', methods=['GET'])
def ask():
    question = request.args.get('question', type=str)
    api_key = request.headers.get('API-Key')

    # Check if API key is valid
    if not authenticate_request(api_key):
        return jsonify({"error": "Unauthorized access"}), 403

    # Check if question is provided
    if not question:
        return jsonify({"error": "Please provide a question."}), 400

    # Print the question for debugging purposes
    print(f"Question received: {question}")

    # Handle negative questions like sports scores
    if "current score" in question.lower():
        return jsonify({"error": "Sorry, I cannot provide sports scores."}), 400

    # If the question is not relevant, return a generic error
    return jsonify({"error": "I'm not sure how to answer that. Could you rephrase the question?"}), 400

if __name__ == '__main__':
    app.run(debug=True)
