function loadEducation() {
	const bulkInsert = db.education.initializeUnorderedBulkOp();
	// Get all Documents in 'full' Collection
	const documents = db.full.find({});

	// Process each document
	documents.forEach(function (doc) {
		const element = {
			education: doc.education,
			education_num: doc.education_num
		};
		// Upsert into education Document
		bulkInsert.find(element).upsert().replaceOne(element);
	});
	bulkInsert.execute();
	return true;
}

function loadOccupation() {
	const bulkInsert = db.occupation.initializeUnorderedBulkOp();
	// Get all Documents in 'full' Collection
	const documents = db.full.find({});

	// Process each document
	documents.forEach(function (doc) {
		const element = {
			occupation: doc.occupation,
			workclass: doc.workclass
		};
		// Upsert into occupation Document
		bulkInsert.find(element).upsert().replaceOne(element);
	});
	bulkInsert.execute();
	return true;
}

function loadRelationship() {
	const bulkInsert = db.relationship.initializeUnorderedBulkOp();
	// Get all Documents in 'full' Collection
	const documents = db.full.find({});

	// Process each document
	documents.forEach(function (doc) {
		const element = {
			relationship: doc.relationship,
			marital_status: doc.marital_status
		};
		// Upsert into relationship Document
		bulkInsert.find(element).upsert().replaceOne(element);
	});
	bulkInsert.execute();
	return true;
}


function loadFinance() {
	const bulkInsert = db.finance.initializeUnorderedBulkOp();
	// Get all Documents in 'full' Collection
	const documents = db.full.find({});

	// Process each document
	documents.forEach(function (doc) {
		const element = {
			capital_gain: doc.capital_gain,
			captial_loss: doc.captial_loss,
			hours_per_week: doc.hours_per_week,
			income_bracket: doc.income_bracket
		};
		// Upsert into finance Document
		bulkInsert.find(element).upsert().replaceOne(element);
	});
	bulkInsert.execute();
	return true;
}