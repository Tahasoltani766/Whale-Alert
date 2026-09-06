# 🐋 Whale-Alert

**Whale-Alert** is a research-oriented cryptocurrency transaction analysis project designed to investigate the potential market impact of large blockchain transactions.

The project focuses on more than simply detecting a large transaction. Its long-term goal is to combine **on-chain transaction history, trading activity, price data, centralized-exchange information, and analytical models** to estimate how a significant blockchain transaction may influence the market.

> ⚠️ **Project Status:** Research / Prototype
> This project is under active development. Several components are currently experimental or planned and should not be considered production-ready.

---

## 🎯 Project Goal

Large cryptocurrency transactions can sometimes have a significant effect on market behavior.

A large transfer may represent:

* Movement of funds between wallets
* Transfer to or from an exchange
* Whale accumulation
* Whale distribution
* Potential selling pressure
* Potential buying pressure
* Internal exchange movement
* Stablecoin movement
* Movement between known entities

Therefore, transaction size alone is not sufficient to determine its importance.

Whale-Alert aims to answer a more interesting question:

> **"Given a large blockchain transaction, what could be its potential impact on the market?"**

The project is designed around collecting relevant historical information and using that information to build an analytical model.

---

## 🧠 Concept

The planned analytical workflow is approximately:

```text
                 Blockchain Transaction
                          │
                          ▼
                    Data Collection
                          │
                          ▼
                       Database
                          │
              ┌───────────┴───────────┐
              │                       │
              ▼                       ▼
      Transaction History        Trading History
              │                       │
              └───────────┬───────────┘
                          ▼
                   Transaction
                     Analyzer
                          │
              ┌───────────┴───────────┐
              │                       │
              ▼                       ▼
       Transaction Impact       CEX Impact
              │                       │
              └───────────┬───────────┘
                          ▼
                    Feature Set
                          │
                          ▼
                    Model Creator
                          │
                          ▼
                  Impact Estimation
```

The internal analyzer documentation describes planned functionality around reading transaction data from the database, examining previous blocked transactions, examining recent trades, calculating transaction impact, and estimating influence on tokens traded on centralized exchanges.

---

# ✨ Main Components

## 1. Scraper

The `scraper` component is intended to provide the data-collection layer of the system.

Its responsibility is to collect relevant blockchain and market information and make it available to the rest of the pipeline.

Potential data sources include:

* Blockchain transaction data
* Wallet activity
* Token transfers
* Trading activity
* Market information

The scraper layer is designed to be extensible so that additional data providers can be integrated later.

---

## 2. Database

The `database` component is responsible for storing the information required by the analytical pipeline.

The database layer is intended to provide historical context for transactions and addresses.

This is important because a transaction cannot always be interpreted correctly in isolation.

For example:

```text
Transaction A
     │
     ├── Sender
     ├── Receiver
     ├── Token
     ├── Amount
     ├── Block
     └── Timestamp
```

becomes significantly more useful when combined with:

```text
Previous transactions
Previous balances
Trading activity
Exchange activity
Historical price
Address behavior
```

---

## 3. Transaction Analyzer

The `analyzor` module represents the analytical core of the project.

The planned workflow includes:

1. Reading transaction data from the database
2. Identifying the relevant address
3. Examining previous transactions
4. Examining recent trading activity
5. Calculating the potential impact of the transaction
6. Evaluating the potential impact on centralized exchanges
7. Passing the resulting information to the model layer

The project therefore attempts to move from simple:

```text
Large Transaction = Alert
```

toward:

```text
Large Transaction
       +
Historical Context
       +
Trading Context
       +
Exchange Context
       =
Potential Market Impact
```

---

## 4. CEX Analyzer

The `cex_analyzer` component is intended to analyze the relationship between on-chain activity and centralized-exchange activity.

A large transfer can have very different meanings depending on its destination.

For example:

```text
Whale Wallet
     │
     ├──────────────► Private Wallet
     │
     └──────────────► Exchange
```

These two transactions may have completely different implications.

The CEX analysis layer is therefore intended to provide additional context around exchange-related activity.

