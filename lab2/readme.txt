Accountant 0 2 -> Report Company
Admin 1 2 -> Client 
BookingAgent 2 4 -> Client Tour
Client 5 4 -> Tour BankCard Validator
Employee 4 3 -> Validator
Guide 1 2 -> Route Excursion
Manager 1 3 -> Tour Client BookingAgent
SupportSpecialist 1 2 -> 
Account 4 3 -> Validator
AnalyticsSystem 2 2 -> Company MarketingCampaign
Auditlog 2 3 -> Validator 
Authorization 3 4 -> Validator
BankCard 4 7 -> Date Validator
BookingCalendar 4 3 -> Validator Date Tour
BookingSystem 2 4 -> Validator Tour
ClientWallet 2 3 -> Validator
Company 6 5 -> Validator Contract Client Manager
Contract 6 1 -> Validator Date Manager
Currency 3 2 -> Validator 
Discount 3 2 -> Validator Client Tour
FinancialReport 3 2 -> Validator Company
Invoice 6 2 -> Validator Client Tour
Mailing 5 2 -> Validator NotificationService
MailingSender 4 2 -> Validator NotoficationService 
MarketingCampaign 6 2 -> Validator NotificationService
NotificationService 4 2 -> Validator 
Partner 5 1 -> Validator TourCatalog
Payment 4 3 -> Validator PaymentSystem BankCard
PaymentSystem 4 1 -> Validator BankCard Payment Date
PromoCode 5 2 -> Validator Date Client
Refund 5 2 -> Validator Payment
RefundProcessing 2 1 -> Validator Payment
Supplier 4 2 -> Validator
UserRegistration 4 2 -> Validator 
Excursion 5 0 -> Guide Route
Factory 0 5 -> Room Client Tour Hotel BankCard Date
Flight 4 1 -> Validator Date Transport
Hotel 4 2 -> Validator Room Date
HotelRating 3 1 -> Review Validator 
LoyaltyProgram 3 3 -> Validator ClientWallet
Review 4 2 -> Validator
Room 4 2 -> Validator Date
Route 4 2 -> Transport
Ticket 4 1 -> Validator Flight Date
Tour 5 0 -> Validator Hotel Route
TourCatalog 3 1 -> Validator Tour
TourSearch 2 2 -> TourCatalog 
Transport 5 2 -> Validator Route
Date 3 7 -> 
Validator 0 3 ->

InvalidPasswordException 0 0 -> 
InsufficientFundsException 0 0 ->
TourNotFoundException 0 0 ->
HotelNotAvailableException 0 0 -> 
BookingAlreadyExistsException 0 0 -> 
CardExpiredException 0 0 -> 
InvalidEmailException 0 0 ->
UnauthorizedAccessException 0 0 -> 
PaymentFailedException 0 0 -> 
GuideNotFoundException 0 0 ->
TransportDelayException 0 0 -> 
ContractViolationException 0 0 ->

Классов: 50
Исключений: 12
Поля: 170
Поведения: 121
Ассоциации: 101
