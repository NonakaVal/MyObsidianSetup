---
tags:
  - learning/review
HUB:
  - "[[hub-bi]]"
---
# Understanding Context in DAX Formulas

## 🧩 Three Types of Context
1. **Row Context** - Current row evaluation  
2. **Filter Context** - Applied filters  
3. **Query Context** - Overall evaluation environment  

## 🔍 Row Context Deep Dive
*Applies when formulas are evaluated row-by-row*

### Iterator Functions (X-functions)
```dax
SUMX(<table>, <expression>)  // Most common iterator
```

**Key Characteristics**:
- Identified by `X` suffix (SUMX, AVERAGEX, etc.)
- Creates implicit row context
- Processes tables row by row

**Example**:
```dax
SUMX(
    Sales, 
    Sales[Price] * (1 + Sales[Tax])
)  // Calculates taxed amount per row then sums
```

## 🎚️ Filter Context Explained
*Filters applied through:*
- Visual columns/rows  
- Slicers  
- Filter pane  
- DAX filter functions  

**Visualization Impact**:
```dax
Total Sales = SUM(Sales[Amount])  // Automatically respects visual filters
```

## 🛠️ CALCULATE Function
*Modifies filter context*

**Syntax**:
```dax
CALCULATE(
    <expression>,
    [filter1],
    [filter2],
    ...
)
```

**Common Patterns**:
```dax
// 1. Simple filter
CALCULATE(
    SUM(Sales[Amount]),
    Sales[Region] = "EMEA"
)

// 2. Multiple filters
CALCULATE(
    AVERAGE(Sales[Price]),
    Sales[Category] = "Electronics",
    Sales[Year] = 2023
)

// 3. Remove filters
CALCULATE(
    SUM(Sales[Qty]),
    ALL(Sales[Region])  // Ignores region filters
)
```

## ⚖️ Context Transition
*When row context becomes filter context*
```dax
// Measure example
Sales Tax = 
VAR Subtotal = SUMX(Sales, Sales[Qty] * Sales[Price])
RETURN
    Subtotal * [TaxRate]  // TaxRate measure needs filter context
```

## 💡 Pro Tips
1. Use `X`-functions for row-by-row calculations
2. `CALCULATE` is your most powerful tool for context manipulation
3. Watch for automatic context transition in measures
4. Test measures in different visual contexts
5. Use `FILTER` for complex filtering logic

> **Remember**: DAX always evaluates formulas within some context - explicit understanding leads to better measures!


Key improvements:
1. Added clear visual hierarchy with icons
2. Organized concepts from basic to advanced
3. Included practical code examples
4. Added context transition explanation
5. Provided professional tips
6. Maintained all original concepts
7. Improved readability with better spacing
8. Added syntax highlighting
9. Included common patterns
10. Added warning about implicit behaviors