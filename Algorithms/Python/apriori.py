
#algorithms_apriori:29_01_2025:

from itertools import combinations
from collections import Counter
from typing import List, Set, Tuple

type Transaction = List[str]

class Apriori:
  def __init__(self, support_threshold, confidence_threshold) -> None:
    self.global_counter = Counter()
    self.flag = True
    self.transaction_num: int
    self.support_threshold: float = support_threshold
    self.confidence_threshold: float = confidence_threshold
    self.discarded: List[Set] = []
    self.itemset_support_values = {}
    self.rules: List[Tuple[Set,Set]] = []
  

  def contains_discarded_subset(self, candidate: tuple):
    candidate_set = set(candidate)
    for discarded_candidate in self.discarded:
      if discarded_candidate.issubset(candidate_set):
        return True
    return False


  def generate_candidates(self, transactions: List[Transaction], k: int) -> List:
    counter = Counter()
    for transaction in transactions:
      sorted_transaction = sorted(transaction)
      counter += Counter(combinations(sorted_transaction,k))

    self.global_counter += counter


    filtered_candidates: List[Set] = []
    for candidate, count in counter.items():
      support = count / self.transaction_num
      if support >= self.support_threshold and not self.contains_discarded_subset(candidate):
        filtered_candidates.append(candidate)
      else:
        #print(f"we got a discard {candidate}")
        self.discarded.append(set(candidate))

    if len(filtered_candidates) == 0:
      print("finished")  
      self.flag = False

    return filtered_candidates

  def process_transactions(self, transactions: List[Transaction]):
    k = 1
    valid_itemsets: List[Set] = []
    self.transaction_num = len(transactions)
    while self.flag:
      generated_candidates = self.generate_candidates(transactions,k)   

      print(generated_candidates)
      valid_itemsets += generated_candidates
      k += 1

    for itemset in valid_itemsets:
      self.generate_rules(itemset)
      #self.calculate_support((itemset))


    for antecedent, consequent in self.rules:
      rule_confidence = self.calculate_confidence(antecedent, consequent)
      rule_lift = self.calculate_lift(antecedent, consequent)
      print(f"Reguła {antecedent} -> {consequent} \n confidence: {rule_confidence}, lift: {rule_lift} \n ---")

  def generate_rules(self, itemset: Set):
    for i in range(1,len(itemset)):
      for antecedent in combinations(itemset,i):
        antecedent = set(antecedent)
        consequent = set(itemset) - antecedent
        confidence = self.calculate_confidence(antecedent, consequent)
        if confidence >= self.confidence_threshold:
          print(f"generated rule {antecedent} -> {consequent}")
          self.rules.append((antecedent,consequent))

  def calculate_support(self, itemset: Set) -> float:
    itemset_counter_key = tuple(sorted(itemset))
    #print(f"ruleset: {itemset} appeared {self.global_counter[itemset_counter_key]} times")
    return self.global_counter[itemset_counter_key] / self.transaction_num

  def calculate_confidence(self, antecedent: Set, consequent: Set) -> float:
    union_support = self.calculate_support(antecedent | consequent)
    antecedent_support = self.calculate_support(antecedent)  
    return union_support / antecedent_support if antecedent_support > 0 else 0  
  
  def calculate_lift(self, antecedent: Set, consequent: Set) -> float:
    union_support = self.calculate_support(antecedent | consequent)
    antecedent_support = self.calculate_support(antecedent)
    consequent_support = self.calculate_support(consequent)
    if antecedent_support > 0 and consequent_support > 0:
        return union_support / (antecedent_support * consequent_support)  
    else:
      return 0
