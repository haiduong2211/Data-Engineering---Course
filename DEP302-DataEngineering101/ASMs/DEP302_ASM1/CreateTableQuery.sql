USE DEP302_ASM1
Go
	
--Create DIM TABLES
CREATE TABLE PetType_Dim (
	PetTypeID int IDENTITY(1,1) PRIMARY KEY,
	Type varchar(3) NOT NULL
);

CREATE TABLE Breed_Dim(
	BreedID int IDENTITY(1,1) PRIMARY KEY,
	Breed varchar(255) NOT NULL
);

CREATE TABLE Gender_Dim (
	GenderID int IDENTITY(1,1) PRIMARY KEY,
	Gender varchar(6) NOT NULL
);

CREATE TABLE Color_Dim (
	ColorID int IDENTITY(1,1) PRIMARY KEY,
	Color varchar(255) NOT NULL
);

CREATE TABLE MaturitySize_Dim (
	MaturitySizeID int IDENTITY(1,1) PRIMARY KEY,
	MaturitySize varchar(13) NOT NULL
);

CREATE TABLE FurLength_Dim (
	FurLengthID int IDENTITY(1,1) PRIMARY KEY,
	FurLength varchar(13) NOT NULL
);

CREATE TABLE Health_Dim (
	HealthID int IDENTITY(1,1) PRIMARY KEY,
	Health varchar(14) NOT NULL,
	Vacinated varchar(8) NOT NULL,
	Dewormed varchar(8) NOT NULL,
	Sterilized varchar(8) NOT NULL
);

CREATE TABLE State_Dim (
	StateID int IDENTITY(1,1) PRIMARY KEY,
	State varchar(255) NOT NULL
);

-- CREATE FACT TABLE
GO
CREATE TABLE Pet_Fact (
	PetSurKey int IDENTITY(1,1) PRIMARY KEY,
	PetTypeID int NOT NULL,
	Breed1ID int NOT NULL,
	Breed2ID int NOT NULL,
	GenderID int NOT NULL,
	Color1ID int NOT NULL,
	Color2ID int NOT NULL,
	Color3ID int NOT NULL,
	MaturitySizeID int NOT NULL,
	FurlengthID int NOT NULL,
	HealthID int NOT NULL,
	StateID int NOT NULL,
	PetID int NOT NULL,
	Age int NOT NULL,
	Quantity INT NOT NULL,
	Fee int NOT NULL,
	RescuerID int NOT NULL,
	CONSTRAINT FK_Pet_Fact_Type_DIM FOREIGN KEY (PetTypeID) 
		REFERENCES PetType_DIM (PetTypeID)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	CONSTRAINT FK_Pet_Fact_Breed1 FOREIGN KEY (Breed1ID)
		REFERENCES Breed_Dim (BreedID)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	CONSTRAINT FK_Pet_Fact_Breed2 FOREIGN KEY (Breed2ID)
		REFERENCES Breed_Dim (BreedID)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION,
	CONSTRAINT FK_Pet_Fact_Gender FOREIGN KEY (GenderID)
		REFERENCES Gender_Dim (GenderID)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	CONSTRAINT FK_Pet_fact_Color1 FOREIGN KEY (Color1ID)
		REFERENCES Color_Dim (ColorID)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	CONSTRAINT FK_Pet_fact_Color2 FOREIGN KEY (Color2ID)
		REFERENCES Color_Dim (ColorID)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION,
	CONSTRAINT FK_Pet_fact_Color3 FOREIGN KEY (Color3ID)
		REFERENCES Color_Dim (ColorID)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION,
	CONSTRAINT FK_Pet_Fact_MaturitySize FOREIGN KEY (MaturitySizeID)
		REFERENCES MaturitySize_dim (MaturitySizeID)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	CONSTRAINT FK_Pet_Fact_FurLength FOREIGN KEY (FurLengthID)
		REFERENCES FurLength_Dim (FurLengthID)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	CONSTRAINT FK_Pet_Fact_Health FOREIGN KEY (HealtHID)
		REFERENCES Health_Dim (HealthID)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	CONSTRAINT FK_Pet_Fact_State FOREIGN KEY (StateID)
		REFERENCES State_dim (StateID)
		ON DELETE CASCADE
		ON UPDATE CASCADE
)
GO