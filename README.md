┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// ┃
// ┃  Lightpass is a growing tech company with many employees.

// ┃
// ┃  Each employee has:

// ┃    • An EID number (Employee ID)

// ┃    • A CRC value (Cumulative Report Count)

// ┃
// ┃  An employee's CRC is the total number of direct and indirect employees

// ┃  who report to them plus 1 (for themself). An employee with no reports

// ┃  has a CRC of 1

// ┃
// ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// ┌─────────────────────────────────────────────────────────────────────────
// │
// │  QUESTION 1

// │
// │  Given this sample direct report map of EIDs, what is the CRC for each

// │  employee?

// │
// │  {

// │    10: [20, 30],

// │    20: [40, 50],

// │    30: [],

// │    40: [],

// │    50: [],

// │  }

// │	Output CRC = 10:5 20:3 30:1 40:1 50:1

// └─────────────────────────────────────────────────────────────────────────
