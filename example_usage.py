from client import B2bKiranaWholesaleRetailSmeCreditEngineClient

def main():
    client = B2bKiranaWholesaleRetailSmeCreditEngineClient()
    res = client.place_kirana_restock_order('KIRANA_MYSURU_11', [{'item': 'Basmati Rice 25kg', 'cost_inr': 2400.0}])
    print('Order: ' + res['wholesale_order_id'] + ' | Total: INR ' + str(res['total_order_inr']))
    print('SME Credit: Approved (' + str(res['credit_repayment_terms_days']) + ' days term) | Delivery: ' + str(res['doorstep_kirana_delivery_eta_hours']) + ' hrs')
    print('Digital Ledger: ' + str(res['digital_khata_ledger_updated']))

if __name__ == '__main__':
    main()