> **Current status:** The repository contains the component structure, but the current implementation is incomplete.

---

## 5. Price Data

The `price_data` component is intended to provide historical or market-price information required for transaction-impact analysis.

Price information can be used to contextualize a transaction by answering questions such as:

* What was the asset price when the transaction occurred?
* How large was the transaction relative to market conditions?
* Did market behavior change after the transaction?
* Was the transaction unusually large compared with historical activity?

---

## 6. Model Creator

The `model_creator` component represents the machine-learning/model layer of the project.

The intended architecture is:

```text
Raw Blockchain Data
        │
        ▼
Feature Extraction
        │
        ▼
Transaction Analysis
        │
        ▼
Market / CEX Analysis
        │
        ▼
Feature Set
        │
        ▼
Model
        │
        ▼
Impact Prediction
```

The long-term objective is to create a model capable of estimating the potential market significance of a transaction based on historical and contextual information.

---

## 7. Executor

The `executor` component is reserved for execution-related functionality within the project architecture.

At the current stage, this component should be considered experimental and is not documented as a production trading or automated execution system.

---

# 🔬 Research Direction

The project is particularly interested in the relationship between:

```text
On-chain behavior
        ↓
Exchange activity
        ↓
Market conditions
        ↓
Price movement
        ↓
Potential impact
```

A future version of the system could generate features such as:

### Transaction Features

* Transaction value
* Token amount
* USD value
* Sender address
* Receiver address
* Block number
* Timestamp
* Transaction frequency
* Historical transaction volume

### Wallet Features

* Wallet balance
* Historical balance
* Wallet age
* Number of transactions
* Historical inflow
* Historical outflow
* Counterparties
* Exchange interaction history

### Market Features

* Asset price
* Trading volume
* Volatility
* Market capitalization
* Liquidity
* Recent price movement

### Exchange Features

* Exchange destination
* Exchange inflow
* Exchange outflow
* Recent exchange volume
* Exchange-side liquidity

---

# 🏗️ Project Structure

```text
Whale-Alert/
│
├── .idea/
│
├── src/
│   │
│   ├── analyzor/
│   │   ├── analyzor.md
│   │   ├── types.py
│   │   └── __init__.py
│   │
│   ├── cex_analyzer/
│   │   ├── analyz_cexs.py
│   │   ├── cex_analyzer.md
│   │   └── __init__.py
│   │
│   ├── constans/
│   │
│   ├── database/
│   │   └── __init__.py
│   │
│   ├── error_handler/
│   │
│   ├── executor/
│   │   └── __init__.py
│   │
│   ├── model_creator/
│   │
│   ├── price_data/
│   │
│   ├── scraper/
│   │
│   ├── tests/
│   │
│   ├── __init__.py
│   ├── app.py
│   └── test.py
│
├── LICENSE
└── README.md
```

---

# 🔄 Intended Data Pipeline

The intended pipeline can be summarized as:

```text
                    ┌─────────────────┐
                    │ Blockchain Data │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │     Scraper     │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    Database     │
                    └────────┬────────┘
                             │
               ┌─────────────┴─────────────┐
               │                           │
               ▼                           ▼
      ┌─────────────────┐        ┌─────────────────┐
      │ Transaction     │        │ CEX Analyzer    │
      │ Analyzer        │        │                 │
      └────────┬────────┘        └────────┬────────┘
               │                          │
               └─────────────┬────────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  Feature Layer  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  Model Creator  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Impact Estimate │
                    └─────────────────┘
```

---

# 🚧 Current Development Status

The repository should currently be considered a **research prototype**.

Several architectural components have been created, but many are still incomplete.

For example, the internal analyzer documentation explicitly describes several future steps as TODO items, including database access, transaction-history analysis, trade analysis, impact calculation, CEX impact calculation, and returning the result to the model layer.

The current `app.py` also contains experimental data-processing code rather than a complete application entry point.

Therefore, the current repository is best understood as:

> **A research codebase exploring the architecture and algorithms required to build a cryptocurrency whale-transaction impact analysis system.**

