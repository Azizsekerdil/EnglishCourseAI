"""Built-in English learner's dictionary (A1-B1, ~900 entries).

Line format:  headword|pos [extra]|turkish; turkish 2|short English definition
The definition is written in simple English so the entry doubles as a
monolingual learner's dictionary; the Turkish column gives the meaning.
Irregular verb forms are appended to the definition after ' — '.
"""

DATA = r"""
# ---- greetings / politeness ----
hello|int|merhaba|a greeting used when you meet someone
hi|int|selam|an informal greeting
good morning|phr|günaydın|a greeting used in the morning
good afternoon|phr|tünaydın; iyi günler|a greeting used after midday
good evening|phr|iyi akşamlar|a greeting used in the evening
good night|phr|iyi geceler|said when leaving at night or going to bed
goodbye|int|hoşça kal; güle güle|said when you leave someone
bye|int|hoşça kal|informal goodbye
see you later|phr|sonra görüşürüz|informal goodbye for a short time
thank you|phr|teşekkür ederim|polite words to show you are grateful
thanks|int|teşekkürler|informal thank you
please|adv|lütfen|polite word used when asking for something
you're welcome|phr|rica ederim|polite reply to thank you
sorry|adj|üzgünüm; özür dilerim|feeling regret; used to apologise
excuse me|phr|affedersiniz|polite way to get attention or apologise
yes|adv|evet|used to agree or say something is true
no|adv|hayır|used to refuse or say something is not true
okay|adv|tamam|all right; used to agree
of course|phr|elbette; tabii ki|certainly; used to say yes strongly
maybe|adv|belki|possibly; perhaps
welcome|int|hoş geldiniz|a friendly greeting to someone who arrives
congratulations|int|tebrikler|said to praise someone for a success
good luck|phr|iyi şanslar|said to wish someone success
happy birthday|phr|doğum günün kutlu olsun|said to someone on their birthday
cheers|int|şerefe|said when raising a drink; informal thanks
bless you|phr|çok yaşa|said when someone sneezes
how are you|phr|nasılsın; nasılsınız|question asking about someone's health or mood
what's your name|phr|adın ne|question asking someone's name
my name is|phr|benim adım|used to say your name
I'm from|phr|…denim; …dan geliyorum|used to say where you come from
I don't understand|phr|anlamıyorum|said when you cannot understand
I don't know|phr|bilmiyorum|said when you have no information
pardon|int|efendim; affedersiniz|used to ask someone to repeat
can you repeat that|phr|tekrar eder misiniz|request to say something again
how much is it|phr|ne kadar|question asking the price
where is|phr|nerede|question asking a place
I would like|phr|istiyorum; rica ediyorum|polite way to say what you want
there is|phr|var|used to say something exists (singular)
there are|phr|var (çoğul)|used to say things exist (plural)
# ---- question words ----
who|pron|kim|which person
what|pron|ne|which thing
where|adv|nerede|in or to which place
when|adv|ne zaman|at what time
why|adv|neden; niçin|for what reason
how|adv|nasıl|in what way
which|pron|hangi|used to choose between things
whose|pron|kimin|belonging to which person
how much|phr|ne kadar|question about amount or price
how many|phr|kaç tane|question about number
how old|phr|kaç yaşında|question about age
# ---- pronouns / articles ----
I|pron|ben|the person speaking
you|pron|sen; siz|the person spoken to
he|pron|o (erkek)|a male person already mentioned
she|pron|o (kadın)|a female person already mentioned
it|pron|o (nesne)|a thing or animal already mentioned
we|pron|biz|the speaker and others
they|pron|onlar|people or things already mentioned
me|pron|beni; bana|object form of I
him|pron|onu; ona (erkek)|object form of he
her|pron|onu; ona; onun (kadın)|object form of she; belonging to her
us|pron|bizi; bize|object form of we
them|pron|onları; onlara|object form of they
my|pron|benim|belonging to me
your|pron|senin; sizin|belonging to you
his|pron|onun (erkek)|belonging to him
its|pron|onun (nesne)|belonging to it
our|pron|bizim|belonging to us
their|pron|onların|belonging to them
mine|pron|benimki|the one belonging to me
yours|pron|seninki; sizinki|the one belonging to you
myself|pron|kendim|reflexive form of I
yourself|pron|kendin|reflexive form of you
this|pron|bu|the thing near the speaker
that|pron|şu; o|the thing farther from the speaker
these|pron|bunlar|plural of this
those|pron|şunlar; onlar|plural of that
the|art|(belirli tanımlık)|used before a noun already known
a|art|bir (belirsiz tanımlık)|used before a singular noun; one
an|art|bir (sesli harften önce)|form of a used before a vowel sound
some|pron|biraz; bazı|an amount or number that is not exact
any|pron|hiç; herhangi|used in questions and negatives for some
every|pron|her|each one of a group
each|pron|her biri|every single one, considered separately
all|pron|hepsi; bütün|the whole number or amount
everything|pron|her şey|all things
something|pron|bir şey|a thing that is not named
nothing|pron|hiçbir şey|not anything
anything|pron|herhangi bir şey|any thing
everyone|pron|herkes|all people
someone|pron|birisi|a person who is not named
nobody|pron|hiç kimse|no person
each other|phr|birbirini|used when two people do the same thing to the other
one|pron|biri; bir tane|a single person or thing; used instead of a noun
another|pron|başka bir; bir tane daha|one more; a different one
other|adj|diğer; öbür|different from the one already mentioned
# ---- numbers ----
zero|num|sıfır|the number 0
one|num|bir|the number 1
two|num|iki|the number 2
three|num|üç|the number 3
four|num|dört|the number 4
five|num|beş|the number 5
six|num|altı|the number 6
seven|num|yedi|the number 7
eight|num|sekiz|the number 8
nine|num|dokuz|the number 9
ten|num|on|the number 10
eleven|num|on bir|the number 11
twelve|num|on iki|the number 12
thirteen|num|on üç|the number 13
fourteen|num|on dört|the number 14
fifteen|num|on beş|the number 15
sixteen|num|on altı|the number 16
seventeen|num|on yedi|the number 17
eighteen|num|on sekiz|the number 18
nineteen|num|on dokuz|the number 19
twenty|num|yirmi|the number 20
thirty|num|otuz|the number 30
forty|num|kırk|the number 40
fifty|num|elli|the number 50
sixty|num|altmış|the number 60
seventy|num|yetmiş|the number 70
eighty|num|seksen|the number 80
ninety|num|doksan|the number 90
hundred|num|yüz|the number 100
thousand|num|bin|the number 1,000
million|num|milyon|the number 1,000,000
first|num|birinci; ilk|coming before all others
second|num|ikinci|coming after the first
third|num|üçüncü|coming after the second
last|adj|son; sonuncu|coming after all others; most recent
half|n|yarım; yarısı|one of two equal parts
quarter|n|çeyrek|one of four equal parts
once|adv|bir kez|one time
twice|adv|iki kez|two times
many|pron|çok; birçok|a large number
much|adv|çok (sayılamayan)|a large amount
few|pron|az; birkaç|a small number
a few|phr|birkaç|a small number, but some
a little|phr|biraz|a small amount
several|pron|birkaç; birçok|more than two but not many
enough|adv|yeterli; yeterince|as much as is needed
# ---- time ----
time|n|zaman; saat|the passing of minutes, hours and days; the hour
hour|n|saat (süre)|sixty minutes
minute|n|dakika|sixty seconds
second|n|saniye|one sixtieth of a minute
day|n|gün|twenty-four hours; the time when it is light
night|n|gece|the time when it is dark
morning|n|sabah|the early part of the day
afternoon|n|öğleden sonra|the part of the day after noon
evening|n|akşam|the part of the day before night
noon|n|öğle|twelve o'clock in the day
midnight|n|gece yarısı|twelve o'clock at night
week|n|hafta|seven days
weekend|n|hafta sonu|Saturday and Sunday
month|n|ay|one of the twelve parts of a year
year|n|yıl; sene|twelve months
century|n|yüzyıl|one hundred years
today|adv|bugün|this day
tomorrow|adv|yarın|the day after today
yesterday|adv|dün|the day before today
now|adv|şimdi|at this moment
soon|adv|yakında|in a short time
later|adv|sonra; daha sonra|after the present time
early|adv|erken|before the usual time
late|adv|geç|after the usual time
always|adv|her zaman; daima|at all times
never|adv|asla; hiç|not at any time
sometimes|adv|bazen|at some times, not always
often|adv|sık sık|many times
rarely|adv|nadiren|not often
usually|adv|genellikle|most of the time
already|adv|zaten; çoktan|before now
still|adv|hâlâ|continuing until now
yet|adv|henüz|until now (in questions and negatives)
again|adv|tekrar; yine|one more time
first|adv|önce; ilk olarak|before anything else
then|adv|sonra; o zaman|next; at that time
finally|adv|sonunda|at the end; at last
suddenly|adv|aniden|quickly and without warning
ago|adv|önce (geçmişte)|before now, measured from the present
Monday|n|pazartesi|the first day of the working week
Tuesday|n|salı|the day after Monday
Wednesday|n|çarşamba|the day after Tuesday
Thursday|n|perşembe|the day after Wednesday
Friday|n|cuma|the day after Thursday
Saturday|n|cumartesi|the day after Friday
Sunday|n|pazar|the day after Saturday
January|n|ocak|the first month of the year
February|n|şubat|the second month of the year
March|n|mart|the third month of the year
April|n|nisan|the fourth month of the year
May|n|mayıs|the fifth month of the year
June|n|haziran|the sixth month of the year
July|n|temmuz|the seventh month of the year
August|n|ağustos|the eighth month of the year
September|n|eylül|the ninth month of the year
October|n|ekim|the tenth month of the year
November|n|kasım|the eleventh month of the year
December|n|aralık|the twelfth month of the year
spring|n|ilkbahar|the season after winter
summer|n|yaz|the warmest season
autumn|n|sonbahar|the season after summer (US: fall)
winter|n|kış|the coldest season
holiday|n|tatil; bayram|a day or period when you do not work
birthday|n|doğum günü|the day you were born, each year
appointment|n|randevu|an arranged meeting at a fixed time
calendar|n|takvim|a list of the days and months of a year
date|n|tarih|a particular day of the month or year
# ---- family / people ----
person|n|kişi|a human being — plural: people
people|n|insanlar|men, women and children
man|n|adam; erkek|an adult male — plural: men
woman|n|kadın|an adult female — plural: women
child|n|çocuk|a young person — plural: children
boy|n|erkek çocuk|a male child
girl|n|kız|a female child
baby|n|bebek|a very young child
family|n|aile|parents and their children
parents|n|anne baba; ebeveyn|a mother and father
mother|n|anne|a female parent
father|n|baba|a male parent
mum|n|anne (samimi)|informal word for mother (US: mom)
dad|n|baba (samimi)|informal word for father
son|n|oğul|a male child of a parent
daughter|n|kız evlat|a female child of a parent
brother|n|erkek kardeş|a male with the same parents
sister|n|kız kardeş|a female with the same parents
grandmother|n|büyükanne; nine|the mother of your parent
grandfather|n|büyükbaba; dede|the father of your parent
grandparents|n|büyükanne ve büyükbaba|the parents of your parents
grandson|n|erkek torun|the son of your child
granddaughter|n|kız torun|the daughter of your child
uncle|n|amca; dayı; enişte|the brother of your parent
aunt|n|teyze; hala; yenge|the sister of your parent
cousin|n|kuzen|the child of your uncle or aunt
husband|n|koca|the man a woman is married to
wife|n|eş; karı|the woman a man is married to — plural: wives
friend|n|arkadaş|a person you like and know well
boyfriend|n|erkek arkadaş|a man someone is in a romantic relationship with
girlfriend|n|kız arkadaş|a woman someone is in a romantic relationship with
neighbour|n|komşu|a person who lives next to you (US: neighbor)
guest|n|misafir|a person invited to your home or event
colleague|n|iş arkadaşı; meslektaş|a person you work with
boss|n|patron|the person in charge at work
name|n|isim; ad|the word you are called by
surname|n|soyadı|your family name
age|n|yaş|how old someone is
adult|n|yetişkin|a fully grown person
teenager|n|genç (13-19)|a person between 13 and 19 years old
young|adj|genç|not old
old|adj|yaşlı; eski|having lived a long time; not new
# ---- jobs ----
job|n|iş; meslek|the work you do for money
work|n|iş; çalışma|activity you do to earn money
profession|n|meslek|a job that needs training
doctor|n|doktor|a person who treats sick people
teacher|n|öğretmen|a person who teaches
student|n|öğrenci|a person who studies
pupil|n|öğrenci (okul)|a child at school
engineer|n|mühendis|a person who designs machines or structures
programmer|n|programcı|a person who writes computer programs
shop assistant|n|tezgâhtar|a person who serves customers in a shop
cook|n|aşçı|a person who prepares food
chef|n|şef (aşçıbaşı)|a professional cook in a restaurant
waiter|n|garson|a man who serves food in a restaurant
waitress|n|kadın garson|a woman who serves food in a restaurant
driver|n|sürücü; şoför|a person who drives a vehicle
police officer|n|polis memuru|a member of the police
journalist|n|gazeteci|a person who writes news
artist|n|sanatçı|a person who makes art
musician|n|müzisyen|a person who plays music
actor|n|oyuncu (erkek)|a man who acts in films or plays
actress|n|oyuncu (kadın)|a woman who acts in films or plays
writer|n|yazar|a person who writes books
lawyer|n|avukat|a person trained in law
baker|n|fırıncı|a person who makes bread
hairdresser|n|kuaför|a person who cuts hair
nurse|n|hemşire|a person who cares for sick people
worker|n|işçi|a person who works, especially by hand
mechanic|n|tamirci|a person who repairs machines
secretary|n|sekreter|a person who does office work
farmer|n|çiftçi|a person who works on a farm
scientist|n|bilim insanı|a person who studies science
translator|n|çevirmen|a person who translates writing
company|n|şirket|a business organisation
office|n|ofis|a room where people work at desks
factory|n|fabrika|a building where things are made
salary|n|maaş|money paid for work each month
customer|n|müşteri|a person who buys something
meeting|n|toplantı|when people come together to discuss
contract|n|sözleşme|a written legal agreement
application|n|başvuru; uygulama|a formal request for a job; a program
interview|n|mülakat; röportaj|a formal meeting with questions
unemployed|adj|işsiz|without a job
career|n|kariyer|your working life
# ---- home ----
house|n|ev|a building where people live
home|n|ev; yuva|the place where you live
flat|n|daire|a set of rooms on one floor (US: apartment)
apartment|n|daire; apartman dairesi|a set of rooms in a building
room|n|oda|a part of a building with walls
kitchen|n|mutfak|the room where you cook
bedroom|n|yatak odası|the room where you sleep
living room|n|oturma odası|the room where you relax
bathroom|n|banyo|the room with a bath or shower
toilet|n|tuvalet|the room or bowl used for going to the toilet
hall|n|koridor; salon|the area inside the front door; a large room
balcony|n|balkon|a platform outside an upper window
garden|n|bahçe|land next to a house with plants
basement|n|bodrum|the floor of a building below ground
roof|n|çatı|the top covering of a building
floor|n|zemin; kat|the surface you walk on; a level of a building
stairs|n|merdiven|steps that go up to another floor
lift|n|asansör|a machine that carries people between floors (US: elevator)
door|n|kapı|you open it to enter a room
window|n|pencere|an opening with glass in a wall
wall|n|duvar|the side of a room or building
ceiling|n|tavan|the top surface of a room
furniture|n|mobilya|tables, chairs, beds and so on
table|n|masa|a flat surface with legs
chair|n|sandalye|a seat for one person
armchair|n|koltuk|a comfortable chair with arms
sofa|n|kanepe|a long soft seat for several people
bed|n|yatak|the thing you sleep on
wardrobe|n|gardırop|a tall cupboard for clothes
cupboard|n|dolap|a piece of furniture with shelves and doors
shelf|n|raf|a flat board for keeping things on — plural: shelves
mirror|n|ayna|glass that shows your image
lamp|n|lamba|a device that gives light
light|n|ışık|the energy that lets you see
carpet|n|halı|thick material covering a floor
picture|n|resim|a painting, drawing or photo
fridge|n|buzdolabı|a machine that keeps food cold
cooker|n|ocak|a device for cooking food (US: stove)
oven|n|fırın|the closed box where food is baked
washing machine|n|çamaşır makinesi|a machine for washing clothes
television|n|televizyon|a device for watching programmes
key|n|anahtar|a metal object that opens a lock
rubbish|n|çöp|things you throw away (US: garbage)
rent|n|kira|money paid to live in a house
neighbourhood|n|mahalle|the area around your home
tidy up|phr|toplamak; düzenlemek|to make a place neat
clean|v|temizlemek|to remove dirt
wash|v|yıkamak|to clean with water
cook|v|yemek pişirmek|to prepare food with heat
live|v|yaşamak; oturmak|to be alive; to have your home somewhere
move|v|taşınmak; hareket etmek|to change your home; to change position
# ---- everyday objects ----
thing|n|şey|any object or idea
bag|n|çanta|a container for carrying things
backpack|n|sırt çantası|a bag carried on your back
suitcase|n|bavul|a case for carrying clothes when travelling
wallet|n|cüzdan|a small case for money and cards
money|n|para|coins and notes used to buy things
phone|n|telefon|a device for calling people
mobile phone|n|cep telefonu|a phone you carry with you
computer|n|bilgisayar|an electronic machine for storing and processing data
laptop|n|dizüstü bilgisayar|a small computer you can carry
glasses|n|gözlük|lenses worn to help you see
umbrella|n|şemsiye|a thing that protects you from rain
book|n|kitap|pages with writing joined together
notebook|n|defter|a book with empty pages for writing
pen|n|kalem (tükenmez)|a tool for writing with ink
pencil|n|kurşun kalem|a tool for writing with graphite
paper|n|kâğıt|thin material for writing on
letter|n|mektup; harf|a written message you send; a symbol of the alphabet
newspaper|n|gazete|printed news sold every day
magazine|n|dergi|a thin book with articles and pictures
photo|n|fotoğraf|a picture made with a camera
present|n|hediye; şimdiki zaman|something you give to someone; the time now
gift|n|hediye; armağan|a present
toy|n|oyuncak|a thing for children to play with
ball|n|top|a round object used in games
watch|n|kol saati|a small clock worn on the wrist
card|n|kart|a small piece of stiff paper or plastic
box|n|kutu|a container with straight sides
bottle|n|şişe|a container for liquids with a narrow neck
# ---- clothing ----
clothes|n|giysiler; kıyafet|things you wear
dress|n|elbise|a piece of clothing for women that covers the body and legs
shirt|n|gömlek|a piece of clothing with buttons for the upper body
T-shirt|n|tişört|a soft shirt with short sleeves
trousers|n|pantolon|clothing for the legs (US: pants)
jeans|n|kot pantolon|trousers made of denim
skirt|n|etek|a piece of clothing that hangs from the waist
coat|n|palto; kaban|a warm piece of clothing worn outside
jacket|n|ceket|a short coat
suit|n|takım elbise|a jacket and trousers of the same material
sweater|n|kazak|a warm piece of clothing for the upper body
hat|n|şapka|a covering for the head
cap|n|kep; şapka|a soft hat with a peak
scarf|n|atkı; eşarp|cloth worn around the neck
glove|n|eldiven|a covering for the hand
sock|n|çorap|a covering for the foot
shoe|n|ayakkabı|a covering for the foot with a hard sole
boot|n|bot; çizme|a shoe that covers the ankle
trainers|n|spor ayakkabı|shoes for sport (US: sneakers)
size|n|beden; boyut|how big something is
put on|phr|giymek|to place clothes on your body
take off|phr|çıkarmak (giysi); kalkış yapmak|to remove clothes; to leave the ground (plane)
wear|v|giymek; takmak|to have clothes on your body — wore, worn
try on|phr|denemek (giysi)|to put on clothes to see if they fit
# ---- body / health ----
body|n|vücut; beden|the whole physical form of a person
head|n|baş; kafa|the part of the body with the brain and face
face|n|yüz|the front of the head
eye|n|göz|the organ you see with
ear|n|kulak|the organ you hear with
nose|n|burun|the organ you smell with
mouth|n|ağız|the opening you eat and speak with
tooth|n|diş|one of the hard white things in your mouth — plural: teeth
hair|n|saç|the fine threads that grow on your head
neck|n|boyun|the part between head and shoulders
throat|n|boğaz|the passage inside the neck
shoulder|n|omuz|the part where the arm joins the body
arm|n|kol|the part between shoulder and hand
hand|n|el|the part at the end of the arm
finger|n|parmak|one of the five parts of the hand
leg|n|bacak|the part between hip and foot
foot|n|ayak|the part at the end of the leg — plural: feet
knee|n|diz|the joint in the middle of the leg
back|n|sırt|the rear part of the body
stomach|n|mide; karın|the organ where food goes
heart|n|kalp|the organ that pumps blood
blood|n|kan|the red liquid in the body
skin|n|deri; cilt|the outer covering of the body
health|n|sağlık|the condition of the body
healthy|adj|sağlıklı|not ill; good for the body
ill|adj|hasta|not healthy (US: sick)
sick|adj|hasta|ill; wanting to vomit
illness|n|hastalık|a disease or period of being ill
disease|n|hastalık|an illness with a name
pain|n|ağrı; acı|the feeling when part of your body hurts
headache|n|baş ağrısı|a pain in the head
fever|n|ateş (hastalık)|a body temperature that is too high
cold|n|soğuk algınlığı; nezle|a common illness with a runny nose
cough|n|öksürük|the act of pushing air out noisily
medicine|n|ilaç|something you take to treat illness
pill|n|hap|a small solid piece of medicine
pharmacy|n|eczane|a shop that sells medicine
hospital|n|hastane|a place where sick people are treated
emergency|n|acil durum|a sudden dangerous situation
ambulance|n|ambulans|a vehicle that carries sick people
accident|n|kaza|something bad that happens by chance
tired|adj|yorgun|needing rest or sleep
sleep|v|uyumak|to rest with your eyes closed — slept, slept
fall asleep|phr|uykuya dalmak|to start sleeping
wake up|phr|uyanmak|to stop sleeping — woke, woken
get up|phr|kalkmak (yataktan)|to leave your bed
rest|v|dinlenmek|to relax and do nothing
hurt|v|acıtmak; incitmek; ağrımak|to cause pain; to feel pain — hurt, hurt
# ---- food / drink ----
food|n|yiyecek; yemek|things people eat
meal|n|öğün; yemek|food eaten at one time
breakfast|n|kahvaltı|the first meal of the day
lunch|n|öğle yemeği|the meal in the middle of the day
dinner|n|akşam yemeği|the main meal, usually in the evening
bread|n|ekmek|food made from flour and baked
butter|n|tereyağı|yellow fat made from milk
cheese|n|peynir|solid food made from milk
milk|n|süt|white liquid from cows
egg|n|yumurta|an oval object laid by a bird, eaten as food
meat|n|et|the flesh of animals used as food
chicken|n|tavuk|a farm bird; its meat
fish|n|balık|an animal that lives in water; its meat
sausage|n|sosis|meat in a thin tube
soup|n|çorba|liquid food eaten with a spoon
rice|n|pirinç; pilav|small white grains cooked as food
pasta|n|makarna|Italian food made from flour, like spaghetti
potato|n|patates|a round vegetable that grows underground — plural: potatoes
chips|n|patates kızartması|fried strips of potato (US: French fries)
vegetable|n|sebze|a plant eaten as food
fruit|n|meyve|the sweet part of a plant with seeds
apple|n|elma|a round fruit, red or green
pear|n|armut|a sweet fruit narrow at the top
banana|n|muz|a long yellow fruit
orange|n|portakal|a round orange citrus fruit
lemon|n|limon|a sour yellow fruit
grape|n|üzüm|a small fruit growing in bunches
strawberry|n|çilek|a small red soft fruit
tomato|n|domates|a red juicy vegetable — plural: tomatoes
cucumber|n|salatalık|a long green vegetable eaten in salads
onion|n|soğan|a round vegetable with strong smell
garlic|n|sarımsak|a plant with a strong taste used in cooking
salad|n|salata|a dish of raw vegetables
carrot|n|havuç|a long orange vegetable
mushroom|n|mantar|a fungus eaten as food
salt|n|tuz|a white substance that makes food taste
sugar|n|şeker|a sweet substance
pepper|n|karabiber; biber|a hot spice; a vegetable
oil|n|yağ|a liquid fat used in cooking
honey|n|bal|a sweet substance made by bees
cake|n|pasta; kek|a sweet baked food
biscuit|n|bisküvi|a small flat dry cake (US: cookie)
chocolate|n|çikolata|a sweet brown food
ice cream|n|dondurma|a frozen sweet food
sweet|n|şeker (tatlı); tatlı|a small piece of sugary food (US: candy)
water|n|su|the clear liquid you drink
tea|n|çay|a hot drink made from dried leaves
coffee|n|kahve|a hot drink made from roasted beans
juice|n|meyve suyu|the liquid from fruit
beer|n|bira|an alcoholic drink made from grain
wine|n|şarap|an alcoholic drink made from grapes
glass|n|bardak; cam|a container for drinking; the material of windows
cup|n|fincan|a small container with a handle for hot drinks
plate|n|tabak|a flat dish for food
spoon|n|kaşık|a tool for eating liquid food
fork|n|çatal|a tool with points for eating
knife|n|bıçak|a tool with a blade for cutting — plural: knives
pan|n|tava|a metal container for cooking
pot|n|tencere|a deep container for cooking
restaurant|n|restoran; lokanta|a place where you buy and eat meals
café|n|kafe|a small place selling drinks and light food
bakery|n|fırın (dükkân)|a shop that sells bread
menu|n|menü|the list of food in a restaurant
bill|n|hesap; fatura|a paper showing how much to pay (US: check)
tip|n|bahşiş; ipucu|extra money for service; a useful piece of advice
delicious|adj|lezzetli|very good to eat
sweet|adj|tatlı|tasting of sugar
sour|adj|ekşi|tasting like lemon
spicy|adj|acı; baharatlı|hot in taste
fresh|adj|taze|recently made or picked
hungry|adj|aç|wanting food
thirsty|adj|susamış|wanting to drink
eat|v|yemek yemek|to put food in your mouth and swallow — ate, eaten
drink|v|içmek|to take liquid into your mouth — drank, drunk
have breakfast|phr|kahvaltı yapmak|to eat the morning meal
order|v|sipariş vermek; emretmek|to ask for food in a restaurant
pay|v|ödemek|to give money for something — paid, paid
taste|v|tatmak; tadı olmak|to try the flavour of food; to have a flavour
# ---- city / transport ----
city|n|şehir|a large town
town|n|kasaba; şehir|a place with many houses, smaller than a city
village|n|köy|a very small town
country|n|ülke; kırsal|a nation; land outside towns
capital|n|başkent|the main city of a country
street|n|sokak; cadde|a road in a town with buildings
road|n|yol|a hard surface for vehicles
square|n|meydan|an open area in a town
bridge|n|köprü|a structure built over a river or road
park|n|park|a public garden
centre|n|merkez|the middle (US: center)
building|n|bina|a structure with walls and a roof
church|n|kilise|a building where Christians pray
mosque|n|cami|a building where Muslims pray
museum|n|müze|a building where old or interesting things are shown
theatre|n|tiyatro|a building where plays are performed
cinema|n|sinema|a building where films are shown
library|n|kütüphane|a place where you can borrow books
school|n|okul|a place where children learn
university|n|üniversite|a place of higher education
bank|n|banka|a place that keeps money
post office|n|postane|a place where you send letters
hotel|n|otel|a building where you pay to sleep
station|n|istasyon; gar|a place where trains or buses stop
bus stop|n|otobüs durağı|a place where a bus stops
airport|n|havalimanı|a place where planes land and take off
underground|n|metro|a train system under a city (US: subway)
bus|n|otobüs|a large vehicle carrying many passengers
tram|n|tramvay|a vehicle on rails in a street
car|n|araba|a road vehicle with four wheels
taxi|n|taksi|a car you pay to be driven in
train|n|tren|vehicles joined together on rails
plane|n|uçak|a flying vehicle with wings
ship|n|gemi|a large boat
boat|n|tekne; kayık|a small vehicle for water
bicycle|n|bisiklet|a vehicle with two wheels you pedal
ticket|n|bilet|a paper that lets you travel or enter
passport|n|pasaport|an official document for travelling abroad
identity card|n|kimlik kartı|an official card showing who you are
border|n|sınır|the line between two countries
journey|n|yolculuk|travelling from one place to another
trip|n|gezi; seyahat|a short journey
tourist|n|turist|a person visiting a place for pleasure
map|n|harita|a drawing of an area
address|n|adres|the details of where a building is
traffic light|n|trafik ışığı|a signal with coloured lights for vehicles
crossroads|n|kavşak|a place where two roads cross
corner|n|köşe|the point where two lines or streets meet
car park|n|otopark|a place for leaving cars (US: parking lot)
petrol station|n|benzin istasyonu|a place that sells fuel (US: gas station)
traffic jam|n|trafik sıkışıklığı|a line of vehicles that cannot move
timetable|n|tarife; program|a list of times when trains or buses leave
departure|n|kalkış|leaving a place
arrival|n|varış|reaching a place
platform|n|peron|the raised area beside train tracks
entrance|n|giriş|the way in
exit|n|çıkış|the way out
right|adv|sağ; sağa|the side opposite to left
left|adv|sol; sola|the side opposite to right
straight on|phr|dümdüz|continuing in the same direction
far|adv|uzak|a long distance away
near|adv|yakın|a short distance away
here|adv|burada|in this place
there|adv|orada|in that place
at home|phr|evde|in your house
upstairs|adv|üst katta|on a higher floor
downstairs|adv|alt katta|on a lower floor
inside|adv|içeride|in a building or container
outside|adv|dışarıda|not in a building
everywhere|adv|her yerde|in all places
nowhere|adv|hiçbir yerde|in no place
# ---- movement verbs ----
go|v|gitmek|to move to another place — went, gone
come|v|gelmek|to move towards the speaker — came, come
walk|v|yürümek|to move on foot
run|v|koşmak|to move fast on foot — ran, run
drive|v|araba sürmek|to control a car — drove, driven
ride|v|binmek (bisiklet, at)|to sit on and control a bicycle or horse — rode, ridden
fly|v|uçmak|to move through the air — flew, flown
swim|v|yüzmek|to move through water — swam, swum
travel|v|seyahat etmek|to go to distant places
arrive|v|varmak|to reach a place
leave|v|ayrılmak; terk etmek; bırakmak|to go away from; to let something stay — left, left
enter|v|girmek|to go into
get in|phr|binmek (araba)|to enter a car
get out|phr|inmek (araba); çıkmak|to leave a car; to go out
get on|phr|binmek (otobüs, tren)|to enter a bus, train or plane
get off|phr|inmek (otobüs, tren)|to leave a bus, train or plane
return|v|geri dönmek; iade etmek|to go back; to give back
come back|phr|geri gelmek|to return
bring|v|getirmek|to carry something to a place — brought, brought
take|v|almak; götürmek|to carry something away; to get — took, taken
fetch|v|gidip getirmek|to go and bring back
pick up|phr|almak (yerden); arabayla almak|to lift; to collect someone in a car
follow|v|takip etmek|to go after someone
jump|v|zıplamak; atlamak|to push yourself into the air
fall|v|düşmek|to drop down — fell, fallen
climb|v|tırmanmak|to go up using hands and feet
cross|v|karşıya geçmek|to go from one side to the other
turn|v|dönmek|to change direction
stop|v|durmak; durdurmak|to end movement
hurry|v|acele etmek|to move quickly
# ---- core verbs ----
be|v|olmak|to exist; used to describe — was/were, been
have|v|sahip olmak|to own; to possess — had, had
do|v|yapmak|to perform an action — did, done
make|v|yapmak; üretmek|to create or produce — made, made
say|v|söylemek; demek|to speak words — said, said
tell|v|anlatmak; söylemek|to give information to someone — told, told
speak|v|konuşmak|to say words; to know a language — spoke, spoken
talk|v|konuşmak; sohbet etmek|to speak with someone
ask|v|sormak; istemek|to put a question; to request
answer|v|cevap vermek|to reply
know|v|bilmek; tanımak|to have information; to be familiar with — knew, known
think|v|düşünmek|to use your mind — thought, thought
believe|v|inanmak|to think something is true
understand|v|anlamak|to know the meaning — understood, understood
mean|v|anlamına gelmek; kastetmek|to have as meaning — meant, meant
want|v|istemek|to wish for
need|v|ihtiyacı olmak|to require
can|v|-ebilmek|to be able to — could
must|v|-meli; zorunda olmak|to have to
should|v|-meli (tavsiye)|used to give advice
may|v|-ebilir (izin, olasılık)|used for permission or possibility
like|v|sevmek; hoşlanmak|to enjoy; to find pleasant
love|v|sevmek; âşık olmak|to like very much
hate|v|nefret etmek|to dislike very much
prefer|v|tercih etmek|to like one thing more than another
see|v|görmek|to notice with the eyes — saw, seen
look|v|bakmak|to turn your eyes towards
watch|v|izlemek|to look at for some time
hear|v|duymak|to notice sound with the ears — heard, heard
listen|v|dinlemek|to pay attention to sound
read|v|okumak|to look at and understand words — read, read
write|v|yazmak|to make letters or words — wrote, written
learn|v|öğrenmek|to get knowledge or skill — learned/learnt
study|v|çalışmak (ders); okumak|to spend time learning
teach|v|öğretmek|to give lessons — taught, taught
practise|v|pratik yapmak|to do something again to improve (US: practice)
work|v|çalışmak|to do a job
play|v|oynamak; çalmak (enstrüman)|to take part in a game; to make music
give|v|vermek|to hand something to someone — gave, given
get|v|almak; elde etmek; olmak|to receive; to obtain; to become — got, got/gotten
receive|v|almak (teslim)|to get something sent to you
buy|v|satın almak|to get by paying money — bought, bought
sell|v|satmak|to give in exchange for money — sold, sold
shop|v|alışveriş yapmak|to buy things in shops
cost|v|mal olmak|to have a price — cost, cost
spend|v|harcamak|to use money or time — spent, spent
open|v|açmak|to move so that something is no longer closed
close|v|kapatmak|to shut
begin|v|başlamak|to start — began, begun
start|v|başlamak; başlatmak|to begin
finish|v|bitirmek|to end; to complete
end|v|bitmek; sona ermek|to stop; to come to a finish
continue|v|devam etmek|to keep doing
wait|v|beklemek|to stay until something happens
look for|phr|aramak|to try to find
find|v|bulmak|to discover — found, found
lose|v|kaybetmek|to no longer have — lost, lost
remember|v|hatırlamak|to keep in your mind
forget|v|unutmak|to fail to remember — forgot, forgotten
help|v|yardım etmek|to make something easier for someone
call|v|aramak (telefon); çağırmak|to phone; to shout for
meet|v|tanışmak; buluşmak|to see someone for the first time; to come together — met, met
show|v|göstermek|to let someone see — showed, shown
explain|v|açıklamak|to make clear
translate|v|çevirmek (dil)|to change words into another language
repeat|v|tekrarlamak|to say or do again
send|v|göndermek|to make something go to a place — sent, sent
put|v|koymak|to place — put, put
sit|v|oturmak|to rest on your bottom — sat, sat
stand|v|ayakta durmak|to be on your feet — stood, stood
lie|v|uzanmak; yalan söylemek|to be flat on a surface; to say untrue things — lay, lain / lied
hold|v|tutmak|to have in your hands — held, held
keep|v|saklamak; tutmak|to continue to have — kept, kept
feel|v|hissetmek|to experience an emotion or touch — felt, felt
fear|v|korkmak|to be afraid of
hope|v|ummak|to want something to happen
decide|v|karar vermek|to choose after thinking
solve|v|çözmek|to find an answer to a problem
try|v|denemek; çalışmak|to attempt
dream|v|rüya görmek; hayal etmek|to see pictures while sleeping; to imagine
laugh|v|gülmek|to make sounds showing you are happy
smile|v|gülümsemek|to make a happy face
cry|v|ağlamak|to have tears in your eyes
shout|v|bağırmak|to say loudly
sing|v|şarkı söylemek|to make music with your voice — sang, sung
dance|v|dans etmek|to move your body to music
draw|v|çizmek|to make a picture with a pen — drew, drawn
paint|v|boyamak; resim yapmak|to make a picture with paint
go for a walk|phr|yürüyüşe çıkmak|to walk for pleasure
be interested in|phr|ilgilenmek|to want to know about
be called|phr|adı olmak|to have as a name
marry|v|evlenmek|to become husband and wife
be born|phr|doğmak|to come into the world
die|v|ölmek|to stop living
grow|v|büyümek; yetiştirmek|to become bigger; to make plants develop — grew, grown
change|v|değiştirmek; değişmek|to make or become different
build|v|inşa etmek|to make a building — built, built
break|v|kırmak; bozmak|to separate into pieces — broke, broken
repair|v|tamir etmek|to fix something broken
fix|v|tamir etmek; sabitlemek|to repair; to attach firmly
throw|v|atmak; fırlatmak|to send through the air with your hand — threw, thrown
lift|v|kaldırmak|to raise to a higher position
carry|v|taşımak|to hold and move something
be late|phr|geç kalmak|to arrive after the expected time
succeed|v|başarmak|to achieve what you wanted
invite|v|davet etmek|to ask someone to come
suggest|v|önermek|to give an idea for consideration
advise|v|tavsiye etmek|to tell someone what they should do
recommend|v|tavsiye etmek; önermek|to say something is good
promise|v|söz vermek|to say you will certainly do something
allow|v|izin vermek|to let someone do something
forbid|v|yasaklamak|to say something must not be done — forbade, forbidden
check|v|kontrol etmek|to make sure something is correct
choose|v|seçmek|to pick from several — chose, chosen
compare|v|karşılaştırmak|to look at differences and similarities
count|v|saymak|to say numbers in order
calculate|v|hesaplamak|to find a number using mathematics
use|v|kullanmak|to do something with a tool or thing
plan|v|planlamak|to decide what you will do
organise|v|düzenlemek; organize etmek|to arrange (US: organize)
take part|phr|katılmak|to be involved in an activity
win|v|kazanmak (yarışma)|to be the best in a game — won, won
earn|v|kazanmak (para)|to get money for work
happen|v|olmak; gerçekleşmek|to take place
seem|v|görünmek; gibi olmak|to appear to be
exist|v|var olmak|to be real
belong|v|ait olmak|to be owned by
stay|v|kalmak|to remain in a place
let|v|izin vermek; bırakmak|to allow — let, let
visit|v|ziyaret etmek|to go to see a person or place
greet|v|selamlamak|to welcome with words
thank|v|teşekkür etmek|to say you are grateful
apologise|v|özür dilemek|to say sorry (US: apologize)
worry|v|endişelenmek|to feel anxious
complain|v|şikâyet etmek|to say you are unhappy about something
argue|v|tartışmak|to disagree angrily
discuss|v|görüşmek; tartışmak|to talk about something seriously
agree|v|kabul etmek; aynı fikirde olmak|to have the same opinion
refuse|v|reddetmek|to say no
pay attention|phr|dikkat etmek|to watch or listen carefully
notice|v|fark etmek|to see or become aware of
describe|v|tanımlamak; betimlemek|to say what something is like
introduce|v|tanıştırmak; tanıtmak|to tell someone another person's name
imagine|v|hayal etmek|to form a picture in your mind
depend|v|bağlı olmak|to be decided by something else
develop|v|geliştirmek; gelişmek|to grow or make better
protect|v|korumak|to keep safe
destroy|v|yok etmek|to damage completely
save|v|kurtarmak; biriktirmek; kaydetmek|to rescue; to keep money; to store a file
waste|v|israf etmek|to use badly
deserve|v|hak etmek|to be worthy of
quit|v|bırakmak (iş, alışkanlık)|to leave a job; to stop — quit, quit
manage|v|yönetmek; başarmak|to be in charge of; to succeed in doing
smoke|v|sigara içmek|to breathe in tobacco smoke
lose weight|phr|kilo vermek|to become thinner
put on weight|phr|kilo almak|to become heavier
treat|v|tedavi etmek; davranmak|to give medical care; to behave towards
cure|v|iyileştirmek|to make an illness go away
# ---- adjectives ----
big|adj|büyük|large in size
small|adj|küçük|little in size
large|adj|büyük; geniş|big
little|adj|küçük; az|small; not much
good|adj|iyi|of high quality; pleasant — better, best
bad|adj|kötü|not good — worse, worst
new|adj|yeni|recently made or bought
beautiful|adj|güzel|very pleasant to look at
handsome|adj|yakışıklı|attractive (of a man)
pretty|adj|güzel; hoş|attractive (of a woman or thing)
ugly|adj|çirkin|unpleasant to look at
clever|adj|zeki; akıllı|quick to learn and understand
smart|adj|akıllı; şık|clever; neat in appearance
stupid|adj|aptal|not clever
kind|adj|nazik; iyi kalpli|caring about others
nice|adj|hoş; güzel; iyi|pleasant; friendly
friendly|adj|arkadaş canlısı|behaving in a kind way
angry|adj|kızgın|feeling strong displeasure
funny|adj|komik|making you laugh
sad|adj|üzgün|unhappy
happy|adj|mutlu|feeling pleasure
glad|adj|memnun|pleased
interesting|adj|ilginç|holding your attention
boring|adj|sıkıcı|not interesting
important|adj|önemli|having great value or effect
difficult|adj|zor|not easy
hard|adj|zor; sert|difficult; not soft
easy|adj|kolay|not difficult
simple|adj|basit|easy to understand; not complicated
complicated|adj|karmaşık|difficult to understand
expensive|adj|pahalı|costing a lot of money
cheap|adj|ucuz|costing little money
rich|adj|zengin|having a lot of money
poor|adj|fakir; zavallı|having little money; deserving pity
strong|adj|güçlü|having power
weak|adj|zayıf; güçsüz|not strong
high|adj|yüksek|far above the ground
low|adj|alçak; düşük|near the ground; not high
tall|adj|uzun boylu|of great height (people, buildings)
short|adj|kısa|not long or tall
long|adj|uzun|of great length
wide|adj|geniş|measuring a lot from side to side
narrow|adj|dar|measuring little from side to side
thick|adj|kalın|not thin
thin|adj|ince; zayıf|not thick; not fat
fat|adj|şişman|having too much flesh
heavy|adj|ağır|weighing a lot
light|adj|hafif; açık (renk)|not heavy; not dark
hot|adj|sıcak|having a high temperature
warm|adj|ılık; sıcak|slightly hot
cold|adj|soğuk|having a low temperature
cool|adj|serin; havalı|slightly cold; fashionable
fast|adj|hızlı|moving quickly
quick|adj|hızlı; çabuk|done in a short time
slow|adj|yavaş|not fast
loud|adj|gürültülü; yüksek sesli|making a lot of noise
quiet|adj|sessiz|making little noise
clean|adj|temiz|not dirty
dirty|adj|kirli|not clean
bright|adj|parlak; aydınlık|full of light
dark|adj|karanlık; koyu|with little light
full|adj|dolu|containing as much as possible
empty|adj|boş|containing nothing
open|adj|açık|not closed
closed|adj|kapalı|not open
free|adj|özgür; ücretsiz; boş|not controlled; costing nothing; available
busy|adj|meşgul|having a lot to do
ready|adj|hazır|prepared
right|adj|doğru; sağ|correct; opposite of left
wrong|adj|yanlış|not correct
true|adj|doğru; gerçek|correct; real
false|adj|yanlış; sahte|not true
real|adj|gerçek|existing; not imaginary
possible|adj|mümkün|able to happen
impossible|adj|imkânsız|not able to happen
necessary|adj|gerekli|needed
same|adj|aynı|not different
different|adj|farklı|not the same
similar|adj|benzer|almost the same
next|adj|sonraki; gelecek|coming immediately after
previous|adj|önceki|coming before
own|adj|kendi|belonging to you
personal|adj|kişisel|belonging to one person
comfortable|adj|rahat|making you feel relaxed
dangerous|adj|tehlikeli|able to cause harm
safe|adj|güvenli|not in danger
sure|adj|emin|certain
honest|adj|dürüst|telling the truth
polite|adj|kibar|showing good manners
serious|adj|ciddi|not joking; important
wet|adj|ıslak|covered in water
dry|adj|kuru|not wet
soft|adj|yumuşak|not hard
round|adj|yuvarlak|shaped like a circle
alive|adj|canlı; hayatta|living
dead|adj|ölü|not alive
famous|adj|ünlü|known by many people
popular|adj|popüler|liked by many people
modern|adj|modern|of the present time
foreign|adj|yabancı|from another country
English|adj|İngiliz; İngilizce|from England; the English language
Turkish|adj|Türk; Türkçe|from Turkey; the Turkish language
hard-working|adj|çalışkan|working with effort
lazy|adj|tembel|not wanting to work
calm|adj|sakin|not excited or worried
nervous|adj|gergin; endişeli|worried and anxious
crazy|adj|çılgın; deli|very strange; mad
alone|adj|yalnız|without other people
together|adv|birlikte|with each other
whole|adj|bütün; tüm|complete; all of
favourite|adj|en sevdiği|liked most (US: favorite)
tasty|adj|lezzetli|having a good flavour
# ---- colours ----
colour|n|renk|red, blue, green etc. (US: color)
white|adj|beyaz|the colour of snow
black|adj|siyah|the colour of night
red|adj|kırmızı|the colour of blood
blue|adj|mavi|the colour of the sky
green|adj|yeşil|the colour of grass
yellow|adj|sarı|the colour of the sun
orange|adj|turuncu|the colour between red and yellow
brown|adj|kahverengi|the colour of wood
grey|adj|gri|between black and white (US: gray)
pink|adj|pembe|light red
purple|adj|mor|between red and blue
# ---- adverbs / prepositions / conjunctions ----
very|adv|çok|to a great degree
too|adv|de/da; fazla|also; more than is good
almost|adv|neredeyse|nearly
only|adv|sadece; yalnızca|no more than
also|adv|ayrıca; de|in addition
even|adv|hatta; bile|used to show surprise
about|adv|hakkında; yaklaşık|on the subject of; approximately
exactly|adv|tam olarak|precisely
really|adv|gerçekten|truly; very
probably|adv|muhtemelen|likely
certainly|adv|kesinlikle|without doubt
unfortunately|adv|ne yazık ki|used to say something is sad
hopefully|adv|umarım|used to say what you hope
especially|adv|özellikle|more than others
quite|adv|oldukça|rather; fairly
rather|adv|oldukça; daha ziyade|fairly; more willingly
at all|phr|hiç|in any way (negatives)
actually|adv|aslında|in fact
by the way|phr|bu arada|used to introduce a new topic
so|conj|bu yüzden; öyle|therefore; to such a degree
therefore|adv|bu nedenle|for that reason
however|adv|ancak; bununla birlikte|but; despite that
anyway|adv|her neyse; zaten|in any case
otherwise|adv|aksi takdirde|if not
besides|adv|ayrıca; üstelik|in addition
not|adv|değil; -me|used to make a negative
and|conj|ve|used to join words
or|conj|veya; ya da|used to give a choice
but|conj|ama; fakat|used to show contrast
because|conj|çünkü|for the reason that
that|conj|ki; -diği|used to introduce a clause
whether|conj|-ip -mediği|if (in indirect questions)
if|conj|eğer; -se|on condition that
although|conj|-e rağmen; her ne kadar|despite the fact that
so that|conj|-sin diye; için|in order that
before|conj|önce|earlier than
after|conj|sonra|later than
while|conj|-iken; sırasında|during the time that
until|prep|-e kadar|up to the time when
since|prep|-den beri|from a time in the past
in|prep|içinde; -de|inside; during
on|prep|üstünde; -de|touching the top of; about
at|prep|-de; -da (nokta)|in a particular place or time
under|prep|altında|below
over|prep|üzerinde; boyunca|above; more than
above|prep|yukarısında|higher than
below|prep|aşağısında|lower than
in front of|prep|önünde|ahead of
behind|prep|arkasında|at the back of
next to|prep|yanında|beside
between|prep|arasında|in the space separating two things
among|prep|arasında (çoklu)|in the middle of several
with|prep|ile; birlikte|accompanied by; using
without|prep|-sız; olmadan|not having
for|prep|için|intended to be given to; during
against|prep|karşı|opposing; touching
through|prep|içinden; boyunca|from one side to the other
across|prep|karşıdan karşıya|from one side to the other of
from|prep|-den; -dan|starting at
to|prep|-e; -a|in the direction of
of|prep|-in; -nın|belonging to; made from
by|prep|tarafından; yanında; ile|done by; near; using
near|prep|yakınında|close to
around|prep|etrafında; civarında|on all sides of; approximately
except|prep|hariç|not including
because of|prep|yüzünden; nedeniyle|as a result of
despite|prep|-e rağmen|without being affected by
instead of|prep|yerine|in place of
along|prep|boyunca|from one end to the other
opposite|prep|karşısında|facing
during|prep|sırasında; boyunca|throughout the time of
# ---- education / language ----
language|n|dil|words used by a nation
word|n|kelime; sözcük|a unit of language with meaning
sentence|n|cümle|a group of words expressing a complete idea
alphabet|n|alfabe|the letters of a language in order
grammar|n|dil bilgisi|the rules of a language
dictionary|n|sözlük|a book listing words and meanings
vocabulary|n|kelime hazinesi|all the words a person knows
lesson|n|ders|a period of teaching
class|n|sınıf|a group of students taught together
course|n|kurs|a series of lessons
exam|n|sınav|a formal test
test|n|test; sınav|questions to check knowledge
mark|n|not (puan); işaret|a grade for schoolwork; a sign
grade|n|not; sınıf (ABD)|a mark for schoolwork; a school year (US)
mistake|n|hata|something done wrongly
question|n|soru|a sentence that asks for information
answer|n|cevap|a reply to a question
rule|n|kural|a statement of what is allowed
example|n|örnek|something that shows what a thing is like
exercise|n|alıştırma; egzersiz|a task for practice; physical activity
homework|n|ödev|schoolwork done at home
text|n|metin|written words
story|n|hikâye; öykü|a description of events, real or invented
history|n|tarih (bilim)|the study of past events
literature|n|edebiyat|books, poems and plays
mathematics|n|matematik|the study of numbers
physics|n|fizik|the science of matter and energy
chemistry|n|kimya|the science of substances
biology|n|biyoloji|the science of living things
geography|n|coğrafya|the study of the earth's surface
science|n|bilim|knowledge based on facts and experiments
meaning|n|anlam|what a word or sign expresses
translation|n|çeviri|words changed into another language
pronunciation|n|telaffuz|the way a word is said
spelling|n|yazım; imla|the way a word is written
memory|n|hafıza; anı|the ability to remember; something remembered
attention|n|dikkat|careful listening or watching
knowledge|n|bilgi|what you know
experience|n|deneyim; tecrübe|knowledge from doing things
board|n|tahta; pano|a flat surface for writing in class
break|n|mola; teneffüs|a short rest from work
degree|n|derece; diploma|a unit of temperature; a university qualification
education|n|eğitim|the process of teaching and learning
# ---- money / shopping ----
price|n|fiyat|the money you must pay
pound|n|sterlin; libre|the British money; a unit of weight
dollar|n|dolar|the money of the USA and other countries
euro|n|avro; euro|the money of many European countries
cash|n|nakit|money in coins and notes
change|n|bozuk para; para üstü; değişiklik|money given back; a difference
discount|n|indirim|a reduction in price
offer|n|teklif; kampanya|something proposed; a special price
shop|n|dükkân; mağaza|a place that sells things (US: store)
supermarket|n|süpermarket|a large shop selling food and goods
market|n|pazar; piyasa|a place with stalls selling things
shopping centre|n|alışveriş merkezi|a large building with many shops (US: mall)
department store|n|büyük mağaza|a large shop with many sections
goods|n|mallar|things for sale
product|n|ürün|something made to be sold
quality|n|kalite|how good something is
credit card|n|kredi kartı|a card used to pay later
account|n|hesap|an arrangement to keep money in a bank
debt|n|borç|money you owe
tax|n|vergi|money paid to the government
insurance|n|sigorta|an agreement that pays if something bad happens
receipt|n|fiş; makbuz|a paper showing you have paid
# ---- communication / technology ----
internet|n|internet|the worldwide computer network
website|n|web sitesi|pages on the internet
email|n|e-posta|a message sent by computer
message|n|mesaj|information sent to someone
number|n|sayı; numara|a figure like 1, 2, 3; a telephone number
phone call|n|telefon görüşmesi|an act of talking by phone
connection|n|bağlantı|a link between things
information|n|bilgi|facts about something
news|n|haber|new information about events
programme|n|program|a show on TV; a plan (US: program)
app|n|uygulama|a program for a phone or computer
screen|n|ekran|the flat surface where pictures appear
keyboard|n|klavye|the set of keys for typing
mouse|n|fare|a small animal; a device to control a computer — plural: mice
file|n|dosya|a collection of data on a computer
folder|n|klasör|a container for files
password|n|şifre; parola|a secret word for access
printer|n|yazıcı|a machine that prints
radio|n|radyo|a device that receives sound broadcasts
music|n|müzik|sounds arranged in a pleasing way
song|n|şarkı|a piece of music with words
film|n|film|a story shown on a screen (US: movie)
series|n|dizi|a set of TV programmes with the same characters
game|n|oyun|an activity with rules for fun
camera|n|kamera; fotoğraf makinesi|a device for taking photos
battery|n|pil; batarya|a device that stores electricity
charge|v|şarj etmek; ücret almak|to fill with electricity; to ask for money
switch on|phr|açmak (cihaz)|to make a device work
switch off|phr|kapatmak (cihaz)|to stop a device working
download|v|indirmek|to copy from the internet
print|v|yazdırmak|to put words on paper with a machine
delete|v|silmek|to remove data
# ---- nature / weather ----
nature|n|doğa|plants, animals and the land
weather|n|hava durumu|the conditions in the air, like rain or sun
sun|n|güneş|the star that gives us light
moon|n|ay (gök cismi)|the object that shines at night
star|n|yıldız|a point of light in the night sky
sky|n|gökyüzü|the space above the earth
cloud|n|bulut|a white or grey mass in the sky
rain|n|yağmur|water falling from clouds
snow|n|kar|soft white frozen water
wind|n|rüzgâr|moving air
storm|n|fırtına|very bad weather with wind and rain
fog|n|sis|thick cloud near the ground
ice|n|buz|frozen water
frost|n|don; kırağı|ice crystals on cold surfaces
heat|n|sıcaklık; ısı|the quality of being hot
temperature|n|sıcaklık (derece)|how hot or cold something is
earth|n|dünya; toprak|the planet we live on; soil
world|n|dünya|the earth and everything on it
air|n|hava|the gas we breathe
fire|n|ateş; yangın|flames and heat
sea|n|deniz|the salt water covering the earth
lake|n|göl|a large area of water with land around
river|n|nehir; ırmak|a long line of water flowing to the sea
beach|n|plaj; kumsal|sand by the sea
island|n|ada|land with water all around
mountain|n|dağ|a very high hill
hill|n|tepe|a raised area of land
forest|n|orman|a large area of trees
field|n|tarla; alan|open land on a farm; an area of study
tree|n|ağaç|a tall plant with a trunk
flower|n|çiçek|the coloured part of a plant
grass|n|çimen; ot|green plants covering the ground
leaf|n|yaprak|the flat green part of a plant — plural: leaves
stone|n|taş|a hard piece of rock
sand|n|kum|tiny grains found on beaches
animal|n|hayvan|a living creature that is not a plant
dog|n|köpek|an animal kept as a pet that barks
cat|n|kedi|an animal kept as a pet that purrs
horse|n|at|a large animal people ride
cow|n|inek|a farm animal that gives milk
pig|n|domuz|a farm animal kept for meat
sheep|n|koyun|a farm animal with wool — plural: sheep
bird|n|kuş|an animal with feathers and wings
bear|n|ayı|a large wild animal with fur
wolf|n|kurt|a wild animal like a dog — plural: wolves
fox|n|tilki|a wild animal with a bushy tail
rabbit|n|tavşan|a small animal with long ears
snake|n|yılan|a long animal without legs
insect|n|böcek|a small animal with six legs
it's raining|phr|yağmur yağıyor|rain is falling
it's snowing|phr|kar yağıyor|snow is falling
it's cold|phr|hava soğuk|the temperature is low
it's hot|phr|hava sıcak|the temperature is high
sunny|adj|güneşli|with a lot of sun
cloudy|adj|bulutlu|with many clouds
windy|adj|rüzgârlı|with a lot of wind
rainy|adj|yağmurlu|with a lot of rain
# ---- sport / leisure ----
sport|n|spor|physical games and activities
football|n|futbol|a game played with a round ball and feet (US: soccer)
basketball|n|basketbol|a game where you throw a ball into a net
tennis|n|tenis|a game played with rackets and a ball
chess|n|satranç|a board game with kings and queens
swimming pool|n|yüzme havuzu|a place built for swimming
stadium|n|stadyum|a large sports ground with seats
team|n|takım|a group playing together
match|n|maç; kibrit|a sports game; a small stick for making fire
training|n|antrenman; eğitim|practice for sport; teaching a skill
victory|n|zafer|winning
hobby|n|hobi|an activity you enjoy in free time
free time|n|boş zaman|time when you are not working
concert|n|konser|a performance of music
exhibition|n|sergi|a public show of art or objects
party|n|parti|a social event with food and music
celebrate|v|kutlamak|to do something special for a happy event
club|n|kulüp|a group of people with a shared interest
# ---- feelings / abstract ----
life|n|hayat; yaşam|the state of being alive — plural: lives
death|n|ölüm|the end of life
love|n|aşk; sevgi|a strong feeling of liking
friendship|n|arkadaşlık; dostluk|the relationship between friends
happiness|n|mutluluk|the feeling of being happy
joy|n|sevinç|great happiness
fear|n|korku|the feeling of being afraid
hope|n|umut|the wish for something good
dream|n|rüya; hayal|pictures in your mind while sleeping; a wish
truth|n|gerçek; hakikat|what is true
lie|n|yalan|something said that is not true
thought|n|düşünce|an idea in your mind
idea|n|fikir|a thought or plan
opinion|n|görüş; fikir|what you think about something
feeling|n|duygu; his|an emotion
mood|n|ruh hali|the way you feel at a time
wish|n|dilek; istek|something you want
interest|n|ilgi; faiz|wanting to know about; money paid on a loan
freedom|n|özgürlük|the state of being free
right|n|hak; sağ|something you are allowed to do
law|n|yasa; hukuk|the rules of a country
order|n|düzen; sipariş; emir|arrangement; a request for goods; a command
choice|n|seçim; tercih|the act of choosing
possibility|n|olasılık|something that may happen
reason|n|sebep; neden|why something happens
result|n|sonuç|what happens because of something
case|n|durum; dava|a situation; a legal matter
way|n|yol; yöntem|a route; a method
condition|n|koşul; durum|something needed; a state
difference|n|fark|the way things are not the same
part|n|parça; bölüm|a piece of something
end|n|son|the last part
beginning|n|başlangıç|the first part
middle|n|orta|the centre
place|n|yer|a position or location
side|n|taraf; yan|a surface or edge; a position
shape|n|şekil|the outer form of something
amount|n|miktar|how much of something
weight|n|ağırlık|how heavy something is
society|n|toplum|people living together in a country
government|n|hükümet|the group that rules a country
war|n|savaş|fighting between countries
peace|n|barış|a time without war
police|n|polis|the people who make sure laws are obeyed
culture|n|kültür|the way of life of a group
art|n|sanat|painting, music and so on
religion|n|din|belief in a god or gods
problem|n|sorun; problem|something difficult to deal with
solution|n|çözüm|the answer to a problem
success|n|başarı|achieving what you wanted
goal|n|hedef; gol|something you want to achieve; a point in football
plan|n|plan|a decision about what to do
project|n|proje|a piece of planned work
environment|n|çevre|the natural world around us
future|n|gelecek|the time after now
past|n|geçmiş|the time before now
event|n|olay; etkinlik|something that happens
situation|n|durum|the things happening at a time and place
relationship|n|ilişki|the way people are connected
responsibility|n|sorumluluk|a duty to deal with something
safety|n|güvenlik|being safe
"""
