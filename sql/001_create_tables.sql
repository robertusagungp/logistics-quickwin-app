CREATE TABLE IF NOT EXISTS shipment_master (
    shipment_id TEXT PRIMARY KEY,
    awb_no TEXT,
    order_time TIMESTAMP,
    pickup_requested_time TIMESTAMP,
    courier_assigned_time TIMESTAMP,
    pickup_actual_time TIMESTAMP,
    first_scan_time TIMESTAMP,
    arrived_origin_station_time TIMESTAMP,
    departed_origin_station_time TIMESTAMP,
    arrived_hub_time TIMESTAMP,
    departed_hub_time TIMESTAMP,
    out_for_delivery_time TIMESTAMP,
    delivered_time TIMESTAMP,
    promised_delivery_time TIMESTAMP,

    current_status TEXT,
    status_category TEXT,

    shipper_id TEXT,
    shipper_name TEXT,
    shipper_segment TEXT,

    origin_region TEXT,
    origin_station TEXT,
    origin_hub TEXT,

    destination_region TEXT,
    destination_station TEXT,
    destination_hub TEXT,

    lane_type TEXT,
    service_type TEXT,
    payment_type TEXT,

    courier_id TEXT,
    vehicle_type TEXT,

    weight_kg NUMERIC,
    volumetric_weight_kg NUMERIC,
    chargeable_weight_kg NUMERIC,

    declared_value_idr BIGINT,
    shipment_revenue_idr BIGINT,
    estimated_cost_idr BIGINT,

    pickup_sla_hours NUMERIC,
    pickup_on_time_flag INTEGER,
    failed_pickup_flag INTEGER,
    failed_pickup_reason TEXT,

    first_scan_timeliness_min INTEGER,

    promised_sla_hours NUMERIC,
    on_time_delivery_flag INTEGER,

    failed_delivery_flag INTEGER,
    failed_delivery_reason TEXT,
    delivery_attempts INTEGER,

    exception_flag INTEGER,
    exception_type TEXT,

    rts_flag INTEGER,
    rts_reason TEXT,

    aging_hours NUMERIC,
    dwell_origin_hours NUMERIC,
    dwell_hub_hours NUMERIC,

    last_scan_location TEXT,
    late_reason_bucket TEXT
);

CREATE TABLE IF NOT EXISTS shipment_event_log (
    event_id TEXT PRIMARY KEY,
    shipment_id TEXT REFERENCES shipment_master(shipment_id),
    event_sequence INTEGER,
    event_type TEXT,
    event_time TIMESTAMP,
    location_code TEXT,
    region TEXT,
    actor_type TEXT,
    actor_id TEXT,
    status_after_event TEXT,
    exception_reason TEXT,
    sla_breach_flag INTEGER
);
