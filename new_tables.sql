CREATE TABLE IF NOT EXISTS summary (
	summary_id TEXT PRIMARY KEY,
	account TEXT,
	sent_likes INT,
	sent_requests INT,
	sent_dm INT,
	end_date DATE DEFAULT now()
);

CREATE TABLE IF NOT EXISTS dm_profiles (
        profile_name TEXT,
        dm_message TEXT
);
