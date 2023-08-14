
# from crypto.Signature import PKCS1_v1_5 as pkcs1_15

# assume we have the following values from the signer:
# - public_key_str: a string representation of the signer's public key
# - message: the original message that was signed
# - signature: the signature produced by the signer

# decode the public key string into a public key object

public_key_exponent = 392258566177228421003307163115947242815517871624631346717903090126183229961109078608342578163598544639622348202706543378823300088456883716985766040382644690051369069625958008556393429941624722757709382524339053411899932974709863724907463406457849329362041190772559250370176157243358852378076238590288446625795740023167910191944892114699320336423735090837750695594223736222510923939649696426928762998517863923455023695417014805496507969365103694350956840083697749628667309373156586686021297211143603439410721216878350102213309630769130802884522003445391500494548058822350680966358881915605035172879540978904253362113560029781449127241228204729141552159698795244641081047611758479766943839402621065569750521120268614530804394293404236301633926071076003951216064620786685895873926785302749487684914715815005629198774569205055134698286336157591963290688030424388212546378087749555889820425456929285924290951941362949113624394522203689840720862318809091019236390754594484374812656228776477607354012640882612578715682360365292998500549094805076700975327154157532015535319026829069350406798663710472594013364313895723676175335189775078187220105972761202562137292852196696256630306821660274491661468683563193575338424185876895777002134950079
signature = 87494733585960957318030830131766228225629166401609907492083244295482946642239053454222747306770765877707383803023347030000290499830497079319185184409903108321653229923454190847937197694144384917210193038533409232520998217532429649989465543472938859201088899047103824946039296423943972867025848539055047255771286985339222861173875978514930677100302735807066746019423935378426021125426111042368017514830610362185766750893979297900743435878459189352426041846857662116729140486917412351701076185023889597434692490798771401979240116055357328597748677924677201518869855148297859686393144924672319892710786483230145110956847006822269307367077144219669366287895030746245613124444914563886844037817270432938672825551795982245837752100621553004072754600729574888587666971535937423716947671952634668428688516913028034071662807003541004174931713067956709029377085352876508977982955775693415621540182186258442499592020195761405404470998817856677729548379261022114181158904501831911561308694257178289714263366809303360336388125727645197759222398132596338405216242207341251121827791770691526281188060972127965824459805508395597178384791596750949981245100796236455226966255608737782831962996738427037179482459713885373592712203168329896970016595616
public_key_modulus = 978343753983864632934132839195853117896241689443550875110886716937174674783978295616042758552613849639294800835757377634690412265606103863151338610110074973908114654389907712471613655474825774184994188818815616366551325608949454415133690912755811142975666223418690297090945704993359431747073714097833955302828588811232672930165448005672344371898933520378804914549450687908005191796198966937439550192524318229272235188344905117037072775608654151682250620461830891382565008824941039394203099930611700135431295507033144849913560530196811806315259587075928025723029936674990831293827642345936756802656612453502104640756494491199832830181004559024543069235378985520363829172213062915883368795562003991463450976462622347556960955375426310622571085527831257165449374761510200575531365371528337081863860767046517841420622194145478014921535691622051066852750705655045059778094771965802633150652251949528118567136368712984504106175826731612606749594021236221956601290456504638395955485639370621654334426763805725188487061715203222083138089946811148799686853562215201364411223784989619653383732973584109192689433339944808088044894866709106748605313371418821987552925662446494298682197285324200726507537573125967597817238673790638491070842144973
message=72427457666856278697997504399689717323721298251763565367093434846140185798694

# create a RSA object from the modulus and exponent values
decrypted_signature = pow(signature, public_key_exponent, public_key_modulus)

print(decrypted_signature)
