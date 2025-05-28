"""
# The Source of the Difference
When you assign + and - signs, you're literally subtracting one group from the other:
+a₁ - a₂ + a₃ - a₄ + a₅

Can be rewritten as:
(a₁ + a₃ + a₅) - (a₂ + a₄)

This is: sum of positive group MINUS sum of negative group

# The Core Answer
We take the difference because that's exactly what the original +/- expression computes!
When you write:
+2 +3 -1 -4 = target
You can regroup it as:
(2 + 3) - (1 + 4) = target
The subtraction in the original expression becomes the difference between the two subset sums!
Why This Isn't Obvious at First
The confusion happens because:

Original problem: "Assign + or - signs"
Transformed problem: "Find difference between subset sums"

It looks like two completely different operations, but they're mathematically identical!
The Key Insight
Every time you assign signs to numbers, you're implicitly:

Grouping numbers by their signs
Adding within each group
Subtracting one group total from the other

So "assign signs to get target" IS "partition into groups with target difference" - they're the same thing expressed differently!


"""

def show_why_difference():
    """Demonstrate why we take difference between subsets"""
    
    print("WHY DO WE TAKE THE DIFFERENCE?")
    print("=" * 35)
    
    # Example 1: Simple case
    print("EXAMPLE 1: nums = [2, 3, 1], target = 4")
    print()
    
    nums = [2, 3, 1]
    target = 4
    
    print("Let's try: +2 +3 -1")
    print("Step by step calculation:")
    print("  +2 = 2")
    print("  +2 +3 = 5") 
    print("  +2 +3 -1 = 4 ✓")
    print()
    
    print("Now let's group by signs:")
    print("  Positive group: {2, 3} → sum = 5")
    print("  Negative group: {1} → sum = 1")
    print("  Result: 5 - 1 = 4 ✓")
    print()
    
    print("THE KEY INSIGHT:")
    print("When we compute +2 +3 -1, we're actually computing:")
    print("(sum of positive numbers) - (sum of negative numbers)")
    print()
    
    # Example 2: More complex
    print("EXAMPLE 2: nums = [1, 1, 1, 1, 1], target = 3")
    print()
    
    nums2 = [1, 1, 1, 1, 1]
    target2 = 3
    
    assignments = [
        ([1, 1, 1, 1], [-1], "+1+1+1+1-1"),
        ([1, 1, 1], [-1, -1], "+1+1+1-1-1"), 
        ([1, 1, 1, 1], [-1], "+1+1-1+1+1")  # Different arrangement, same partition
    ]
    
    for pos_group, neg_group, expression in assignments:
        pos_sum = sum(pos_group)
        neg_sum = sum(abs(x) for x in neg_group)  # Remove negative signs for sum
        result = pos_sum - neg_sum
        
        print(f"Expression: {expression}")
        print(f"  Positive group: {pos_group} → sum = {pos_sum}")
        print(f"  Negative group: {[abs(x) for x in neg_group]} → sum = {neg_sum}")
        print(f"  Difference: {pos_sum} - {neg_sum} = {result}")
        print()

def show_mathematical_equivalence():
    """Show the mathematical equivalence step by step"""
    
    print("MATHEMATICAL EQUIVALENCE")
    print("=" * 25)
    
    print("Original expression with signs:")
    print("±a₁ ± a₂ ± a₃ ± a₄ ± a₅ = target")
    print()
    
    print("Group terms by their signs:")
    print("(terms with +) + (terms with -) = target")
    print()
    
    print("But negative terms are subtracted:")
    print("(terms with +) - (absolute value of terms with -) = target")
    print()
    
    print("This becomes:")
    print("sum(positive_subset) - sum(negative_subset) = target")
    print()
    
    print("THAT'S WHY WE TAKE THE DIFFERENCE!")
    print("The difference operation comes directly from the")
    print("subtraction in the original expression!")

def demonstrate_with_code():
    """Show this equivalence in code"""
    
    def calculate_with_signs(nums, signs):
        """Calculate result using +/- signs"""
        result = 0
        for i, sign in enumerate(signs):
            if sign == '+':
                result += nums[i]
            else:  # sign == '-'
                result -= nums[i]
        return result
    
    def calculate_with_partition(nums, positive_indices):
        """Calculate result using subset partition"""
        pos_sum = sum(nums[i] for i in positive_indices)
        neg_sum = sum(nums[i] for i in range(len(nums)) if i not in positive_indices)
        return pos_sum - neg_sum
    
    print("CODE DEMONSTRATION")
    print("=" * 18)
    
    nums = [2, 3, 1, 4]
    
    # Method 1: Using signs
    signs = ['+', '+', '-', '-']
    result1 = calculate_with_signs(nums, signs)
    
    # Method 2: Using partition (same result!)
    positive_indices = [0, 1]  # indices where we had '+' signs
    result2 = calculate_with_partition(nums, positive_indices)
    
    print(f"nums = {nums}")
    print(f"signs = {signs}")
    print()
    print(f"Method 1 (signs): {signs[0]}{nums[0]} {signs[1]}{nums[1]} {signs[2]}{nums[2]} {signs[3]}{nums[3]} = {result1}")
    print()
    print(f"Method 2 (partition):")
    pos_indices = [i for i, sign in enumerate(signs) if sign == '+']
    neg_indices = [i for i, sign in enumerate(signs) if sign == '-']
    pos_values = [nums[i] for i in pos_indices]
    neg_values = [nums[i] for i in neg_indices]
    print(f"  Positive subset: {pos_values} (sum = {sum(pos_values)})")
    print(f"  Negative subset: {neg_values} (sum = {sum(neg_values)})")
    print(f"  Difference: {sum(pos_values)} - {sum(neg_values)} = {result2}")
    print()
    print(f"Both methods give: {result1} = {result2} ✓")

def the_aha_moment():
    """The final 'aha' explanation"""
    
    print("THE 'AHA!' MOMENT")
    print("=" * 17)
    
    print("When you write: +a - b + c - d")
    print("You're not adding and subtracting randomly...")
    print()
    print("You're computing:")
    print("  (a + c) - (b + d)")
    print("   ↑       ↑")
    print("   |       └─ sum of numbers that got minus signs")
    print("   └─ sum of numbers that got plus signs")
    print()
    print("So the TARGET SUM problem is asking:")
    print("'How many ways can you split the array into two groups")
    print("such that (group1_sum - group2_sum) equals the target?'")
    print()
    print("That's why we take the DIFFERENCE between subsets!")
    print("It comes directly from the +/- operations in the original problem!")

# Run all explanations
show_why_difference()
print("\n" + "="*50 + "\n")
show_mathematical_equivalence()
print("\n" + "="*50 + "\n")
demonstrate_with_code()
print("\n" + "="*50 + "\n")
the_aha_moment()