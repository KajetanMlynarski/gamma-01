# Three-layer Meta-Operational System (English)
class MetaOperationalSystem:
    def __init__(self):
        self.layers = {
            "computational": ComputationalLayer(),
            "monitoring": MonitoringLayer(),
            "ontological": OntologicalLayer()
        }
        
    def process_input(self, input_data):
        # Step 1: Computational processing
        processed = self.layers["computational"].execute(input_data)
        
        # Step 2: Harmony metric calculation
        h_metrics = self.layers["monitoring"].analyze(processed)
        
        # Step 3: Γ-harmonization
        if h_metrics["H"] >= 0.82:
            return self.layers["ontological"].harmonize(processed, h_metrics)
        else:
            return self.activate_emergency_protocol(processed, h_metrics)
    
    def activate_emergency_protocol(self, data, metrics):
        """Apply deidentification tensor when H < 0.82"""
        tensor = DeidentificationTensor(reduction_factor=0.6)
        return tensor.apply(data, metrics)