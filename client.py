class B2bKiranaWholesaleRetailSmeCreditEngineClient:
    def place_kirana_restock_order(self, kirana_store_id='KIRANA_BLR_092', wholesale_staples=None, apply_credit_line=True):
        wholesale_staples = wholesale_staples or [{'item': 'Atta 10kg x10', 'cost_inr': 3800.0}, {'item': 'Sunflower Oil 15L x2', 'cost_inr': 3100.0}]
        total_inr = sum(i['cost_inr'] for i in wholesale_staples)
        return {
            'wholesale_order_id': 'jbt_ord_4491',
            'kirana_store_id': kirana_store_id,
            'total_order_inr': total_inr,
            'sme_working_capital_credit_approved': True,
            'credit_repayment_terms_days': 14,
            'doorstep_kirana_delivery_eta_hours': 18.0,
            'digital_khata_ledger_updated': True
        }
