const mongoose = require("mongoose");

const agentSchema = new mongoose.Schema({
    agencyName: { type: String, required: true },
    officialEmail: { type: String, required: true, unique: true },
    password: { type: String, required: true },
    phone: { type: String, required: true },
    address: { type: String, required: true }
});

const Agent = mongoose.models.Agent || mongoose.model("Agent", agentSchema);
module.exports = Agent;
