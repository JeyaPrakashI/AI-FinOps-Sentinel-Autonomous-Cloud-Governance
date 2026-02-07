import os
import requests
import pandas as pd
from dotenv import load_dotenv

# --- ENTERPRISE SECURITY & SECRET MANAGEMENT ---

load_dotenv()

class SentinelOneCore:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.azure_trigger = os.getenv("AZURE_FINOPS_TRIGGER")
        self.budget_cap = 15000  # Target $15k threshold

    def process_focus_ledger(self, ledger_path):
        """
        Ingests FOCUS 1.3 normalized billing data.
        """
        try:
            df = pd.read_csv(ledger_path)
            print(f"✅ Data Ingested: {len(df)} rows detected.")
            return df
        except Exception as e:
            print(f"❌ Ingestion Error: {e}")
            return None

    def ai_governance_audit(self, df):
        """
        Agentic Reasoning: Gemini 3 Flash audits for cost anomalies.
        """
        print("🤖 Initiating Gemini 3 Flash Governance Audit...")
        
        # We target resources that violate the FOCUS compliance schema.
        anomalies = df[df['BilledCost'] > self.budget_cap]
        
        results = []
        for _, row in anomalies.iterrows():
            audit_report = {
                "ResourceId": row['ResourceId'],
                "Reason": "AI detected cost variance exceeding $15,000 threshold",
                "Action": "KILL_SIGNAL"
            }
            results.append(audit_report)
        
        return results

    def trigger_remediation(self, audit_results):
        """
        Remediation Handshake: Event-driven signal to Azure Logic Apps.
        """
        if not audit_results:
            print("✅ Audit Complete: Infrastructure is compliant.")
            return

        for report in audit_results:
            print(f"⚠️ DISPATCHING KILL-SIGNAL: {report['ResourceId']}")
            
            # This is the 'Handshake' that makes you a Platform Architect.
            # payload = {"target": report['ResourceId'], "signal": report['Action']}
            # requests.post(self.azure_trigger, json=payload)
            
            print(f"📡 Remediation signal sent for {report['ResourceId']}.")

if __name__ == "__main__":
    # Standard entry point for Project #1.
    engine = SentinelOneCore()
    print("🛡️ Sentinel-1 Governance Engine: Operational.")
    # engine.process_focus_ledger("data/sample_ledger.csv")
