CREATE INDEX IF NOT EXISTS idx_shipment_order_time
    ON shipment_master(order_time);

CREATE INDEX IF NOT EXISTS idx_shipment_origin_station
    ON shipment_master(origin_station);

CREATE INDEX IF NOT EXISTS idx_shipment_destination_station
    ON shipment_master(destination_station);

CREATE INDEX IF NOT EXISTS idx_shipment_service_type
    ON shipment_master(service_type);

CREATE INDEX IF NOT EXISTS idx_shipment_current_status
    ON shipment_master(current_status);

CREATE INDEX IF NOT EXISTS idx_shipment_shipper_id
    ON shipment_master(shipper_id);

CREATE INDEX IF NOT EXISTS idx_event_shipment_id
    ON shipment_event_log(shipment_id);

CREATE INDEX IF NOT EXISTS idx_event_type
    ON shipment_event_log(event_type);

CREATE INDEX IF NOT EXISTS idx_event_time
    ON shipment_event_log(event_time);