---

# 🛣️ Roadmap

## Phase 1 — Data Collection

* [ ] Implement blockchain data ingestion
* [ ] Implement wallet tracking
* [ ] Normalize transaction data
* [ ] Store historical transactions
* [ ] Add timestamp normalization
* [ ] Add token metadata

## Phase 2 — Historical Analysis

* [ ] Address transaction history
* [ ] Wallet balance history
* [ ] Inflow/outflow analysis
* [ ] Transaction frequency
* [ ] Counterparty analysis

## Phase 3 — Market Analysis

* [ ] Historical price data
* [ ] Trading volume
* [ ] Volatility
* [ ] Liquidity metrics
* [ ] Price movement after large transactions

## Phase 4 — CEX Analysis

* [ ] Identify exchange addresses
* [ ] Detect exchange inflows
* [ ] Detect exchange outflows
* [ ] Correlate exchange activity with price
* [ ] Calculate exchange-related features

## Phase 5 — Impact Model

* [ ] Define feature set
* [ ] Build training dataset
* [ ] Define target variable
* [ ] Train baseline model
* [ ] Evaluate model
* [ ] Compare different models
* [ ] Add confidence score

## Phase 6 — Alerting

* [ ] Real-time transaction detection
* [ ] Transaction scoring
* [ ] Whale classification
* [ ] Impact classification
* [ ] Alert generation
* [ ] Notification integrations

---

# 📊 Potential Future Output

A future version could transform a raw transaction such as:

```text
Transaction
────────────
Token:       ETH
Value:       $5,000,000
From:        0x...
To:          0x...
Block:       19,717,698
```

into an analytical result such as:

```text
Whale Transaction Detected

Asset:             ETH
Transaction Value: $5.0M

Wallet Behavior:
  Historical Activity: High
  Exchange Interaction: Detected

Market Context:
  Volume:              ...
  Volatility:          ...
  Liquidity:           ...

Estimated Impact:
  Low / Medium / High

Confidence:
  ...
```

This represents the intended direction of the project rather than a claim about functionality currently implemented in the repository.

---

# 🧪 Development

Clone the repository:

```bash
git clone https://github.com/Tahasoltani766/Whale-Alert.git
cd Whale-Alert
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Linux/macOS:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install project dependencies when a finalized dependency file is available:

```bash
pip install -r requirements.txt
```

> **Note:** The current repository does not yet provide a complete production dependency/setup specification. The commands above describe the conventional Python environment setup and may require adjustment as the project evolves.

---

# 🧪 Research Philosophy

Whale-Alert is not intended to treat transaction size as the only indicator of importance.

Instead, the project explores a contextual approach:

```text
Transaction Size
       +
Wallet History
       +
Transaction History
       +
Market Data
       +
CEX Activity
       +
Historical Behavior
       ↓
Contextual Transaction Analysis
```

This distinction is important because a large transaction can have very different meanings depending on its context.

---

# ⚠️ Disclaimer

This project is intended for **research, educational, and analytical purposes**.

Predictions or estimated transaction impacts should not be interpreted as guaranteed market outcomes.

Cryptocurrency markets are highly volatile, and historical relationships do not necessarily imply future behavior.

The project does not provide financial advice.

---

# 📜 License

See [`LICENSE`](./LICENSE) for the applicable license.

---

# 👤 Author

**Taha Soltani**

GitHub: [@Tahasoltani766](https://github.com/Tahasoltani766)

Repository: [Whale-Alert](https://github.com/Tahasoltani766/Whale-Alert)

---

## ⭐ Project Vision

The long-term vision of Whale-Alert is to evolve from a simple large-transaction detector into a contextual blockchain intelligence system capable of answering:

> **What happened?**

> **Who was involved?**

> **What has this address done before?**

> **What is happening on exchanges?**

> **How unusual is this transaction?**

> **What could its potential market impact be?**

The ultimate goal is to combine **on-chain intelligence, market data, exchange activity, and machine learning** into a unified transaction-impact analysis pipeline.
